# Technologien und Paradigmen
\label{sec:technology}

## JavaScript
\label{sec:javascript}

Softwaretechnisch wird auf Server- und Client-Seite primär auf JavaScript in seiner aktuellsten Iteration gesetzt. Die Verwendung der gleichen Sprache erleichtert die Wartung und ermöglicht den Einsatz von universellem, sogenannten isomorphischem, Code: Server und Client können auf die gleichen Bibliotheken zugreifen und gegebenenfalls Funktionen oder Klassen teilen.

Der Server setzt auf die *nodejs* Laufzeitumgebung und bietet 2 Wege der Kommunikation mit Client-Applikationen an:

  1. Eine REST-API, über welche primär statische Daten wie Gesetzesdokumente zur Verfügung gestellt werden, und
  2. Websockets, welche für die Synchronisierung von atomaren Interaktionen der Nutzer mit der Applikation zwischen Datenbank und über mehrere Geräte hinweg zuständig sind.

Der Client selbst entsteht als \ac{SPA} auf Basis des *React* Frameworks und orientiert sich strukturell an den *Flux* Prinzipien (weitere Erläuterungen folgen). Funktional stellt die Web-Applikation den Nutzern nach initialer Registrierung das Durchsuchen, Lesen und Sammeln von Gesetzen zur Verfügung. Außer Gesetzessammlungen manuell zusammenzustellen kann der Nutzer auch auf vorgegebene Sammlungen zurückgreifen, eine solche würde zum Beispiel in ihrem Umfang dem zu Beginn vorgestellten *Schönfelder* entsprechen. Der Trick ist es, dies so interaktiv und komfortabel wie möglich zu gestalten, unabhängig von der Art Endgerät die der Nutzer verwendet. Zu den wichtigsten Eigenschaften der Applikation zählt daher, dass sie nach initialer Einrichtung auch für längere Zeitabschnitte komplett offline funktional ist. Sobald Nutzer ihre persönlichen *Regale* eingerichtet haben, ist die Interaktion mit diesen auch ohne aktive Internetverbindung möglich. Änderungen werden mit dem Server synchronisiert sobald wieder eine Internetverbindung verfügbar ist. Außerdem ist es für die Web-Applikation unabdingbar, dass sie universell auf einer möglichst großen Bandbreite von Geräten einsetzbar ist, um einen möglichst großen Markt testen zu können. Individuell optimierte native Lösungen, insbesondere für iPads (Erläuterung folgt), sind für spätere Phasen geplant.
