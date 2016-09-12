# Diskussion {#sec:discussion}
Zum Zeitpunkt des Abschlusses der vorliegend Arbeit sind beide Endpunkte, Client und Server, noch zugriffsbeschränkt. Der API-Server erlaubt so aktuell nur Anfragen von der auf der offiziellen Domain betriebenen Webapplikation und die Webapplikation benötigt eine zusätzliche Authentifizierung. Dies soll möglichst bald, soweit das weitere Vorgehen geklärt ist und insbesondere eine Landingpage als Einführung für neue Nutzer erstellt wurde, geändert werden. Gleichermaßen ist es für diesen Zeitpunkt auch geplant den Code vollständig unter einer Open Source Lizenz zu veröffentlichen -- die Details dies bezüglich müssen noch entschieden werden.



## Rückblick {#sec:discussion:backward}
Rückblickend wurden die ursprünglich für diese Arbeit gesetzten Ziele erreicht. Die geplanten Ansichten und Funktionalitäten wurden umgesetzt, die Webapplikation zeigt einer nativen Applikation ähnliche Performance und ist für den mobilen offline Einsatz gerüstet. Außerdem ist sie für den Produktiveinsatz vorbereitet und kann, außer einiger letzter Nachbesserungen, aus Knopfdruck freigeschaltet werden.

Der Weg dahin war allerdings von einigen Komplikationen geprägt, insbesondere, da einige sehr vielversprechende Technologien wie beispielsweise Service Worker bisher nicht von allen Browserherstellern umgesetzt wurden. Zusätzlich hat sich auch die Wahl des zuvor noch nicht verwendeten React-Ecosystem als sehr arbeitsintensiv erwiesen: anders als bei beispielsweise Angular.js (mit welchem Vorerfahrung besteht), ist React nicht "*batteries-included*". Das bedeutet, dass es nicht von Hause aus den Großteil der für die Entwicklung und den Produktiveinsatz benötigten Werkzeuge mitbringt. Alleine die Konfiguration des für das produktive Arbeiten notwendige Webpacks hätte mehrere Seiten dieser Arbeit füllen können.

Ähnliches gilt für die neuartige clientseitige Applikationsarchitektur. Die objektorientierte Programmierung und den Einsatz des \ac{MVC}-Konzeptes gewöhnt, ist der Einstieg in die eingesetzten Konzepte, wie beispielsweise der uni-direktionale Datenfluss, aufwendig. Allerdings hat sich die Entscheidung für den gewählten Entwicklungsstack als richtig erwiesen: die in Abschnitt @sec:client-theorie aufgeführten Punkte wie zum Beispiel die sehr viel bessere Verständlichkeit der Architektur und die Vorhersehbarkeit von Zustandsänderungen haben den Entwicklungsprozess nach einer zu Beginn steilen Lernkurve sehr angenehm gestaltet.

In Bezug auf das Gesamtprojekt ist zu bemerken, dass in den letzten Wochen vor der Fertigstellung dieser Arbeit ein österreichischer Anbieter aufgetreten ist, welcher sehr vieles richtig macht. *openlaws.com* setzt ähnlich wie Lawly auf Open Data im juristischen Bereich aufzubereiten und zu verknüpfen. Mit einem scheinbar über zweijährigen Entwicklungsvorsprung konnte die Plattform außerdem bereits Fördergelder der Europäischen Union verbuchen. Obwohl der Start dieses direkten Konkurrenten anfänglich frustrierend war, bestätigt er auch die Notwendigkeit einer solchen Dienstleistung. Zusätzlich sind bei *openlaws.com* Open Data und Open Source zwar für Marketingzwecke beliebte Schlagwörter, allerdings keine von der Plattform selbst umgesetzten Prinzipien. Weder ist ihr Quelltext frei verfügbar, noch stellt sie eine Schnittstelle für die von ihr vermarkteten aufbereiteten Daten bereit. Beides Grundsätze, welche für Lawly zum Konzept gehören.



## Ausblick {#sec:discussion:forward}
Obwohl der Rückblick etwas dämpft, ist der Ausblick positiv. So ermöglichen die technologischen Entscheidungen durch das Heranreifen von React Native langfristige Entwicklungschancen -- um den Markt zu erreichen ist so beispielsweise die Entwicklung einer nativen iPad-Applikation mittelfristig denkbar.

In Bezug auf die realisierte Webapplikation gilt es vorerst die Performance weiter zu optimieren. Dazu gehört insbesondere auch die *gefühlte Performance*, welche die geschickte Verwendung von Animationen erfordert -- eine Thematik welche im bisherigen Entwicklungsverlauf noch nicht angegangen wurde. Außerdem gilt es, \acf{SSR} auch in Produktion einzusetzen und die Seite damit für Suchmaschinen zu optimieren. Dazu gehört auch der Gedanke mithilfe des gleichen \ac{SSR}-Codes durch die Generierung von \ac{AMP} einen Rankingvorteil bei Google zu erreichen. Google bevorzugt offiziell Seiten, welche diesen von ihnen offen entwickelten Standard einsetzen.[^makethewebgreatagain]

[^makethewebgreatagain]: [googleblog.blogspot.de/2016/02/amping-up-in-mobile-search.html](https://googleblog.blogspot.de/2016/02/amping-up-in-mobile-search.html), abgerufen 08/2016

Außerdem erfordert auch die Ansicht für die eigentlichen Gesetzestexte noch weitere Aufmerksamkeit, da dies die Ansicht ist, auf der Nutzer voraussichtlich die meiste Zeit verbringen werden. Von verbreiteten Anbietern für Lesedienste wie beispielsweise Pocket[^pocket] sind so zum Beispiel die Möglichkeiten zur Anpassung von Schriftart und -größe oder auch der Einsatz von mehrspaltigen Layouts bekannt.

[^pocket]: [getpocket.com](https://getpocket.com)

Letztendlich ist auch die Finanzierung des Projektes nicht zu vernachlässigen. Kurzfristig gilt es, zumindest die Kosten für den Betrieb zu decken und langfristig auch die Weiterentwicklung zu finanzieren. Vorläufig soll, auf Grundlage der in Abschnitt @sec:lawly vorgestellten Ideale, eine nicht kommerzielle Finanzierung im Vordergrund stehen. Dies wäre zum Beispiel durch eine Plattform wie Patreon[^buymeacookie] denkbar, bei welcher regelmäßige kleine Spenden zur langfristigen Finanzierung von Projekten im Vordergrund stehen. Außerdem steht der Prototypefund[^fundmebig], eine staatlich geförderte Initiative zur Förderung deutscher Open Source Projekte von öffentlichem Interesse, aus. Die Bewerbung um eine Förderung durch letzteren ist wohl der erste anstehende Schritt.

[^buymeacookie]: [patreon.com](https://www.patreon.com/)

[^fundmebig]: [prototypefund.de](https://prototypefund.de)

\vfill

![Aktuelles *lawly.org* Logo](assets/lawly.png){#fig:lawly}

\vfill
