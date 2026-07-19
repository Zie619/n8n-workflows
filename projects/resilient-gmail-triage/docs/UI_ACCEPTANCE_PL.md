# Test akceptacyjny przez UI n8n

## Ważne: manualny `02` wymaga trzech przebiegów

Worker akcji celowo zapisuje checkpoint po każdym efekcie ubocznym:

```text
1. CLASSIFIED → DRAFT_CREATED
2. DRAFT_CREATED → NOTIFIED
3. NOTIFIED → PROCESSED
```

To nie jest pętla wykonywana trzy razy w jednym manualnym execution. Przy aktywnym harmonogramie kolejne kroki wykonują się automatycznie co minutę.

## Przygotowanie

1. Wszystkie cztery workflow pozostaw nieaktywne.
2. W Credentials sprawdź, czy nie ma czerwonych ostrzeżeń przy:
   - `Gmail - Contact Mailbox`
   - `Gemini - Mail Triage`
   - `Discord - Mail Triage`
   - `Discord - Automation Alerts`
3. Data Table `message_processing_state` powinna być pusta przed czystym testem.
4. Usuń z Gmaila `AUTO/PROCESSING` pozostawione przez wcześniejsze częściowe wykonania.

## Test klasyfikacji

1. Wyślij jeden fikcyjny mail z unikalnym subjectem.
2. Otwórz `01 - Gmail Triage - Intake and Classify`.
3. Z listy triggerów wybierz `Manual Intake`.
4. Kliknij Execute workflow.
5. Sprawdź, czy execution dochodzi do:
   - `Normalize and Guard`
   - `Gemini Structured Classify`
   - `Finalize and Validate`
   - `Save CLASSIFIED`
6. W Data Table oczekuj `status = CLASSIFIED`.

Nie uruchamiaj `02`, jeśli 01 zatrzymał się przed `Save CLASSIFIED`.

## Test draftu, Discorda i finalizacji

Otwórz `02 - Gmail Triage - Act and Notify`, wybierz trigger `Manual Act` i wykonuj pojedynczo:

### Przebieg 1

Oczekiwane:

- dokładnie jeden Gmail draft;
- `status = DRAFT_CREATED`;
- `draft_created = true`;
- brak Discorda jest w tym momencie prawidłowy.

### Przebieg 2

Oczekiwane:

- dokładnie jeden alert Discord;
- `status = NOTIFIED` lub `NEEDS_ESCALATION`;
- `discord_notified = true`;
- nie powstaje drugi draft.

### Przebieg 3

Oczekiwane:

- `status = PROCESSED`;
- Gmail ma `AUTO/PROCESSED`;
- Gmail nie ma `AUTO/PROCESSING`;
- nadal istnieje tylko jeden draft i jeden alert Discord.

## Test health

1. W `03` uruchom najpierw trigger `Every 15 Minutes`.
2. Następnie uruchom `Daily Health Report`.
3. Znaczenie kolorów:
   - 🟢 `HEALTHY` — brak pending/stale;
   - 🟠 `DEGRADED` — istnieje pending lub quarantine;
   - 🔴 `CRITICAL` — istnieje stale item albo przekroczony próg;
   - ⚪ `UNKNOWN` — telemetry danego komponentu nie była aktualizowana od ponad 30 minut.

Raport nie powinien przedstawiać starej telemetry jako zielonej.

## Aktywacja

Dopiero po pełnym przejściu jednego maila aktywuj/publikuj w kolejności:

1. `04 - Gmail Triage - Global Error Handler`
2. `01 - Gmail Triage - Intake and Classify`
3. `02 - Gmail Triage - Act and Notify`
4. `03 - Gmail Triage - Recovery and Diagnostics`

Po aktywacji normalny mail może potrzebować do około trzech minut na pełną ścieżkę draft → Discord → finalizacja.
