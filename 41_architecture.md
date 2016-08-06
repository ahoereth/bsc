## Architektur
\label{sec:architecture}

  * API-Server / SPA-Client Architektur Entscheidung (Strukturell)
  * Programmiersprachliche Entscheidung, einführung in Javascript

Konzeptionell gilt es für die initiale Web-Applikation drei unabhängige Architekturen zu entwickeln:

  a) Datenbank
  b) Server
  c) Client

Bei dem Clienten handelt es sich im Rahmen dieser Arbeit, wie zuvor erläutert, um ein möglichst breites Spektrum an unterschiedlichen Plattformen erreichen zu können, bei dem Client um eine reine Web-Applikation. Um für zukünftige native Applikationen für die verschiedenen Plattformen gerüstet zu sein wird der Server als reiner \ac{API}-Server entwickelt, welcher unabhängig von den eigentlichen Applikationen agieren kann. Er stellt eine Reihe von klar definierten Schnittstellen bereit, welche die reinen Daten unabhängig von ihren in den verschiedenen Applikationen später möglicherweise sehr unterschiedlichen visuellen Repräsentationen bereit stellt. Die Datenbank als dritte, den anderen beiden zu Grunde liegende, Komponente wird eng gekoppelt mit dem API-Server entwickelt um die Daten möglichst effizient bereitstellen zu können. 

Durch diese konzeptionelle Trennung ergibt sich die Möglichkeit Server und Client auch strukturell zu trennen und so zum Beispiel über unterschiedliche Server bereitzustellen und diese unabhängig von einander der unter Betrieb und durch zu erhoffendes Wachstum entstehenden Last anzupassen, das sogenannte [*Scaling*](#glossary).

Neben dem API-Server wird auf die Datenbank außerdem von verschiedenen Skripten aus zugegriffen, welche Aktualisierungen der vorhandenen Gesetze vornehmen. Um diesen Prozess in Zukunft möglichst stark zu automatisieren oder zumindest zunächst möglichst linear zu gestalten, so dass ein Editor nur noch Aktualisierungen absegnen muss, wird es gelten hierfür eine getrennte Applikation zu entwickeln. Zugriff auf diese würde nicht den allgemeinen Nutzern sondern nur ausgewählten Editoren gewährt werden und sie würde über eigene Schnittstellen unabhängig von den eigentlichen Client-Produkten mit der Datenbank kommunizieren.

((Zusätzlich, allerdings nicht unbedingt im Rahmen dieser Arbeit, wird eine Landing-Page für das Produkt entwickelt. Mithilfe von A/B-Testing wird diese Schritt für Schritt optimiert und sondiert, noch vor allgemeiner Verfügbarkeit des eigentlichen Produkts, mögliche Interessenten und versucht diese zur Registrierung mit ihrer E-Mailadresse zu überzeugen.))
