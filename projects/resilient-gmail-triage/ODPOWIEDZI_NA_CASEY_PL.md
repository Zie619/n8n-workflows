# Odpowiedzi na sytuacje projektowe

## Case 1: błędna klasyfikacja maili

**Temat: Re: Błędna klasyfikacja maili**

Cześć,

rozumiem problem. Jeśli reklamacja trafiła do spamu, nie powinniście jeszcze traktować klasyfikacji jako wiążącej. Do czasu poprawki zostawiłbym obecny proces jako wsparcie zespołu, a nie jedyne źródło decyzji.

Podeślijcie proszę kilka błędnie oznaczonych wiadomości wraz z kategorią, której oczekiwaliście. Najbardziej przydadzą się przykłady graniczne, zwłaszcza zapytanie ofertowe zaklasyfikowane jako „inne” i wspomniana reklamacja. Sprawdzę wtedy, czy problem leży w instrukcji dla modelu, zbyt szerokiej definicji spamu, czy w samej treści maila po normalizacji.

Na tej podstawie doprecyzuję reguły kategorii i dodam te wiadomości do stałego zestawu regresyjnego. Poprawkę najpierw uruchomię na kopii danych testowych. Uznajmy temat za zamknięty dopiero wtedy, gdy poprawione reguły przejdą cały zestaw, a wcześniejsze poprawne przypadki nie zaczną trafiać do złych kolejek.

Pozdrawiam<br>
Olek

---

## Case 2: klient nie rozumie decyzji AI

**Temat: Re: Dlaczego AI tak to oznaczyło?**

Cześć,

w tym przypadku system rozróżnia kategorie głównie na podstawie relacji nadawcy z firmą i intencji wiadomości. „Zapytanie ofertowe” oznacza nową potrzebę zakupu lub prośbę o wycenę. „Pytanie od obecnego klienta” dotyczy już trwającej współpracy, na przykład statusu projektu, zmiany zakresu albo problemu z bieżącą usługą.

Żeby wyjaśnić tę konkretną decyzję, potrzebuję treści maila albo jego identyfikatora z tabeli przetwarzania. Nie chcę dopowiadać uzasadnienia po fakcie bez sprawdzenia danych, które model rzeczywiście dostał.

Jeżeli takich niejasnych przypadków będzie więcej, dodam do wyniku krótką, ustandaryzowaną przyczynę klasyfikacji, na przykład „prośba o wycenę nowej usługi” albo „pytanie o aktywny projekt”. Dzięki temu zespół zobaczy nie tylko etykietę, ale też kryterium, które zadecydowało o routingu. Sprawdzimy rozwiązanie na przykładach z obu kategorii i wspólnie potwierdzimy, czy granica jest zrozumiała.

Pozdrawiam<br>
Olek

---

## Case 3: brak powiadomień i zdenerwowany klient

**Temat: Re: Co się dzieje?!**

Cześć,

traktuję to jako incydent. Na czas diagnozy proszę monitorować bezpośrednio skrzynkę Gmail, żeby żadna pilna wiadomość nie zależała od powiadomienia na Discordzie.

Sprawdzę po kolei, czy maile zostały pobrane, czy utknęły przed klasyfikacją, czy drafty powstały oraz czy problem dotyczy wyłącznie połączenia z Discordem. Zweryfikuję też status credentiala, ostatnie execution, kolejkę retry i wpisy w `system_events`. To pozwoli oddzielić awarię komunikatora od zatrzymania całego procesu.

Po diagnozie wrócę z trzema informacjami: od kiedy powiadomienia nie wychodziły, które wiadomości zostały dotknięte i co dokładnie naprawiliśmy. Następnie wykonamy kontrolowany test od nowego maila do Discorda. Incydent zamkniemy dopiero po sprawdzeniu zaległych wiadomości oraz potwierdzeniu, że nowy test przeszedł pełną ścieżkę.

Pozdrawiam<br>
Olek

---

## Case 4: klient podważa sens rozwiązania

**Temat: Re: Czy to ma sens?**

Cześć,

jeżeli podczas testów poświęcacie więcej czasu na kontrolę automatyzacji niż wcześniej na obsługę maili, to obecny sposób pilotażu wymaga uproszczenia. Sam fakt, że system działa technicznie, nie oznacza jeszcze, że oszczędza czas zespołu.

Proponuję przez kilka dni mierzyć cztery rzeczy: liczbę poprawnych przypisań, liczbę ręcznych korekt, czas od przyjścia maila do wskazania właściciela oraz czas potrzebny na poprawienie draftu. To pokaże, czy problemem jest jakość klasyfikacji, zbyt rozbudowany proces kontroli, czy drafty, które wymagają za dużo edycji.

Na czas pomiaru ograniczyłbym test do etykietowania, routingu i draftów, bez dodatkowych elementów diagnostycznych widocznych dla użytkownika. Po zebraniu wyników zdecydujemy, co zostawić, co uprościć, a z czego zrezygnować. Jeśli narzędzie nie skróci obsługi i nie zmniejszy liczby przeoczonych wiadomości, nie będę rekomendował wdrożenia go w obecnej formie.

Pozdrawiam<br>
Olek

---

## Case 5: niewykryta pilna reklamacja

**Temat: Re: PILNE: reklamacja klienta**

Cześć,

zgadzam się, że to błąd o wysokim priorytecie. Do czasu jego wyjaśnienia proponuję ręcznie obserwować wiadomości od kluczowych klientów i nie opierać eskalacji wyłącznie na decyzji modelu.

Podeślijcie proszę identyfikator tej wiadomości albo jej temat, czas otrzymania i nadawcę. Sprawdzę, jaką kategorię, urgency i confidence zwrócił model oraz czy reguły deterministyczne rozpoznały słowa i kontekst wskazujące na kryzys.

Dla kluczowych klientów dołożę twardą regułę opartą na kontrolowanej liście nadawców lub domen. Połączymy ją z sygnałami takimi jak awaria, blokada działania, reklamacja i bezpośrednia prośba o pilny kontakt. Model nadal będzie analizował treść, ale nie będzie jedyną warstwą decydującą o eskalacji.

Przed ponownym uruchomieniem sprawdzę ten mail oraz zestaw podobnych i niepilnych wiadomości. Chodzi o to, żeby wychwycić krytyczny przypadek bez oznaczania każdej reklamacji jako alarmu.

Pozdrawiam<br>
Olek

---

## Case 6: dodatkowe wymagania w trakcie wdrożenia

**Temat: Re: Jeszcze jedna rzecz**

Cześć,

możemy to dodać, ale potraktowałbym integrację z CRM jako osobny zakres, a nie drobną zmianę w obecnym wdrożeniu. Automatyczne tworzenie notatki i zadania wprowadza kolejne efekty uboczne, uprawnienia oraz ryzyko duplikatów.

Najpierw potrzebuję ustalić, z jakiego CRM korzystacie, przy których kategoriach ma powstawać zadanie, kto ma być właścicielem oraz jakie dane z maila wolno zapisać. Trzeba też uzgodnić zachowanie przy ponownym przetworzeniu tej samej wiadomości i przy błędzie połączenia z CRM.

Po krótkim doprecyzowaniu przygotuję osobną wycenę i plan zmiany. Obecny zakres możemy w tym czasie domknąć i przetestować bez czekania na CRM. Nową integrację uznamy za gotową po teście, który potwierdzi jedną notatkę i jedno zadanie dla danego maila, również po ponownym uruchomieniu workflow.

Pozdrawiam<br>
Olek

---

## Case 7: brak zaufania przed produkcją

**Temat: Re: Wątpliwości do wdrożenia**

Cześć,

te obawy są uzasadnione. Skrzynka kontaktowa nie powinna zależeć od procesu, który może zatrzymać się bez śladu.

Automatyzacja nie usuwa maili i nie wysyła odpowiedzi samodzielnie. Przygotowuje draft do zatwierdzenia przez człowieka. Każdy mail ma trwały rekord stanu, a utworzenie draftu i powiadomienia jest zapisane osobnymi checkpointami. Jeśli integracja chwilowo nie odpowie, system wykonuje ograniczone retry. Recovery szuka też wiadomości, które są w Gmailu, ale nie pojawiły się w tabeli przetwarzania. Błędy trafiają do `system_events` i na techniczny kanał Discord.

Nie oznacza to, że ryzyko spada do zera. Przed produkcją uruchomiłbym etap równoległy: zespół nadal obserwuje Gmail, a my codziennie porównujemy liczbę nowych maili z liczbą rekordów zakończonych lub świadomie poddanych kwarantannie. Ustalimy też prostą procedurę awaryjną na wypadek braku alertów.

Produkcję włączymy dopiero po przejściu testu zwykłego maila, pilnej eskalacji, spamu, prompt injection i kontrolowanej awarii. Kryterium jest proste: żadna wiadomość nie może zniknąć bez terminalnego statusu albo widocznego alertu.

Pozdrawiam<br>
Olek
