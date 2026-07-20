const state = {
  config: null,
  scenarios: [],
  mode: "prepared",
  selected: new Set(),
  preview: [],
  previewIndex: 0,
  csrfToken: "",
};

const elements = {};

function cacheElements() {
  const ids = [
    "transport", "recipient", "load-error", "prepared-panel", "custom-panel", "random-panel",
    "scenario-list", "select-all", "custom-form", "custom-subject", "custom-body", "subject-count",
    "body-count", "subject-error", "body-error", "draw-random", "selection-summary", "preview-position",
    "preview-empty", "mail-preview", "preview-recipient", "preview-category", "preview-urgency", "preview-subject", "preview-body",
    "preview-prev", "preview-next", "confirm-send", "confirm-label", "send-button", "activity-log", "clear-log"
  ];
  ids.forEach((id) => { elements[id] = document.getElementById(id); });
  elements.modeButtons = [...document.querySelectorAll(".mode-button")];
}

async function fetchJson(url, options = {}) {
  const response = await fetch(url, options);
  let payload;
  try {
    payload = await response.json();
  } catch (_error) {
    throw new Error(`Serwer zwrócił nieprawidłową odpowiedź (${response.status}).`);
  }
  if (!response.ok) throw new Error(payload.error || `Błąd HTTP ${response.status}`);
  return payload;
}

function scenarioById(id) {
  return state.scenarios.find((scenario) => scenario.id === id);
}

function badge(text, className, urgency = "") {
  const item = document.createElement("span");
  item.className = className;
  item.textContent = text;
  if (urgency) item.dataset.urgency = urgency;
  return item;
}

function renderScenarios() {
  elements["scenario-list"].replaceChildren();
  state.scenarios.forEach((scenario) => {
    const row = document.createElement("div");
    row.className = "scenario-row";

    const check = document.createElement("input");
    check.type = "checkbox";
    check.id = `scenario-${scenario.id}`;
    check.checked = state.selected.has(scenario.id);
    check.setAttribute("aria-label", `Wybierz: ${scenario.title}`);
    check.addEventListener("change", () => {
      if (check.checked) state.selected.add(scenario.id);
      else state.selected.delete(scenario.id);
      updatePreparedPreview(scenario.id);
      updateSelectAllLabel();
    });

    const show = document.createElement("button");
    show.type = "button";
    show.className = "scenario-row__button";
    const title = document.createElement("strong");
    title.textContent = scenario.title;
    const description = document.createElement("span");
    description.textContent = scenario.description;
    show.append(title, description);
    show.addEventListener("click", () => {
      if (!state.selected.has(scenario.id)) state.selected.add(scenario.id);
      renderScenarios();
      updatePreparedPreview(scenario.id);
      updateSelectAllLabel();
    });

    const meta = document.createElement("div");
    meta.className = "scenario-row__meta";
    meta.append(
      badge(scenario.category, "badge"),
      badge(scenario.urgency, "badge badge--neutral", scenario.urgency)
    );
    row.append(check, show, meta);
    elements["scenario-list"].append(row);
  });
  updateSelectAllLabel();
}

function updateSelectAllLabel() {
  const allSelected = state.scenarios.length > 0 && state.selected.size === state.scenarios.length;
  elements["select-all"].textContent = allSelected ? "Odznacz wszystkie" : "Zaznacz wszystkie";
}

function updatePreparedPreview(preferredId = null) {
  state.preview = [...state.selected].map(scenarioById).filter(Boolean);
  if (preferredId) {
    const index = state.preview.findIndex((item) => item.id === preferredId);
    state.previewIndex = index >= 0 ? index : 0;
  } else {
    state.previewIndex = Math.min(state.previewIndex, Math.max(state.preview.length - 1, 0));
  }
  renderPreview();
}

function customPreview() {
  const subject = elements["custom-subject"].value.trim();
  const body = elements["custom-body"].value.trim();
  elements["subject-count"].textContent = `${elements["custom-subject"].value.length}/200`;
  elements["body-count"].textContent = `${elements["custom-body"].value.length}/5000`;
  elements["subject-error"].textContent = subject ? "" : "Temat jest wymagany.";
  elements["body-error"].textContent = body ? "" : "Treść jest wymagana.";
  elements["custom-subject"].setAttribute("aria-invalid", subject ? "false" : "true");
  elements["custom-body"].setAttribute("aria-invalid", body ? "false" : "true");
  state.preview = subject && body ? [{ id: "custom", title: "Własna wiadomość", category: "UNKNOWN", urgency: "unknown", subject, body }] : [];
  state.previewIndex = 0;
  renderPreview();
}

function renderPreview() {
  const count = state.preview.length;
  const item = count ? state.preview[state.previewIndex] : null;
  elements["preview-empty"].hidden = Boolean(item);
  elements["mail-preview"].hidden = !item;
  elements["preview-position"].hidden = count < 2;
  elements["preview-position"].textContent = count ? `${state.previewIndex + 1} z ${count}` : "";
  elements["preview-prev"].disabled = state.previewIndex <= 0;
  elements["preview-next"].disabled = state.previewIndex >= count - 1;

  if (item) {
    elements["preview-category"].textContent = item.category;
    elements["preview-urgency"].textContent = item.urgency;
    elements["preview-urgency"].dataset.urgency = item.urgency;
    elements["preview-subject"].textContent = item.subject;
    elements["preview-body"].textContent = item.body;
  }

  const summary = count === 0
    ? "Wybierz scenariusz, aby zobaczyć treść."
    : count === 1 ? "Przygotowano 1 wiadomość." : `Przygotowano ${count} wiadomości.`;
  elements["selection-summary"].textContent = summary;
  elements["confirm-send"].checked = false;
  elements["confirm-send"].disabled = count === 0;
  elements["confirm-label"].textContent = count === 0
    ? "Najpierw przygotuj wiadomość."
    : `Potwierdzam wysyłkę ${count} ${count === 1 ? "wiadomości" : "wiadomości"} do skonfigurowanego odbiorcy.`;
  updateSendButton();
}

function updateSendButton() {
  const count = state.preview.length;
  elements["send-button"].disabled = count === 0 || !elements["confirm-send"].checked;
  const dry = state.config?.transport === "dry-run";
  elements["send-button"].textContent = dry
    ? (count > 1 ? `Zasymuluj ${count} wiadomości bez wysyłki` : "Zasymuluj bez wysyłki")
    : (count > 1 ? `Wyślij ${count} wiadomości` : "Wyślij wiadomość");
}

function switchMode(mode) {
  state.mode = mode;
  elements.modeButtons.forEach((button) => {
    const active = button.dataset.mode === mode;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  elements["prepared-panel"].hidden = mode !== "prepared";
  elements["custom-panel"].hidden = mode !== "custom";
  elements["random-panel"].hidden = mode !== "random";
  if (mode === "prepared") updatePreparedPreview();
  if (mode === "custom") customPreview();
  if (mode === "random") {
    state.preview = [];
    state.previewIndex = 0;
    renderPreview();
  }
}

function requestPayload() {
  if (state.mode === "custom") {
    return {
      mode: "custom",
      subject: elements["custom-subject"].value.trim(),
      body: elements["custom-body"].value.trim(),
      confirmedCount: state.preview.length,
    };
  }
  return {
    mode: "selected",
    scenarioIds: state.preview.map((item) => item.id),
    confirmedCount: state.preview.length,
  };
}

function addLogRow({ ok, subject, messageId = "", detail = "" }) {
  const empty = elements["activity-log"].querySelector(".activity-empty");
  if (empty) empty.remove();
  const row = document.createElement("li");
  const time = document.createElement("time");
  const now = new Date();
  time.dateTime = now.toISOString();
  time.textContent = now.toLocaleTimeString("pl-PL", { hour: "2-digit", minute: "2-digit", second: "2-digit" });
  const description = document.createElement("div");
  const status = document.createElement("span");
  status.className = ok ? "result-success" : "result-error";
  status.textContent = ok ? "Wysłano" : "Błąd";
  const text = document.createElement("span");
  text.textContent = ` ${subject || detail}`;
  description.append(status, text);
  const id = document.createElement("code");
  id.textContent = messageId || detail;
  row.append(time, description, id);
  elements["activity-log"].prepend(row);
}

async function sendPrepared() {
  if (!elements["confirm-send"].checked || state.preview.length === 0) return;
  elements["send-button"].disabled = true;
  elements["send-button"].textContent = "Wysyłanie…";
  try {
    const payload = await fetchJson("/api/send", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-CSRF-Token": state.csrfToken },
      body: JSON.stringify(requestPayload()),
    });
    payload.results.forEach((result) => addLogRow({ ok: true, subject: result.subject, messageId: result.messageId }));
    elements["confirm-send"].checked = false;
  } catch (error) {
    addLogRow({ ok: false, detail: error.message });
  } finally {
    updateSendButton();
  }
}

function bindEvents() {
  elements.modeButtons.forEach((button) => button.addEventListener("click", () => switchMode(button.dataset.mode)));
  elements["select-all"].addEventListener("click", () => {
    if (state.selected.size === state.scenarios.length) state.selected.clear();
    else state.scenarios.forEach((scenario) => state.selected.add(scenario.id));
    renderScenarios();
    updatePreparedPreview();
  });
  elements["custom-subject"].addEventListener("input", customPreview);
  elements["custom-body"].addEventListener("input", customPreview);
  elements["draw-random"].addEventListener("click", () => {
    const scenario = state.scenarios[Math.floor(Math.random() * state.scenarios.length)];
    state.preview = scenario ? [scenario] : [];
    state.previewIndex = 0;
    renderPreview();
  });
  elements["preview-prev"].addEventListener("click", () => { state.previewIndex -= 1; renderPreview(); });
  elements["preview-next"].addEventListener("click", () => { state.previewIndex += 1; renderPreview(); });
  elements["confirm-send"].addEventListener("change", updateSendButton);
  elements["send-button"].addEventListener("click", sendPrepared);
  elements["clear-log"].addEventListener("click", () => {
    const empty = document.createElement("li");
    empty.className = "activity-empty";
    empty.textContent = "Nie wysłano jeszcze żadnej wiadomości.";
    elements["activity-log"].replaceChildren(empty);
  });
}

async function initialize() {
  cacheElements();
  bindEvents();
  try {
    const [config, scenarios] = await Promise.all([fetchJson("/api/config"), fetchJson("/api/scenarios")]);
    state.config = config;
    state.csrfToken = config.csrfToken;
    state.scenarios = scenarios;
    elements.transport.textContent = config.transport;
    elements.recipient.textContent = config.recipient;
    elements["preview-recipient"].textContent = config.recipient;
    renderScenarios();
    renderPreview();
  } catch (error) {
    elements["load-error"].textContent = `Nie udało się uruchomić konsoli: ${error.message}`;
    elements["load-error"].hidden = false;
    elements["scenario-list"].replaceChildren();
  }
}

document.addEventListener("DOMContentLoaded", initialize);
