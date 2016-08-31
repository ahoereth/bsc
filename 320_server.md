## Server {#sec:server}
Im folgenden wird zu Beginn auf die Entscheidung eingegangen, Server und Client strukturell vollständig voneinander zu trennen. In den Abschnitten @sec:api und @sec:database wird dann, respektive, die eingesetzte Server- und Datenbank-Architektur diskutiert.

Auf Grund der Anforderung einer in Zukunft flexibel auf weitere Plattformen erweiterbaren Applikation kommt nur eine klare Trennung von Server und Client in Frage. Bei der Entwicklung eines reinen \ac{API}-Servers ist es wichtig, dass dieser Daten in einer von ihrer für den Endnutzer endgültigen Repräsentation unabhängigen, leicht zu verarbeiteten Form zur Verfügung stellt. Allerdings ist es gleichermaßen wichtig, die bereitgestellten Schnittstellen nicht zu abstrakt zu gestalten sondern Daten sinnvoll zu bündeln, um unnötig viele Anfragen durch die Client-Applikationen zu vermeiden.

Aus dieser Unabhängigkeit ergibt sich die Möglichkeit serverseitige Logik wie zum Beispiel Datenbankanfragen und Nutzer-Authentifizierung wiederzuverwenden. Im besten Fall wird für eine bestimmte Aufgabe wie zum Beispiel die Registrierung eines neuen Nutzers die serverseitige Logik nur ein einziges mal implementiert, so dass beliebige darauf angewiesene clientseitige Applikationen in Zukunft nur noch eine einmalige standardisierte Anfrage an den Server stellen müssen. Dadurch ist es nicht Notwendig bei der Erstellung zusätzlicher Apps mit ähnlichem Funktionsumfang wie dem initialen Produkt Änderungen am Server vorzunehmen. Bei der Implementierung neuer Funktionalität muss so nur einmalig eine neue API-Schnittstelle hinzugefügt werden.

In Bezug auf eine Web-Applikation ergibt sich zusätzlich der Vorteil, dass die API und die eigentliche für den Nutzer zur Verfügung gestellte Applikation auf unabhängigen Servern bereitgestellt werden können. So ist es Möglich flexibel auf Lastspitzen durch Skalierung des jeweils betroffenen zu reagieren.



### Application Programming Interface {#sec:api}
Für das geplante Produkt gibt es zwei Konzepte die für den API-Server interessant sind:

  1. Eine REST-API, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Die zentrale Unterscheidung zwischen den beiden Ansätzen ist das `pull/push`-Prinzip. Bei einer REST-API werden mithilfe von sogenannten HTTP-Verben einzelne Anfragen an den Server gestellt, auf welche der Server reagiert. Diese Anfragen sind im besten Fall für den Server komplett voneinander unabhängig und nicht auf einen gewissen serverseitig vorgehaltenen Zustand angewiesen. Bildlich werden per Anfrage also Daten vom Server *gepulled* . Ein Übertragen von Daten an den Clienten ist nur als einmalige Antwort auf eine von diesem initiierte Anfrage möglich.

Im Gegensatz dazu muss sich bei der Verwendung von WebSockets der Client nur für einen initialen Verbindungsaufbau beim Server anmelden. Ab diesem Zeitpunkt wird eine Verbindung zwischen Server und Clienten aufrechterhalten, an die beide, wann immer aktualisierte Informationen vorhanden sind, Daten *pushen* und auf über diesen Weg erhaltene Daten reagieren können.[^longpolling]

[^longpolling]: Für bessere Kompatibilität mit älteren Browsern ist auch möglich, sogenanntes *long-polling* einzusetzen. Hierbei erfolgt der Verbindungsaufbau wie bei einer Rest-API, allerdings wird die ankommende Anfrage nicht sofort beantwortet. Der Server hält die Verbindung offen und antwortet erst zu einem späteren Zeitpunkt auf die Anfrage. Sobald der Client eine Antwort erhält sendet er unmittelbar eine erneute Anfrage um dem Server wieder die Möglichkeit zu eröffnen ihm gewissermaßen ungefragt Daten zu übermitteln.


#### HTTP & REST
Aus diesen Erläuterungen geht ein für die Implementierung zentrales Unterscheidungsmerkmal hervor: Nur bei verfolgen des Rest-Prinzips ist es möglich, vollständig zustandslose Schnittstellen zu entwickeln. Der Server hält so keine Informationen über vorhergehende Anfragen vor, wodurch die Infrastruktur, wenn notwendig, horizontal skaliert (*horizontal scaling*) werden kann. Um dies zu erreichen, ist es notwendig, dass jede Anfrage auch relevante Authentifizierungsinformationen mitliefert. Siehe hierzu Abschnitt @sec:security.

Horizontal Scaling
:  Horizontale Skalierung
:  Bei der horizontalen Skalierung werden, je nach Notwendigkeit, unterschiedlich viele Maschinen in einem Pool zusammengeschaltet. Ein zentraler Schnittpunkt, der sogenannte *Load-Balancer*, verteilt in diesem Fall die Anfragen auf die einzelnen Server für eine gleichmäßige Lastverteilung. Im Gegensatz zur horizontalen steht die vertikale Skalierung: Ein einzelner Server wird, um mit erhöhter Last umgehen zu können, mit leistungsfähigeren Komponenten, also mehr Arbeitsspeicher, besserem Prozessor uws., ausgestattet.

  * \color{red}{representational state transfer}
  * \color{red}{HTTP verbs}
  * \color{red}{Ausblick für sockets}
  * \color{red}{Strukturelle Problematik bei multi-server setups.}

#### Express
Wie zuvor in Abschnitt #sec:concurrency:event ist eine zentrale und für viele Neulinge verwirrende Eigenschaft von JavaScript der Event Loop. Bei beispielsweise in PHP geschriebenen Servern wird bei jeder eintreffenden Netzwerkanfrage eine Instanz gestartet in welcher der komplette Quelltext ausgeführt wird. Im Falle eines Node.js-Servers hingegen wird die Applikation initial einmalig gestartet und lauscht von nun an auf auftretende Ereignisse. Ein solches Event ist im Fall eines Rest-API-Servers zum Beispiel das Eintreffen einer Netzwerkanfrage. Wie in Listing @lst:server:simple dargestellt, lauscht der Server auf ein solches `request` Event und behandelt es mithilfe einer vordefinierten Funktion, eines sogenannten Handlers. Dieser Handler ist nichts anderes als ein Callback für eine asynchrone Funktion, wie in Abschnitt @sec:js:runtime erläutert.

Listing: Einfacher Node.js Server

~~~{#lst:server:simple}
import http from 'http';
const server = http.createServer();
server.on('request', (request, response) => {
  response.end(`Received request at ${request.url}!`);
});
server.listen(8080, () => {
  console.log('Listening on port 8080');
});
~~~

Um leichter dem Rest-Prinzip folgen zu können wird bei der Applikation auf das Express-Framework gesetzt. Wie in Listing @lst:server:express filtert die eintreffenden HTTP-Anfragen und verteilt sie auf klar definierte Handler für einzelne HTTP-Verben und Pfade.

Listing: Node.js Server mit Express

~~~{#lst:server:express}
import { Server }  from 'http';
import express from 'express';
const app = express();
const server = Server(app);
app.get('/obj', (request, response) => {
  response.end(`Received GET request at /obj!`);
});
app.put('/obj/:id', (request, response) => {
  const { id } = request.params;
  response.end(`Received PUT request at /obj/${id}!`);
});
server.listen(8080, () => {
  console.log('Listening on port 8080');
});
~~~



### Database {#sec:database}
Im folgenden wird knapp auf die zentrale Unterscheidung zwischen normalisierten SQL- und denomalisierten Dokument-basierten Datenbanken eingegangen -- breiteres Vorwissen wird hier allerdings vorausgesetzt. Primär wird der durch neuere Versionen der Open Source Datenbank PostgreSQL ermöglichte Hybrid-Ansatz erläutert.

Als Datenbank kommen Grundlegend zwei verschiedene Ansätze in Frage: Traditionellere SQL- und in den letzten Jahren aufgekommene NoSQL- bzw. Dokument-Datenbanken. Besonders für schnell wachsende und im großen Stil Daten anhäufende Anwendungen haben sich in den letzten Jahren NoSQL-Datenbanken durchgesetzt. Sie basieren auf der Grundidee einzelne nicht direkt voneinander abhängige Dokumente zu speichern. Ähnlich wie bei dem verfolgten Ansatz eines Zustandslosen API-Servers, beschrieben zu Beginn von Abschnitt @sec:server, ist es so möglich die Datenbank horizontal durch hinzufügen neuer Instanzen zu skalieren.

Ein zentraler Aspekt von SQL-Datenbanken ist im Kontrast dazu eine meiste eingesetzte *normalisierte* Struktur: Bei strenger Einhaltung werden dabei Informationen niemals redundant abgespeichert. In dem Fall, das ein Nutzer ein bestimmtes Gesetz vorgemerkt hat, würden sich so zwei gegensätzliche Herangehensweisen ergeben: In einer Dokument-basierten Datenbank würde der Titel dieses Gesetzes direkt in dem dem Nutzer zugeordneten Dokument abgespeichert werden, so dass bei Zugriff auf dieses direkt alle von ihm vorgemerkten Gesetze verfügbar sind. In einer normalisierten SQL-Datenbank hingegen würde stattdessen ein neuer Eintrag erstellt werden, welcher auf die eindeutigen Identifikationsnummern des Nutzers und des Gesetzes verweist. Beim Abrufen der Nutzerinformation würde dann der Nutzer über solche *one-to-many* Beziehungen mit den vorgemerkten Gesetzen in Verbindung gebracht werden.

Ein Nachteil starker Normalisierung ist allerdings eine steigende Komplexität des Systems und der hohe Ressourcenanspruch. Bei komplexen Systemen sind mehrschichtige `Joins`, also das auflösen von normalisierten Beziehungen, rechenintensiv. Die Lösung hiervon besteht in intensivem Caching der Ergebnisse, was allerdings nur bei oft wiederkehrenden Anfragen hilfreich ist. Wird so zum Beispiel der aktuell Anfragende Nutzer in den Query mit einbezogen, kann nicht auf den Cache eines vorhergehenden Queries eines anderen Nutzers zurückgegriffen werden.[^spam]

Gleichermaßen führt die bei Dokument-basierten Systemen notwendige Demoralisierung der Daten zu einer starken Redundanz der gespeicherten Informationen und dem dadurch mögliche Integritätsverlust. In einer normalisierten Datenbank wird die Integrität der gespeicherten Daten durch die fehlende Redundanz garantiert. Um die Integrität in einem denomalisierten System aufrecht zu erhalten, ist es Notwendig viele Dokumente zu aktualisieren. Bei großen strukturell geteilten Systemen geschieht dies oft erst Zeitversetzt, was teilweise auch für den Nutzer merklich ist. So kann es in großen sozialen Netzwerken oftmals vorkommen, dass an manchen stellen noch ein veraltetes Profilbild eines Nutzers angezeigt wird, wenn dieser es vor kurzer Zeit erneuert hat.

Um die Güte beider Systeme zu vereinen wird für Lawly auf PostgreSQL in einer aktuellen Version gesetzt. Obwohl PostgreSQL zur Grundlage eine traditionelle an Tabellen orientierte Struktur nutzt, bringt es neue Dokument-ähnliche-Datentypen mit sich. Diese eröffnen die Möglichkeit in einzelnen Spalten mehr als nur einen Wert zu speichern oder auch komplexere Dokumente abzulegen. Dabei ist es weiterhin möglich diese Dokumente oder in ihnen verschachtelte Einträge in SQL-Queries und -Indices zu nutzen. Dadurch kann für sich oft ändernde Informationen eine normalisierte Struktur, allerdings für langfristig statische aber oft abgefragte Beziehungen, eine denormalisierte Struktur eingesetzt werden.

[^spam]: Die geschilderte Erfahrung brachte die Entwicklung der Kurs-Suchfunktion für die *Study Planning Machine* für den Cognitive Science Studiengang an der Universiät Osnabrück. Dabei galt es, eine in Echtzeit Anfragen beantwortende Lösung zu entwickeln, welche innerhalb der Suchergebnisse bereits die Verbindung des suchenden Nutzers zu dem gelieferten Kurs darstellt -- also ob der Nutzer diesen Kurs zum Beispiel bereits in seine Sammlung aufgenommen hat. Die in diesem Fall verwendete Datenbankstruktur ist streng normalisiert: $Studienordnungen \leftrightarrow Module \leftrightarrow Kurse \leftrightarrow Lehrende \leftrightarrow Studenten$. Um Caching Nutzen zu können, wurde die Verbindung zum anfragenden Studenten endgültig Clientseitig gelöst. Quelltext unter [github.com/ahoereth/spam/](https://github.com/ahoereth/spam/).
