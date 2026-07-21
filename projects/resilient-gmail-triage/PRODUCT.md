# Product

## Register

product

## Users

Osoba testująca automatyzację obsługi skrzynki kontaktowej: rekruter, klient pilotażowy albo członek pięcioosobowego zespołu. Korzysta z narzędzia w przeglądarce podczas testu akceptacyjnego i chce wysłać kontrolowaną wiadomość bez używania terminala.

## Product Purpose

Narzędzie wysyła bezpieczne, syntetyczne wiadomości do jednej skonfigurowanej skrzynki testowej. Użytkownik może wybrać gotowy scenariusz, wysłać małą paczkę, wylosować przypadek albo wpisać własny temat i treść. Sukces oznacza, że przed wysyłką wiadomo dokładnie co zostanie wysłane, a po wysyłce otrzymuje identyfikator i instrukcję sprawdzenia wyniku w Gmailu, Discordzie oraz n8n.

## Brand Personality

Spokojny, precyzyjny, odpowiedzialny. Interfejs mówi prostym językiem i nie udaje, że test jest bez ryzyka. Ważniejsze od efektu wizualnego są kontrola, czytelne statusy i zaufanie.

## Anti-references

Nie powinien przypominać landing page'a SaaS, klienta pocztowego ani panelu do masowych kampanii. Bez dekoracyjnych gradientów, szklanych kart, wielkich metryk i marketingowych obietnic. Nie może sugerować, że można wysyłać wiadomości do dowolnych odbiorców.

## Design Principles

1. Pokaż zakres wysyłki przed wykonaniem działania.
2. Ogranicz możliwe szkody w backendzie, nie tylko w interfejsie.
3. Każdy status powinien mówić, co się stało i gdzie sprawdzić kolejny etap.
4. Gotowe scenariusze mają uczyć sposobu testowania, a nie tylko dostarczać dane.
5. Własna wiadomość powinna być równie łatwa do wysłania jak fixture, ale podlegać tym samym limitom.

## Accessibility & Inclusion

Cel: WCAG 2.1 AA. Pełna obsługa klawiatury, widoczne focus states, semantyczne formularze, komunikaty statusowe z `aria-live`, kontrast tekstu co najmniej 4.5:1 oraz brak interakcji zależnych wyłącznie od koloru. Ruch ograniczony do krótkiej informacji zwrotnej i wyłączany przez `prefers-reduced-motion`.
