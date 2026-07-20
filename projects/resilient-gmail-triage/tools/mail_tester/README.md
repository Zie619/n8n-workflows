# Test Mail Console

Lokalna strona do testowania przepływu Gmail → Gemini → Discord bez używania terminala. Pozwala wybrać pojedynczy scenariusz, małą paczkę, losowy przypadek albo własny temat i treść.

Adres odbiorcy pochodzi wyłącznie z konfiguracji backendu. Formularz nie przyjmuje pola `recipient`, więc klient nie może użyć aplikacji do wysyłki na dowolne adresy.

## Szybki start: dry-run

```bash
TEST_MAIL_TRANSPORT=dry-run \
TEST_MAIL_RECIPIENT=contact@example.invalid \
python3 -m tools.mail_tester.app --port 8040
```

Otwórz `http://127.0.0.1:8040`. Ten tryb nie wysyła wiadomości. Pozwala sprawdzić interfejs, fixture'y i log sesji.

## Opcjonalny test przez adapter Gmail API środowiska Hermes

Ten wariant nie korzysta z credentiala n8n. Wymaga opcjonalnego skryptu `google_api.py` z instalacji Hermes Agent oraz osobnej autoryzacji Google Workspace. Na standardowym checkoutcie repozytorium wybierz autoryzowany relay SMTP opisany niżej. Brak adaptera jest wykrywany przy starcie z jednoznacznym komunikatem. Nie wpisuj tokenu ani hasła w formularzu.

```bash
TEST_MAIL_TRANSPORT=gmail-api \
TEST_MAIL_RECIPIENT=adres-skrzynki-testowej@example.com \
python3 -m tools.mail_tester.app --port 8040
```

Po wysłaniu sprawdź kolejno:

1. nową wiadomość i etykietę `AUTO/*` w Gmailu;
2. draft odpowiedzi w Gmailu;
3. właściwy kanał oraz rolę na Discordzie;
4. execution workflow 01 i 02 w n8n.

Gmail Trigger odpytuje skrzynkę co minutę, a kolejne checkpointy workflow 02 również przechodzą w minutowych tickach.

## Lokalny SMTP z Mailpit

Mailpit sprawdza, czy aplikacja prawidłowo buduje i przekazuje wiadomości do serwera SMTP. Przechwytuje je lokalnie. Nie dostarcza ich do Gmaila, więc nie uruchomi workflow n8n opartego na skrzynce Gmail.

```bash
docker compose -f tools/mail_tester/docker-compose.mailpit.yml up -d

TEST_MAIL_TRANSPORT=smtp \
TEST_MAIL_RECIPIENT=contact@example.invalid \
TEST_MAIL_FROM=tester@example.invalid \
TEST_MAIL_SMTP_HOST=127.0.0.1 \
TEST_MAIL_SMTP_PORT=1025 \
python3 -m tools.mail_tester.app --port 8040
```

Konsola aplikacji: `http://127.0.0.1:8040`

Skrzynka Mailpit: `http://127.0.0.1:8025`

## Zewnętrzny relay SMTP

Można podłączyć dowolny autoryzowany relay SMTP. Dane logowania pozostają po stronie procesu serwera:

```bash
export TEST_MAIL_TRANSPORT=smtp
export TEST_MAIL_RECIPIENT=adres-skrzynki-testowej@example.com
export TEST_MAIL_FROM=adres-nadawcy@example.com
export TEST_MAIL_SMTP_HOST=smtp.example.com
export TEST_MAIL_SMTP_PORT=587
export TEST_MAIL_SMTP_STARTTLS=true
export TEST_MAIL_SMTP_USERNAME=...
export TEST_MAIL_SMTP_PASSWORD=...
python3 -m tools.mail_tester.app --port 8040
```

Nie zapisuj rzeczywistych wartości w repozytorium. Aplikacja nie zwraca ich przez API i nie umieszcza ich w logach. Przy `STARTTLS` certyfikat serwera oraz hostname są weryfikowane przez systemowy trust store.

## Ograniczenia bezpieczeństwa

- serwer domyślnie nasłuchuje wyłącznie na `127.0.0.1`;
- próba uruchomienia na publicznym interfejsie jest odrzucana;
- odbiorca jest stały i konfigurowany po stronie serwera;
- maksymalna paczka ma 12 wiadomości;
- temat ma limit 200, a body 5000 znaków;
- endpoint wysyłki wymaga tokenu CSRF;
- Content Security Policy blokuje skrypty zewnętrzne i `eval`;
- log audytowy zapisuje hash body, nie pełną treść;
- po błędzie transportu aplikacja nie wykonuje automatycznej ponownej wysyłki.

Jeśli strona ma być dostępna poza komputerem testowym, postaw przed nią reverse proxy z uwierzytelnieniem. Nie zmieniaj bind address bez takiej warstwy.

## Testy

```bash
pytest -q tests/test_mail_tester.py
```
