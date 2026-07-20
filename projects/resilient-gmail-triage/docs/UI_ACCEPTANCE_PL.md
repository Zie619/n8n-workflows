# Test akceptacyjny przez UI n8n

## Najprostsza ścieżka

Do wysyłania wiadomości użyj lokalnej Test Mail Console opisanej w [`../tools/mail_tester/README.md`](../tools/mail_tester/README.md). Odbiorca jest ustawiony po stronie serwera, a każda wiadomość otrzymuje unikatowy znacznik `E2E`.

## Dlaczego workflow 02 potrzebuje trzech ticków

Worker akcji zapisuje checkpoint po każdym efekcie ubocznym:

```text
1. CLASSIFIED → DRAFT_CREATED
2. DRAFT_CREATED → NOTIFIED
3. NOTIFIED → PROCESSED
```

To nie jest pętla wykonywana trzy razy w jednym execution. Przy aktywnym harmonogramie kolejne kroki wykonują się automatycznie co minutę.

## Przygotowanie

1. W czystym imporcie pozostaw wszystkie pięć workflow nieaktywne.
2. Sprawdź dziewięć credentiali wymienionych w głównym README.
3. Potwierdź obecność tabel `message_processing_state`, `system_health` i `system_events`.
4. Potwierdź etykiety Gmail `AUTO/*`.
5. Ustaw role Discord przez environment variables.
6. Nie aktywuj workflow 05 poza kontrolowanym testem błędu.

Nie trzeba opróżniać tabeli stanu przed każdym testem. Unikatowy Gmail message ID oraz znacznik E2E pozwalają odróżnić nowe wykonanie. Czyszczenie tabel ma sens wyłącznie przy osobnym, kontrolowanym teście od zera.

## Test klasyfikacji

1. Wyślij jeden przygotowany fixture przez Test Mail Console.
2. Otwórz `01 - Gmail Triage - Intake and Classify`.
3. Przy nieaktywnym Gmail Triggerze wybierz `Manual Intake` i uruchom workflow.
4. Sprawdź wykonanie węzłów:
   - `Normalize and Guard`;
   - `Gemini Structured Classify` dla zwykłego maila;
   - `Finalize and Validate`;
   - `Save CLASSIFIED`.
5. W Data Table oczekuj `CLASSIFIED`. Dla prompt injection prawidłowym wynikiem jest `QUARANTINED` bez wywołania Gemini.

Nie uruchamiaj akcji, jeśli zwykły mail zatrzymał się przed `Save CLASSIFIED`.

## Test draftu, Discorda i finalizacji

Przy nieaktywnym harmonogramie otwórz `02 - Gmail Triage - Act and Notify`, wybierz `Manual Act` i wykonuj pojedynczo.

### Przebieg 1

- powstaje dokładnie jeden Gmail draft;
- `status = DRAFT_CREATED`;
- `draft_created = true`;
- brak Discorda jest na tym etapie prawidłowy.

### Przebieg 2

- powstaje dokładnie jedna notyfikacja na właściwym kanale Discord;
- notyfikacja zawiera kategorię, urgency, rolę, podsumowanie, propozycję odpowiedzi i link Gmail;
- `status = NOTIFIED`;
- `discord_notified = true`;
- nie powstaje drugi draft.

### Przebieg 3

- `status = PROCESSED`;
- Gmail ma `AUTO/PROCESSED` i etykietę kategorii;
- Gmail nie ma `AUTO/PROCESSING`;
- wiadomość krytyczna ma etykietę pilną;
- nadal istnieje tylko jeden draft i jedna notyfikacja.

## Test prompt injection

1. Wyślij fixture `Próba prompt injection`.
2. Oczekuj `QUARANTINED`.
3. Nie powinien powstać Gmail draft.
4. Zwykłe kanały biznesowe nie powinny otrzymać wiadomości.
5. Kanał `Discord - Inne` powinien otrzymać jeden alert metadata-only.

## Test health

1. W workflow 03 uruchom trigger `Every 15 Minutes`.
2. Następnie uruchom `Daily Health Report`.
3. Interpretacja:
   - `HEALTHY`: brak pending i stale;
   - `DEGRADED`: istnieje bieżąca praca oczekująca;
   - `CRITICAL`: istnieje stale backlog, przekroczony próg albo retry-exhausted quarantine;
   - `UNKNOWN`: telemetry nie była aktualizowana przez ponad 30 minut.

## Test automatycznego error handlera

1. Tymczasowo aktywuj workflow 05.
2. Uruchom jego manualny launcher albo kontrolowany endpoint lokalny.
3. Oczekuj wpisu w `system_events` i oczyszczonego alertu na Discordzie.
4. Po demonstracji natychmiast wyłącz workflow 05.

Nie wyłączaj Gmaila, Gemini ani Discorda tylko po to, żeby wywołać błąd.

## Aktywacja

Po pełnym teście aktywuj workflow w kolejności:

1. `04 - Gmail Triage - Global Error Handler`;
2. `01 - Gmail Triage - Intake and Classify`;
3. `02 - Gmail Triage - Act and Notify`;
4. `03 - Gmail Triage - Recovery and Diagnostics`.

Workflow 05 pozostaje nieaktywny. Normalna wiadomość może potrzebować kilku kolejnych minutowych ticków na ścieżkę draft → Discord → finalizacja.
