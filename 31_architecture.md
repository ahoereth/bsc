## Architektur
\label{sec:architecture}

  * API-Server / SPA-Client Architektur Entscheidung (Strukturell)
  * Programmiersprachliche Entscheidung, einführung in Javascript

Konzeptionell gilt es für die initiale Web-Applikation drei unabhängige Architekturen zu entwickeln:

  a) Datenbank
  b) Server
  c) Client

Bei dem Clienten handelt es sich im Rahmen dieser Arbeit, wie zuvor erläutert, um ein möglichst breites Spektrum an unterschiedlichen Plattformen erreichen zu können, bei dem Client um eine reine Web-Applikation. Um für zukünftige native Applikationen für die verschiedenen Plattformen gerüstet zu sein wird der Server als reiner \ac{API}-Server entwickelt, welcher unabhängig von den eigentlichen Applikationen agieren kann. Er stellt eine Reihe von klar definierten Schnittstellen bereit, welche die reinen Daten unabhängig von ihren in den verschiedenen Applikationen später möglicherweise sehr unterschiedlichen visuellen Repräsentationen bereit stellt. Die Datenbank als dritte, den anderen beiden zu Grunde liegende, Komponente wird eng gekoppelt mit dem API-Server entwickelt um die Daten möglichst effizient bereitstellen zu können. 

Neben dieser für den Betrieb der eigentlichen Applikation notwendigen Architektur gilt es außerdem 
Neben dem API-Server wird auf sie von verschiedenen Skripten aus zugegriffen welche (in Zukunft möglichst automatisiert) Aktualisierungen der vorhandenen Gesetze vornehmen.

((Zusätzlich, allerdings nicht unbedingt im Rahmen dieser Arbeit, wird eine Landing-Page für das Produkt entwickelt. Mithilfe von A/B-Testing wird diese Schritt für Schritt optimiert und sondiert, noch vor allgemeiner Verfügbarkeit des eigentlichen Produkts, mögliche Interessenten und versucht diese zur Registrierung mit ihrer E-Mailadresse zu überzeugen.))


### JavaScript

Softwaretechnisch wird auf Server- und Client-Seite primär auf JavaScript in seiner aktuellsten Iteration gesetzt. Die Verwendung der gleichen Sprache erleichtert die Wartung und ermöglicht den Einsatz von universellem, sogenannten isomorphischem, Code: Server und Client können auf die gleichen Bibliotheken zugreifen und gegebenenfalls Funktionen oder Klassen teilen.

Der Server setzt auf die *nodejs* Laufzeitumgebung und bietet 2 Wege der Kommunikation mit Client-Applikationen an:

  1. Eine REST-API, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Der Client selbst entsteht als \ac{SPA} auf Basis des *React* Frameworks und orientiert sich strukturell an den *Flux* Prinzipien (weitere Erläuterungen folgen). Funktional stellt die Web-Applikation den Nutzern nach initialer Registrierung das Durchsuchen, Lesen und Sammeln von Gesetzen zur Verfügung. Außer Gesetzessammlungen manuell zusammenzustellen kann der Nutzer auch auf vorgegebene Sammlungen zurückgreifen, eine solche würde zum Beispiel in ihrem Umfang dem zu Beginn vorgestellten *Schönfelder* entsprechen. Der Trick ist es, dies so interaktiv und komfortabel wie möglich zu gestalten, unabhängig von der Art Endgerät die der Nutzer verwendet. Zu den wichtigsten Eigenschaften der Applikation zählt daher, dass sie nach initialer Einrichtung auch für längere Zeitabschnitte komplett offline funktional ist. Sobald Nutzer ihre persönlichen *Regale* eingerichtet haben, ist die Interaktion mit diesen auch ohne aktive Internetverbindung möglich. Änderungen werden mit dem Server synchronisiert sobald wieder eine Internetverbindung verfügbar ist. Außerdem ist es für die Web-Applikation unabdingbar, dass sie universell auf einer möglichst großen Bandbreite von Geräten einsetzbar ist, um einen möglichst großen Markt testen zu können. Individuell optimierte native Lösungen, insbesondere für iPads (Erläuterung folgt), sind für spätere Phasen geplant.
