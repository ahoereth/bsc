## Server {#sec:server}
Im folgenden wird zu Beginn auf diese Entscheidung Server und Client strukturell vollständig voneinander zu trennen und dann in Abschnitt @sec:rest und @sec:database auf die eingesetzte Server- und, respektive, Datenbank-Architektur eingegangen.

Auf Grund der Anforderung einer in Zukunft flexibel auf weitere Plattformen erweiterbaren Applikation kommt nur eine klare Trennung von Server und Client in Frage. Bei der Entwicklung eines reinen \ac{API}-Servers ist es wichtig, dass dieser Daten in einer von ihrer für den Endnutzer endgültigen Repräsentation unabhängigen, leicht zu verarbeiteten Form zur Verfügung stellt. Allerdings ist es gleichermaßen wichtig, die bereitgestellten Schnittstellen nicht zu abstrakt zu gestalten sondern Daten sinnvoll zu bündeln, um unnötig viele Anfragen durch die Client-Applikationen zu vermeiden.

Aus dieser Unabhängigkeit ergibt sich die Möglichkeit serverseitige Logik wie zum Beispiel Datenbankanfragen und Nutzer-Authentifizierung wiederzuverwenden. Im besten Fall wird für eine bestimmte Aufgabe wie zum Beispiel die Registrierung eines neuen Nutzers die serverseitige Logik nur ein einziges mal implementiert, so dass beliebige darauf angewiesene clientseitige Applikationen in Zukunft nur noch eine einmalige standardisierte Anfrage an den Server stellen müssen. Dadurch ist es nicht Notwendig bei der Erstellung zusätzlicher Apps mit ähnlichem Funktionsumfang wie dem initialen Produkt Änderungen am Server vorzunehmen. Bei der Implementierung neuer Funktionalität muss so nur einmalig eine neue API-Schnittstelle hinzugefügt werden.

In Bezug auf eine Web-Applikation ergibt sich zusätzlich der Vorteil, dass die API und die eigentliche für den Nutzer zur Verfügung gestellte Applikation auf unabhängigen Servern bereitgestellt werden können. So ist es Möglich flexibel auf Lastspitzen durch Skalierung des jeweils betroffenen zu reagieren.

### Application Programming Interface
Für das geplante Produkt gibt es zwei Konzepte die für den API-Server interessant sind:

  1. Eine REST-API, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Die zentrale Unterscheidung zwischen den beiden Ansätzen ist das `pull/push`-Prinzip. Bei einer REST-API werden mithilfe von sogenannten HTTP-Verben einzelne Anfragen an den Server gestellt, auf welche der Server reagiert. Diese Anfragen sind im besten Fall für den Server komplett voneinander unabhängig und nicht auf einen gewissen serverseitig vorgehaltenen Zustand angewiesen. Bildlich werden per Anfrage also Daten vom Server *gepulled* . Ein Übertragen von Daten an den Clienten ist nur als einmalige Antwort auf eine von diesem initiierte Anfrage möglich.

Im Gegensatz dazu muss sich bei der Verwendung von WebSockets der Client nur für einen initialen Verbindungsaufbau beim Server anmelden. Ab diesem Zeitpunkt wird eine Verbindung zwischen Server und Clienten aufrechterhalten, an die beide, wann immer aktualisierte Informationen vorhanden sind, Daten *pushen* und auf über diesen Weg erhaltene Daten reagieren können.[^longpolling]

[^longpolling]: Für bessere Kompatibilität mit älteren Browsern ist auch möglich, sogenanntes *long-polling* einzusetzen. Hierbei erfolgt der Verbindungsaufbau wie bei einer Rest-API, allerdings wird die ankommende Anfrage nicht sofort beantwortet. Der Server hält die Verbindung offen und antwortet erst zu einem späteren Zeitpunkt auf die Anfrage. Sobald der Client eine Antwort erhält sendet er unmittelbar eine erneute Anfrage um dem Server wieder die Möglichkeit zu eröffnen ihm gewissermaßen ungefragt Daten zu übermitteln.

\color{red}{Stateful/stateless...}

  * representational state transfer
  * HTTP verbs
  * stateless
  * Ausblick für sockets
  * Strukturelle Problematik bei multi-server setups.

Im Rahmen dieser Arbeit wird nur Punkt 1, die REST-API, umgesetzt. Websockets 

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



### Database

  * sql
  * no-sql
  * --> postgres

