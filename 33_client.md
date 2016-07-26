## Client
\label{sec:client}

### Grundlagen einer modernen Web-Applikationen
\label{sec:webapps}

Bei traditionellen Webseiten und auch Webapplikationen führt bei einer \ac{SPA} nicht jede Interaktion zu einem vollständigen sogenannten Client-Server-Round-Trip. Bei einem solchen wird traditionell durch jede Interaktion eine Anfrage an den Server gestellt welcher auf Grundlage dieser eine neue Seite generiert und an den Client schickt, welcher die vorherige Seite dann durch die neue ersetzt.

Durch die zentrale Anforderung an die Client-Web-Applikation, sich ähnlich nativer Software zu verhalten ist die Entwicklung einer \ac{SPA} unabdingbar. Im Gegensatz zu den zuvor erläuterten Konzept eines vollständigen round-trips wird hierbei ein Großteil der Berechnungen auf Client-Seite ausgeführt. Beim initialen Laden der Seite werden alle notwendigen Layout- und Script-Dateien übertragen, so dass zum reagieren auf weitere Interaktionen nur semantische aber keine strukturellen Informationen mehr vom Server angefordert werden müssen. Dieser Ansatz liegt sehr nah an dem vorherrschenden Betriebskonzept von Mobilapplikationen: Nach der initialen Installation der App werden nur noch aktuelle semantische Informationen, zum Beispiel Nachrichten oder Videos, vom Server bereitgestellt.

Der von uns verfolgte Ansatz geht einen Schritt weiter: Nicht nur werden strukturelle Informationen lokal nach dem initialen Laden vorgehalten, sondern auch Ergebnisse von weiteren Anfragen an den Server werden gespeichert (Stichwort: caching) um sie, in dem Fall, dass sie noch einmal relevant werden, nicht erneut ausführen zu müssen. Zum Beispiel werden so alle Einträge für die Gesetzesübersicht sofort zu Beginn an die Client-Instanz übertrage, um sie nicht bei jedem Aufruf der Übersichtsseite erneut laden zu müssen.

Bei jeder Interaktion wird so clientseitig getestet ob die notwendigen Daten bereits lokal zur Verfügung stehen. Wenn dies der Fall ist, kann die neue Seite sofort angezeigt werden ohne unnötige Ladezeit. Dies führt zu einer besseren Nutzererfahrung weil Seitenwechsel so im besten Fall nicht mehr durch mögliche Konnektivitätseinschränkungen beeinträchtigt werden. Um dieses Nutzungsergebnis weiter zu verbessern ergibt sich hier auch die Möglichkeit potentiell relevante Daten vorzuladen. So hat ein Nutzer möglicherweise favorisierte Gesetze die er voraussichtlich regelmäßig aufrufen wird -- diese können nun unmittelbar zur Verfügung gestellt werden.

Der dritte Schritt ist es, nicht nur bereits alle voraussichtlich relevanten Daten zusammen mit jedem initialen Aufruf der Applikation zur Verfügung zu stellen, sondern über mehrere Aufrufe hinweg zu speichern und somit die Applikation auch ohne Internetverbindung verfügbar zu machen. Hieraus ergeben sich zwei neue Problematiken: Einerseits müssen nun vorgehaltene Daten müssen auf ihre Aktualität getestet und eventuell aktualisiert werden. Anderseits müssen, sobald eine Internetverbindung zum initialen Laden der Applikation nicht mehr relevant ist, auch zwingend Interaktionen welche nicht nur für die aktuelle Instanz relevant sind, lokal gespeichert und beim wieder erlangen einer Verbindung zum Server mit diesem abgeglichen werden.

Beim Aufbau einer diesen Paradigmen folgenden Applikation ist es von Interesse einem "offline-first" Ansatz zu folgen. Ähnlich wie es bereits Standard ist sich beim Webdesign an "mobile-first" zu orientieren, betrachtet man quasi das schwächste beziehungsweise eingeschränkteste Glied der Kette als den Standard: Im optimalen Fall ist alles, was auf diesem Gerät nicht funktioniert, optional. Bei "mobile-first" ist so das Smartphone-Display meist der Maßstab für den gestaltet wird. An größere Displays passt sich das Layout dann möglichst durch relativ definierte Größen von Schriften und Containern und dynamisches fließen der Elemente, so dass je nach verfügbarer Fläche mehr oder weniger Container nebeneinander angezeigt werden, an. "offline-first" nimmt nun also das fehlen einer Internetverbindung als den Standard an. Alle Reaktionen auf Nutzeraktionen werden lokal berechnet und durchgeführt. Erst in einem zweiten Schritt werden diese dann, sobald eine Internetverbindung verfügbar ist, mit dem Server abgeglichen. Hierbei gilt, dass der Server immer "Recht" hat: Falls der Server als Ergebnis einer Aktion etwas anderes präsentiert als der Client, ersetzt das Ergebnis des Servers nachträglich das des Clients. Dies ist relevant da die Integrität des auf Clientseite ausgeführten Codes nicht garantiert werden kann. Somit kann es passieren, dass die Client-Applikation eine bestimmte Interaktion wie zum Beispiel das Löschen eines (wie auch immer gearteten) Eintrages genehmigt und lokal durchführt, der Server aber anderer Auffassung ist und die Löschung auf seiner Seite nicht durchführt und damit auch dem Client den Auftrag gibt sie rückgängig zu machen.



### Web-Browser als Software Plattform
\label{sec:browserSE}


### Grundlegende Architektur


* Redux
* Zentraler Store
* Linearer Datenstrom

#### Actions

#### Reducers

#### Store

### React

* Komponenten Hierarchie
* Virtual DOM

#### Container

* Interaktion mit Redux

#### Components

* *Dumme* Komponenten
* Weiß nichts von Redux --> leicht zu testen
* Zum großen Teil komplett state less -> leicht zu testen


\pagebreak

### Design

* Material Design
