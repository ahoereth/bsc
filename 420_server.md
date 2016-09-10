## Server {#sec:server-architecture}
Durch die Entscheidung den Server als reine \ac{API} umzusetzen, fällt dieser denkbar einfach aus. Im Fokus der folgenden Beschreibung liegen daher die definierte \ac{REST}-Schnittstellen und das standardisierte Antwortformat. Zusätzlich muss der Server effizient mit Authentifizierung von Anfragen umgehen können und durch starke Modularisierung für eine zukünftige Erweiterung gerüstet sein. Um eine einfachere Modularisierung zu ermöglichen wird, wie zuvor erläutert, das Express-Framework eingesetzt.



### Authentifizierung {#sec:server:middleware}
Die Authentifizierung von Anfragen findet mithilfe einer *Middleware* statt.[^code:authentication] Middlewares sind Funktionen welche von Express zwischen das Eingehen einer Anfrage und ihrer Bearbeitung durch einen bestimmten Handler geschaltet werden und die enthaltenen Request- und Response-Objekte erweitern können. Die implementierte Authentifizierungs-Middleware überprüft, ob der `Authorization`-Header gesetzt ist. Wenn dies gilt, wird aus diesem der \ac{JWT} extrahiert und, mithilfe der Open Source Bibliothek `node-jsonwebtokens` auf Validität überprüft. Zusätzlich wird überprüft ob der Token nur noch weniger als 24 Stunden gültig ist und gegebenenfalls ein neuer ausgestellt. Die im \ac{JWT} enthaltenen Nutzerdaten und der eventuelle neue Token werden dem Request-Objekt hinzugefügt und dieses an nachfolgende Middlewares bzw. den Route-Handler weitergereicht. Vergleiche in Bezug hierauf auch Abschnitt @sec:security.

[^code:authentication]: [lawly_api: /server/config/authentication.js#L144ff](https://github.com/ahoereth/lawly_api/blob/master/server/config/authentication.js#L144-L190)



### HTTP-Endpunkte
Um große Applikationen mit vielen HTTP-Endpunkten besser Unterteilen zu können bietet Express die Möglichkeit, bestimmte \ac{URL}-Pfade in *Routern* zu bündeln. Dabei wird ein solcher Router angesprochen, sobald auf dem ihm zugeordneten beziehungsweise einem diesem untergeordneten Pfad eine Anfrage eintrifft. Der Router kümmert sich dann um die weitere Verteilung an ihm zugeordnete Handler.

Obwohl die aktuelle \ac{API} nur einen sehr überschaubaren Umfang hat, wird bereits vorausschauend auf die Unterteilung in zwei Router gesetzt: Respektive sind diese jeweils für Anfragen an die Pfade `/laws` und `/users` zuständig.[^code:router] Wie in Abschnitt @sec:client-theory angekündigt, ergeben sich die Aufgaben dieser Router bereits selbsterklärend aus den ihnen zugeordneten HTTP-Pfaden.

Unter `/laws` finden sich lediglich zwei `GET` Schnittstellen, da kein Nutzer der Applikation zum Eintragen oder ändern von Gesetzen bemächtigt ist und zu diesem Zeitpunkt kein die API nutzendes administratives Interface existiert.[^code:laws] Direkte `GET`-Anfragen an den Wurzel-Pfad werden mit der Übersicht über alle verfügbaren Gesetze beantwortet. Um das zur Verfügung gestellte Paket dabei möglichst klein zu halten, ist in der Übersicht jedes Gesetz nur mit seinem eindeutigen Kürzel (z.B. *BGB*) und seinem Titel (z.B. *Bürgerliches Gesetzbuch*) vertreten. Mithilfe des Query-Parameters `search` ist es hier zusätzlich möglich das Ergebnis durch eine Volltextsuche zu filtern.

Für detailliertere Informationen über ein Gesetz steht der Endpunkt `/laws/:groupkey` zur Verfügung, dabei wird als Wert für den `groupkey` Parameter das Kürzel eines Gesetzes bezeichnet -- die Bezeichnung *groupkey* resultiert daraus, dass das Kürzel eines Gesetzes in der Datenbank den eindeutigen Schlüssel für eine Sammlung von Normen beschreibt.

Unter `/users` hingegen werden nicht nur lesende `GET`-, sondern auch schreibende `PUT`- und `POST`-Anfragen bereitgestellt.[^code:users] So dient `POST /users` zum Beispiel der Erstellung eines neuen oder Authentifizierung eines bestehenden Benutzeraccounts.^[Hierbei handelt es sich um den einzigen Endpunkt, an dem das Nutzerpasswort erwartet wird. Alle anderen Endpunkte, wenn in ihrem Zugriff beschränkt, benötigen für die Autorisierung einen hierüber ausgestellten oder von der in Abschnitt @sec:server:middleware beschrieben Middleware erneuerten \ac{JWT}.] Die zweite zentrale aktuell bereitgestellte Route ist etwas verschachtelter: `PUT /:email/laws/:groupkey/:enu?`. Hierüber können Nutzer per `PUT` Anfrage, also einer Anfrage um einen bestehenden Datenbestand zu verändern, Gesetze und Normen in ihre Sammlung aufnehmen. Der `:email` Parameter spezifiziert dabei, wessen Sammlung verändert werden soll -- aktuell gilt es, dass Nutzer nur zur Veränderung ihrer eigenen Sammlung autorisiert sind (die Adresse wird also mit dem \ac{JWT} abgeglichen), langfristig ist es aber denkbar, dass auch Gruppen gemeinsame Sammlungen anlegen und bearbeiten können. `:groupkey` spezifiziert das Kürzel des Gesetzes und `:enu` die eindeutige Enumeration einer Norm innerhalb des Gesetzes -- falls `:enu` nicht angegeben ist, wird die Wurzel-Norm zugegriffen. Innerhalb des Anfragen-Körpers wird hierbei nun ein JSON-Objekt mit dem Feld `starred` erwartet, dessen Boole'scher Wert angibt, ob die spezifizierte Norm gemerkt oder vergessen werden soll.

[^code:router]: [lawly_api: /server/routes/index.js](https://github.com/ahoereth/lawly_api/blob/master/server/routes/v0/index.js)

[^code:laws]: [lawly_api: /server/routes/laws.js](https://github.com/ahoereth/lawly_api/blob/master/server/routes/v0/laws.js)

[^code:users]: [lawly_api: /server/routes/users.js](https://github.com/ahoereth/lawly_api/blob/master/server/routes/v0/users.js)



### Antworten
Um Antworten gleichmäßig zu gestalten wurde ein Klasse implementiert, welche eine Response-Objekt erwartet (welches jedem Route-Handler übergeben wird) und Methoden anbietet dieses einheitlich zu verarbeiten.[^code:reply] Grundlegend gilt hierbei, dass jede Methode der Klasse für einen bestimmten HTTP-Statuscode zuständig ist und es damit vereinfacht, diesen korrekt zu setzen. Zusätzlich werden die an eine Antwort angehängten Daten dabei in ein einheitliches JSON-Objekt verpackt, welches zusätzliche Informationen wie den Erfolg oder Misserfolg der Operation und einen eventuell durch die zuvor beschriebe Middleware generierten neuen Authentifizierungstoken beinhaltet. Außerdem werden ein paar Unregelmäßigkeiten in der Handhabung von Antworten ausgeglichen. Ein Beispiel hierfür ist der Statuscode `204 No Content`, bei welchem laut Standard generell keine Daten enthalten sein dürfen [@Fielding2014] und dessen Header von älteren Versionen des Internet Explorer komplett ignoriert wird -- um dies zu vermeiden und auch bei `No Content` einen erneuerten Token senden zu können, werden solche Antworten auf Status 200 umgeschrieben.

[^code:reply]: [lawly_api: /server/helpers/reply.js](https://github.com/ahoereth/lawly_api/blob/master/server/helpers/reply.js)
