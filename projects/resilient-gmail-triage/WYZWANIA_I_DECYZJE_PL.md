# Wyzwania i decyzje projektowe

## Największe wyzwanie

Najtrudniejsze nie było samo połączenie Gmaila, Gemini i Discorda. Problem pojawia się wtedy, gdy workflow wykona tylko część pracy. Draft może już istnieć, a Discord chwilowo nie odpowiadać. Zwykłe ponowienie całego procesu utworzyłoby drugi draft. Jeszcze gorszy wariant to mail pobrany z Gmaila, który znika z kolejki po błędzie i nikt o tym nie wie.

Dlatego każdy mail ma trwały rekord oparty na Gmail message ID. Utworzenie draftu i wysłanie Discorda mają osobne checkpointy. Kolejny tick wykonuje tylko brakującą część pracy. Recovery sprawdza stare rekordy oraz wiadomości obecne w Gmailu, których nie ma w Data Table.

## Decyzje projektowe

### Draft zamiast automatycznej odpowiedzi

AI przygotowuje propozycję, ale jej nie wysyła. Człowiek nadal odpowiada za ton, zobowiązania i poprawność informacji przekazywanej klientowi.

### Role zamiast konkretnych użytkowników

Workflow oznacza role Discord, na przykład Sprzedaż, Finanse albo Crisis. Gdy zmienia się skład zespołu, administrator aktualizuje członkostwo w roli bez edycji automatyzacji.

### Guard przed wywołaniem AI

Treść maila jest danymi zewnętrznymi. Najbardziej oczywiste próby prompt injection i wyłudzenia sekretów są wykrywane deterministycznie przed Gemini. Taki mail trafia do kwarantanny i nie otrzymuje draftu.

### Kilka mniejszych workflow zamiast jednego dużego

Intake, efekty uboczne, recovery i globalne błędy mają osobne odpowiedzialności. Ułatwia to diagnozę i pozwala ponowić bezpiecznie tylko ten etap, który się nie udał.

### Osobne kanały Discord

Kategorie są kierowane do siedmiu webhooków. Ogranicza to szum na jednym wspólnym kanale i upraszcza kontrolę dostępu. Normalna notyfikacja zawiera summary oraz draft, więc kanał powinien mieć podobny poziom ochrony jak skrzynka kontaktowa.

## Czego nie zrealizowałem w tej wersji

- Data Tables nie mają atomowego claimu rekordu. Przy większej liczbie równoległych execution zastosowałbym bazę z blokadą albo ograniczenie concurrency.
- Nie ma osobnej redakcji PII w summary i drafcie wysyłanym na Discord. Na produkcji dodałbym ją lub ograniczył treść notyfikacji.
- Korekta błędnej kategorii przez użytkownika nie wraca automatycznie do zbioru testowego. Następnym krokiem byłby prosty feedback loop z kategorią oczekiwaną.
- Routing jest czytelny, ale jego mapa nadal znajduje się w kodzie workflow. Przy częstych zmianach przeniósłbym ją do tabeli konfiguracyjnej z wersjonowaniem.
- Recovery jest dostosowane do małej skrzynki. Większy wolumen wymaga paginacji, indeksów i mierzonego limitu batcha.
- Lokalna Test Mail Console nasłuchuje tylko na loopback. Dostęp dla zewnętrznego klienta wymaga reverse proxy z uwierzytelnieniem.

Nie dodawałem integracji CRM ani automatycznego tworzenia zadań. To oddzielny zakres z własnymi uprawnieniami, deduplikacją i obsługą błędów. Najpierw domknąłbym stabilny proces mailowy, a dopiero później rozszerzał liczbę efektów ubocznych.
