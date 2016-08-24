## Server
\label{sec:server}

Auf Grund der Anforderung eines flexibel auf mehr Plattformen erweiterbaren Produktes kommt für den Server nur eine reine \ac{API}-Struktur in Frage. Als Grundlegend gilt hierbei, dass der Server keinerlei Wissen über die eigentliche Darstellung der Daten auf Client-Seite hat, sondern diese nur in ihrer Rohform in über klar definierte und intuitiv verständliche Endpunkte zur Verfügung stellt.

  1. Eine REST-API, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Wie zuvor dargestellt ist eine zentrale und für viele Neulinge verwirrende Eigenschaft von JavaScript die Ereignisschleife bzw. der Event Loop. Bei beispielsweise in PHP geschriebenen Servern wird bei jeder eintreffenden Netzwerkanfrage eine Instanz gestartet in welcher der komplette Quelltext ausgeführt wird. Im Falle eines Node.js-Servers hingegen wird die Applikation initial einmalig komplett interpretiert und lauscht von nun an auf Ereignisse bzw. Events. Ein solches Event ist wäre im Fall eines Servers zum Beispiel das Eintreffen einer Netzwerkanfrage. Der Server lauscht auf dieses `connection` Ereignis und behandelt es mit Hilfe einer vordefinierten Funktion, einen sogenannten Handlers. Dieser Handler ist nichts anderes als ein Callback für eine asynchrone Funktion, wie in Kapitel @sec:concurrency beschrieben.

~~~{#lst:js:server_listen}
import http from 'http';
const server = http.createServer();

server.on('request', (request, response) => {
  response.end(`Received a request at ${request.url}!`);
});

server.listen(8080, () => {
  console.log('Listening on port 8080');
});
~~~



### REST

  * representational state transfer
  * HTTP verbs
  * stateless


### Sockets

  * Ausblick
  * Strukturelle Problematik bei multi-server setups.


