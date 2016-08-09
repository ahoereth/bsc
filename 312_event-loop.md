### Event-Loop
Eine alternative Herangehensweise ist die Verwendung eines Event-Loops.  

Listing: **Nicht-blockierende Datenbank-Operation in JavaScript.** Code innerhalb der anonymen Funktion in Zeile 6/7 wird nach der Fertigstellung der Datenbank Anfrage ausgeführt. Programmcode in Zeile 9ff wird unmittelbar nach Absenden der Anfrage und vor Erhalt der Antwort ausgeführt. Die Ergebnis-Variable `rows` ist nur innerhalb der anonymen Funktion sichtbar.

~~~{#lst:javascriptio .javascript}
import mysql from 'mysql';
const db = mysql.createConnection(...configuration);
db.connect();

connection.query('SELECT * FROM foo', (err, rows) => {
  if (err) { throw err; }
  // Do something with the result rows.
});

// Non-blocking -- do something else concurrently.
// Result `rows` is not available here.
~~~

