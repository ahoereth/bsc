## Server {#sec:server-theory}
Im Folgenden wird zu Beginn auf die Entscheidung eingegangen, Server und Client strukturell vollständig voneinander zu trennen. In den Abschnitten @sec:api und @sec:database wird dann, respektive, die eingesetzte Server- und Datenbank-Architektur diskutiert.

Aufgrund der Anforderung einer in Zukunft flexibel auf weitere Plattformen erweiterbaren Applikation kommt nur eine klare Trennung von Server und Client in Frage. Bei der Entwicklung eines reinen \ac{API} Servers ist es wichtig, dass dieser Daten in einer von ihrer für den Endnutzer endgültigen Repräsentation unabhängigen, leicht zu verarbeiteten Form zur Verfügung stellt. Allerdings gilt es dabei gleichermaßen, die bereitgestellten Schnittstellen nicht zu abstrakt zu gestalten, sondern Daten sinnvoll zu bündeln, um vermeidbare Anfragen durch Client-Applikationen vorzubeugen.

Aus dieser Unabhängigkeit ergibt sich die Möglichkeit serverseitige Logik, wie beispielsweise Datenbankanfragen und Nutzer-Authentifizierung, wiederzuverwenden. Im besten Fall wird für eine bestimmte Aufgabe, wie etwa die Registrierung eines neuen Nutzers, die serverseitige Logik nur ein einziges mal implementiert, so dass beliebige darauf angewiesene clientseitige Applikationen in Zukunft nur noch eine einmalig standardisierte Anfrage an den Server stellen müssen. Dadurch ist es nicht Notwendig bei der Erstellung zusätzlicher Apps mit ähnlichem Funktionsumfang wie dem initialen Produkt Änderungen am Server vorzunehmen. Auch bei der Implementierung neuer Funktionalität auf allen Plattformen muss so nur einmalig eine neue \ac{API}-Schnittstelle hinzugefügt werden.

In Bezug auf eine Webapplikation ergibt sich zusätzlich der Vorteil, dass die \ac{API} und die eigentliche für den Nutzer zur Verfügung gestellte Applikation auf unabhängigen Servern bereitgestellt werden können. So ist es möglich, flexibel auf Lastspitzen durch Skalierung der jeweils stärker betroffenen Hardware zu reagieren.



### Application Programming Interface {#sec:api}
Grundlegend gibt es aktuell zwei für den Einsatz als \acp{API} interessante Konzepte:

  1. Eine \ac{HTTP}-\ac{REST}-\ac{API}, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Die zentrale Unterscheidung zwischen den beiden ist das `pull/push`-Prinzip. Bei einer \ac{REST}-API werden mithilfe von sogenannten HTTP-Verben einzelne Anfragen an den Server gestellt, worauf hin eine Antwort erwartet wird. Diese Anfragen sind im besten Fall für den Server komplett voneinander unabhängig und nicht auf einen gewissen serverseitig vorgehaltenen Zustand angewiesen. Bildlich werden per Anfrage also Daten vom Server *gepulled*. Ein Übertragen von Daten an den Client ist hierbei immer nur als Antwort auf eine von diesem initiierte Anfrage möglich.

Im Gegensatz dazu muss sich bei der Verwendung von WebSockets der Client nur für einen initialen Verbindungsaufbau beim Server anmelden. Ab diesem Zeitpunkt wird eine Verbindung zwischen Server und Client aufrechterhalten, an die beide, wann immer aktualisierte Informationen vorhanden sind, Daten *pushen* und auf erhaltene Daten reagieren können. Hierbei wird nicht mehr von einzelnen Anfragen, sondern von Ereignissen, auf welche die Teilnehmer reagieren, gesprochen.[^longpolling]

Für das initiale Produkt wird auf eine reine \ac{HTTP}-Schnittstellen gesetzt. Im geplanten Funktionsumfang ist, initial, kein Austausch von Informationen in Echtzeit nach dem push Prinzip notwendig. Der Client arbeitet nur mit konkret von ihm angefragten Daten, wie zum Beispiel der Gesetzesübersicht und den Normen eines bestimmten Gesetzes. Zwar ist es interessant, Interaktionen, wie zum Beispiel das Vormerken von Gesetzen, mithilfe von einer durch WebScokets realisierten Echtzeitverbindung zwischen mehreren aktiven Geräten des gleichen Nutzers per push zu synchronisieren, allerdings mit einem großen Mehraufwand verbunden, so dass es erst zu einem späteren Zeitpunkt umgesetzt werden soll.

[^longpolling]: Für bessere Kompatibilität mit älteren Browsern ist auch möglich, sogenanntes *long-polling* einzusetzen. Hierbei erfolgt der Verbindungsaufbau wie bei einer \ac{REST}-API, allerdings wird die ankommende Anfrage nicht sofort beantwortet. Der Server hält die Verbindung offen und antwortet erst zu einem späteren Zeitpunkt auf die Anfrage. Sobald der Client eine Antwort erhält sendet er unmittelbar eine erneute Anfrage um dem Server wieder die Möglichkeit zu eröffnen ihm gewissermaßen ungefragt Daten zu übermitteln.



#### HTTP & REST
Ein wichtiger Punkt, welcher beim Einsatz von WebSockets für einen stark erhöhten Implementierungsaufwand sorgen würde, ist, dass ein WebSocket-Server niemals zustandslos sein kann. Er muss nach einer initialen Anfrage eines Clients die Verbindung zu diesem aufrecht erhalten um im weiteren Verlauf mit ihm kommunizieren zu können. Im Gegensatz dazu kann bei einer \ac{HTTP}-\ac{API} der Server so implementiert werden, dass er keinerlei Informationen über vorhergehende Anfragen vorhält, wodurch die Infrastruktur, wenn notwendig, horizontal skaliert (*horizontal scaling*) werden kann.

Horizontal and vertical scaling
:  Horizontale und vertikale Skalierung
:  Bei der horizontalen Skalierung werden, je nach Notwendigkeit, unterschiedlich viele Maschinen in einem Pool zusammengeschaltet. Ein zentraler Schnittpunkt, der sogenannte *Load-Balancer*, verteilt in diesem Fall die Anfragen auf die einzelnen Server für eine gleichmäßige Lastverteilung. Im Gegensatz zur horizontalen steht die vertikale Skalierung: Ein einzelner Server wird, um mit erhöhter Last umgehen zu können, mit leistungsfähigeren Komponenten, also mehr Arbeitsspeicher, besserem Prozessor uws., ausgestattet. [@Vaquero2011]

Um dies zu ermöglichen, ist es notwendig, dass jede Anfrage alle für ihre Beantwortung notwendigen Informationen mitliefert -- zum Beispiel auch relevante Authentifizierungsinformationen (siehe hierzu den dritte Teil von Abschnitt @sec:security, Sicherheit). Im Fall von WebSockets ist es notwendig, dass Verbindungen entweder zentral, also für alle im Cluster befindlichen Server erreichbar, vorgehalten werden oder aber dafür gesorgt wird, dass ein Client sich immer nur mit dem Server, mit welchem er initial von dem das Cluster verwaltende Load-Balancer verbunden wurde, kommunizieren kann.

Durch die Orientierung an einer *RESTful Resource-Oriented Architecture*, ergibt sich die Entwicklung einer intuitiv verständlichen \ac{API}. Anfragen werden so anhand ihrer URL an eine bestimmte Ressource gerichtet und mithilfe der \ac{HTTP}-Methode (*GET*, *POST*, *PUT* etc.) die gewünschte Aktion spezifiziert. Daraus ergibt sich, dass aus der ersten Zeile der \ac{HTTP}-Anfrage bereits hervorgeht, was der Client zu erreichen gedenkt. Eine solche erste Zeile sieht in der entwickelten Anwendung zum Beispiel wie folgt aus: `GET /laws/BGB HTTP/1.1` -- der Client erwartet als Antwort ein Gesetz, welches durch *BGB* eindeutig identifizierbar ist. [@Tilkov2015] <!--, s. 13 -->

Um auch geschützte Ressourcen verfügbar zu machen bietet \ac{HTTP} und das in der entwickelten Applikation eingesetzte, nach initialer Verbindung gleich zu verwendende, \ac{HTTPS} den sogenannten `Authorization`-Header. Über diesen wird der alle für die Autorisation notwendigen Informationen enthaltende Autorisierungstokens (siehe Abschnitt @sec:security) bei jeder Anfrage nach der initialen Anmeldung eines Nutzers übertragen.



#### Express
Eine zentrale und gleichermaßen für viele Neulinge verwirrende Eigenschaft von JavaScript ist der Event Loop. Bei beispielsweise in PHP geschriebenen Servern wird bei jeder eintreffenden Netzwerkanfrage eine Instanz gestartet in welcher der komplette Quelltext ausgeführt wird. Im Falle eines Node.js-Servers hingegen wird die Applikation initial einmalig gestartet und lauscht von nun an auf auftretende Ereignisse. Ein solches Event ist im Fall eines \ac{REST}-\ac{API}-Servers zum Beispiel das Eintreffen einer Netzwerkanfrage. Wie in Listing @lst:server:simple dargestellt, lauscht der Server auf ein solches `request`-Event und behandelt es mithilfe einer vordefinierten Funktion, eines sogenannten Handlers. Solche Handler sind in JavaScript *Callbacks* für asynchrone Funktionsaufrufe. Sie werden also bei Fertigstellung der asynchron ausgeführten Operation mit dem Ergebnis oder eventuellen Fehlern aufgerufen.

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

Um leichter dem \ac{REST}-Prinzip folgen zu können wird bei der Applikation auf das Express-Framework gesetzt. Wie in Listing @lst:server:express sichtbar, filtert es die eintreffenden HTTP-Anfragen und verteilt sie auf klar definierte Handler für einzelne HTTP-Verben und Pfade.

Listing: Node.js Server mit Express

~~~{#lst:server:express}
import express from 'express';
const app = express();
app.get('/obj', (request, response) => {
  response.end(`GET at 2!`);
});
app.put('/obj/:id', (request, response) => {
  response.end(`PUT at /obj/${request.params.id}!`);
});
app.listen(8080, () => {
  console.log('Listening on port 8080');
});
~~~



### Datenbank {#sec:database}
Im folgenden wird knapp auf die zentrale Unterscheidung zwischen normalisierten SQL- und denomalisierten dokumentorientierten Datenbanken eingegangen -- breiteres Vorwissen wird hier allerdings vorausgesetzt. Primär wird der durch neuere Versionen der Open Source Datenbank PostgreSQL ermöglichte Hybrid-Ansatz erläutert.

Als Datenbank kommen grundlegend zwei verschiedene Ansätze in Frage: Traditionellere SQL- und in den letzten Jahren aufgekommene NoSQL- bzw. Dokument-Datenbanken. Besonders für schnell wachsende und im großen Stil Daten anhäufende Anwendungen haben sich die NoSQL-Datenbanken bewiesen, müssen sich aber in ihrer Ausdauer noch im Vergleich zu den jahrzehntelang gehärteten SQL-Systemen beweisen. Sie basieren auf der Grundidee einzelne, nicht direkt voneinander abhängige Dokumente zu speichern. Ähnlich wie bei dem verfolgten Ansatz eines zustandslosen API-Servers, beschrieben in Abschnitt @sec:server-theory, ist es so möglich die Datenbank horizontal durch hinzufügen neuer Instanzen zu skalieren.

Ein zentraler Aspekt von SQL-Datenbanken ist im Kontrast dazu eine *normalisierte* Struktur: Bei strenger Einhaltung werden dabei Informationen niemals redundant abgespeichert. In dem Fall, dass ein Nutzer ein bestimmtes Gesetz vorgemerkt hat, ergeben sich so zwei gegensätzliche Herangehensweisen: In einer dokumentorientierten Datenbank werden der Titel dieses Gesetzes direkt in dem einem Nutzer zugeordneten Dokument abgespeichert, so dass bei Zugriff auf dieses direkt alle vom jeweiligen Nutzer vorgemerkten Gesetze verfügbar sind. In einer normalisierten SQL-Datenbank hingegen würde stattdessen ein neuer Eintrag erstellt werden, welcher auf die eindeutigen Identifikationsnummern des Nutzers und des Gesetzes verweist. Beim Abrufen der Nutzerinformation würde dann der Nutzer über solche *one-to-many* Beziehungen mit den vorgemerkten Gesetzen in Verbindung gebracht werden.

Ein Nachteil starker Normalisierung ist allerdings eine steigende Komplexität des Systems und der hohe Ressourcenanspruch. Bei komplexen Systemen sind mehrschichtige `Joins`, also das auflösen von normalisierten Beziehungen, rechenintensiv. Die Lösung hiervon besteht meist in intensivem Caching der Ergebnisse, was allerdings nur bei oft wiederkehrenden Anfragen hilfreich ist. Wird so zum Beispiel der aktuell Anfragende Nutzer in den Query mit einbezogen, kann nicht auf den Cache eines vorhergehenden Queries eines anderen Nutzers zurückgegriffen werden.[^spam]

[^spam]: Die geschilderte Erfahrung brachte die Entwicklung der Kurs-Suchfunktion für die [*Study Planning Machine*](https://cogsci.uos.de/~SPAM) für den Cognitive Science Studiengang an der Universität Osnabrück. Dabei galt es, eine in Echtzeit Anfragen beantwortende Lösung zu entwickeln, welche innerhalb der Suchergebnisse bereits die Verbindung des suchenden Nutzers zu dem gelieferten Kurs darstellt -- also zum Beispiel ob der anfragende Nutzer diesen Kurs bereits in seine Sammlung aufgenommen hat. Die in diesem Fall verwendete Datenbankstruktur ist streng normalisiert: $Studienordnungen \leftrightarrow Module \leftrightarrow Kurse \leftrightarrow Lehrende \leftrightarrow Studenten$. Um verstärkt von Caching Gebrauch machen zu können, wurde die Verbindung zum anfragenden Studenten endgültig Clientseitig gelöst. Applikation auf [cogsci.uos.de/~SPAM](https://cogsci.uos.de/~SPAM), Quelltext unter [github.com/ahoereth/spam](https://github.com/ahoereth/spam/).

Gleichermaßen führt die bei dokumentorientierten Systemen notwendige Denormalisierung der Daten zu einer starken Redundanz der gespeicherten Informationen und dadurch zu der Gefahr eines Integritätsverlust. In einer normalisierten Datenbank wird die Integrität der gespeicherten Daten durch die fehlende Redundanz garantiert. Um die Integrität in einem denormalisierten System aufrecht zu erhalten, ist es Notwendig die von einer geänderten Information abhängigen Dokumente alle möglichst gleichzeitig zu aktualisieren. Bei großen strukturell geteilten Systemen geschieht dies oft erst zeitversetzt, was teilweise auch für den Nutzer merklich ist. So kann es in großen sozialen Netzwerken oftmals vorkommen, dass an manchen stellen noch ein veraltetes Profilbild eines Nutzers angezeigt wird, wenn dieser es vor kurzer Zeit erneuert hat.

Um die Güte beider Systeme zu vereinen wird für Lawly auf das SQL-Datenbanksystem PostgreSQL gesetzt. Obwohl PostgreSQL zur Grundlage eine traditionelle an Tabellen orientierte Struktur nutzt, bringt es in neueren Versionen aus dokumentorientierten Systemen bekannte JSON-Datentypen mit. Diese eröffnen die Möglichkeit in einzelnen Spalten nicht nur mehr als einen einzelnen Wert zu speichern, sondern auch komplexere Dokumentstrukturen abzulegen. Dabei ist es weiterhin möglich diese Dokumente oder in ihnen verschachtelte individuelle Einträge in SQL-Anfragen und -Indices zu nutzen. Dadurch kann für sich oft ändernde Informationen eine normalisierte Struktur, allerdings für langfristig statische aber oft abgefragte Beziehungen, eine denormalisierte Struktur eingesetzt werden.
