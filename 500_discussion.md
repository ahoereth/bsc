# Diskussion {#sec:discussion}
Zum Zeitpunkt des Verfassens sind beide Endpunkte, Client und Server, noch Zugriffsbeschränkt. Der API-Server erlaubt so aktuell nur Anfragen von der auf der offiziellen Domain betriebenen Webapplikation und die Webapplikation benötigt eine zusätzliche Authentifizierung. Dies soll möglichst bald, soweit das weitere vorgehen geklärt ist und insbesondere eine Landingpage als Einführung für neue Nutzer erstellt wurde, geändert werden. Gleichermaßen ist es für diesen Zeitpunkt auch geplant den Code vollständig unter eine Open Source Lizenz zu veröffentlichen -- die Details dies bezüglich müssen noch entschieden werden.



## Rückblick {#sec:discussion:backward}
Rückblickend wurden die ursprünglich für diese Arbeit gesetzten Ziele erreicht. Die Webapplikation ist ähnlich einer nativen Applikation auf mobilen Endgeräten auch ohne Internetverbindung einsetzbar und zeigt sich erstaunlich performant. 

Der Weg dahin war allerdings von einigen Komplikationen geprägt, insbesondere da sehr vielversprechende Technologien wie beispielsweise Service Worker bisher nicht von allen Browserherstellern umgesetzt wurden. Zusätzlich hat sich auch die Wahl des zuvor noch nicht verwendeten React-Ecosystem als sehr arbeitsintensiv erwiesen: anders als bei beispielsweise Angular.js (mit welchem Vorerfahrung besteht), ist React nicht "*batteries-included*". Das bedeutet, dass es nicht von Hause aus den Großteil der für die Entwicklung und den Produktiveinsatz benötigte Werkzeuge mitbringt. Alleine die Konfiguration des für das produktive Arbeiten notwendige Webpack hätte mehrere Seiten dieser Arbeit füllen können.

Ähnliches gilt für die neuartige clientseitige Applikationsarchitektur. Die objektorientierte Programmierung und den Einsatz des \ac{MVC}-Konzeptes gewöhnt, ist der Einstieg in den eingesetzten uni-direktionalen Datenfluss aufwendig. Allerdings hat sich die Entscheidung für den gewählten Entwicklungsstack als richtig erwiesen: die aufgeführten Punkte wie sehr viel bessere Verständlichkeit der Architektur und besser vorhersehbare Zustandsänderungen haben den Entwicklungsprozess nach einer zu Beginn steilen Lernkurve sehr angenehm gestaltet.

Auf das gesamte Projekt bezogen ist in den letzten Wochen dieser Arbeit ein österreichischer Spieler aufgetreten welcher sehr vieles richtig macht. *openlaws.com* setzt ähnlich wie Lawly darauf Open Data im juristischen Bereich aufzubereiten und zu Verknüpfen. Mit einem scheinbar über zweijährigen Entwicklungsvorsprung konnte die Plattform außerdem bereits Fördergelder der Europäischen Union verbuchen. Obwohl dies initial frustrierend war, bestätigt es auch die Notwendigkeit einer solchen Dienstleistung. Zusätzlich sind bei *openlaws.com* zwar Open Data und Open Source scheinbar für Marketingzwecke beliebte Schlagwörter, allerdings folgt die Plattform selber diesen Prinzipien nicht. Weder ist ihr Quelltext frei verfügbar, noch stellt sie eine Schnittstelle für die von ihr vermarkteten aufbereiteten Daten bereit. Beides Dinge, welche für Lawly zum Konzept gehören.



## Ausblick {#sec:discussion:forward}
Obwohl der Rückblick etwas dämpft, ist der Ausblick positiv. So ermöglichen die technologischen Entscheidungen durch das heranreifen von React Native langfristige Entwicklungschancen -- um den Markt zu erreichen ist so beispielsweise die Entwicklung einer nativen iPad-Applikation mittelfristig denkbar.

In Bezug auf die realisierte Webapplikation gilt es vorerst die Performance weiter zu optimieren. Dazu gehört insbesondere auch die *gefühlte Performance*, welche die geschickte Verwendung von Animationen erfordert -- eine Thematik welche im bisherigen Entwicklungsverlauf noch nicht angegangen wurde. Außerdem gilt \ac{SSR} auch in Produktion einzusetzen und die Seite damit für Suchmaschinen zu optimieren. Dazu gehört auch der Gedanke mithilfe des gleichen \ac{SSR}-Codes durch die Generierung von \ac{AMP} einen Rankingvorteil bei Google zu erreichen. Google bevorzugt offiziell Seiten welche diesen von ihnen offen entwickelten Standard einsetzen.[^makethewebgreatagain]

[^makethewebgreatagain]: [googleblog.blogspot.de/2016/02/amping-up-in-mobile-search.html](https://googleblog.blogspot.de/2016/02/amping-up-in-mobile-search.html), abgerufen 08/2016

Außerdem erfordert auch die Ansicht für die eigentlichen Gesetzestexte noch weitere Aufmerksamkeit, da sie die Seite ist, auf der Nutzer voraussichtlich die meiste Zeit verbringen. Von verbreiteten Anbietern für Lesedienste wie beispielsweise Pocket[^pocket] sind so zum Beispiel die Möglichkeiten zur Anpassung von Schriftart und -größe oder auch der Einsatz von mehrspaltigen Layouts bekannt.

[^pocket]: [getpocket.com](https://getpocket.com)

Zu guter Letzt ist auch die Finanzierung nicht zu vernachlässigen. Kurzfristig gilt es zumindest die Kosten für den Betrieb zu decken, langfristig auch die Weiterentwicklung zu finanzieren. Vorläufig soll, auf Grundlage der in Abschnitt @sec:lawly vorgestellten Ideale, eine nicht kommerzielle Finanzierung im Vordergrund stehen. Dies wäre zum Beispiel durch eine Plattform wie Patreon[^buymeacookie] denkbar, bei welcher regelmäßige kleine Spenden zur langfristigen Finanzierung von Projekten im Vordergrund stehen. Außerdem steht der Prototypefund[^fundmebig] aus. Dieser ist eine Initiative um deutsche Open Source Projekte von öffentlichem Interesse voranzutreiben und dafür ein nicht geringes sechsmonatiges Einkommen für einen einzelnen Entwickler in Aussicht stellt. Die Bewerbung für letzteres ist wohl der erste anstehende Schritt.

[^buymeacookie]: [patreon.com](https://www.patreon.com/)

[^fundmebig]: [prototypefund.de](https://prototypefund.de)
