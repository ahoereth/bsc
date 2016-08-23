## Client: Progressive Web Applikation

Offline-First
Mobile-First

* SPA
* SSR
* Responsive Design

### Single Page Applications {#sec:spa}
Traditionell wird bei dem Aufruf einer Webseite ein einzelnes HTML-Dokument vom Server an den Client übertragen, welches alle Informationen in einer bereits für die Darstellung strukturierten Form beinhaltet. Jede Interaktion mit einer solchen Webseite führt zu einer neuen Anfrage an den Server, welcher anhand der vom Clienten zur Verfügung gestellten Informationen eine neue Seite gegebenenfalls individuell generiert und zur Verfügung gestellt. Diesen Kreislauf von Anfrage an den Server, Darstellung der Webseite und Nutzerinteraktion mit dieser wird im folgenden als *vollständiger Roundtrip* bezeichnet, da jedes mal alle benötigten Daten übertragen werden. 

In Abbildung @lst:website wird dieser Kreislauf beispielhaft durchnummeriert dargestellt: Nach einer initialen Anfrage an den Server (1) antwortet dieser mit einer Webseite (2) mit welcher der Nutzer interagiert (3). Diese Interaktion löst eine Anfrage an den Server aus (4) welcher anhand dieser eine neue Webseite bereitstellt (5). Diese neue Webseite kann sich zwar inhaltlich mit der alten überschneiden, muss aber vom Clienten komplett neu dargestellt werden. An dieser Stelle beginnt der Kreislauf erneut: Der Nutzer interagiert mit der Seite (6), was in einer Anfrage an den Server resultiert (7) und so weiter.

Listing: Server-/Client-Kommunikation einer traditionellen Webseite

```{.dot #lst:website}
digraph {
  node [shape=none];
  SERV [label="Server"];
  APP1 [label="Website"];
  APP2 [label="Website"];
  APP3 [label="[...]"];
  USER [label="User"];

  VOID -> SERV [label="(1) initial req."]
  SERV:sw -> APP1 [label="(2) res."];
  USER -> APP1 [label="(3) action"];
  APP1 -> SERV:s [label="(4) req."]
  SERV -> APP2:nw [label="(5) res."];
  USER -> APP2 [label="(6) action"];
  APP2 -> SERV [label="(7) req."]
  SERV -> APP3 [style=dashed];
  USER -> APP3 [style=dashed];

  // Formatting hacks.
  VOID [label=""]
  VOID -> USER [style=invis]
  APP1 -> APP2 [style=invis];
  APP2 -> APP3 [style=invis];
  {rank=min;SERV}
  {rank=same;APP1 APP2 APP3};
  {rank=same;VOID USER}
  {rank=max;USER}
}
```

Eine erste Erweiterung dieses Ansatzes liegt in dem Einsatz von interaktiven JavaScript Elementen: Interaktive Elemente sind in diesem Fall solche Teile der Webseite, welche Interaktionen ohne einen Neuladen der Seite zur Verfügung stellen. Weit verbreitet ist dies zum Beispiel für Foto-Galerien auf Nachrichten Seiten, in welchen zu jedem Zeitpunkt nur ein Bild dargestellt wird, das Anzeigen eines weiteren aber nicht eine neue Webseite lädt sondern nur das alte Bild-Element mit dem neuen austauscht. Zusätzlich ist es mit Hilfe von \ac{AJAX} möglich an solche Interaktionen Anfragen an den Server zu koppeln und weitere Informationen, wie zum Beispiel die URL und Beschreibung des nächsten Bildes, nachzuladen.

\ac{AJAX} ist auch zentraler Teil von \ac{SPA}: Anstatt nur einzelne Elemente der Webseite mit Hilfe von JavaScript interaktiv zu gestalten, werden alle Interaktionen des Nutzers mit der Webseite durch JavaScript behandelt. Dieses Modell wird in Abbildung @lst:spa dargestellt: Ähnlich wie in Abbildung @lst:website stellt der Nutzer eine initiale Anfrage an den Server (1) woraufhin dieser die Webseite mit allen benötigten Skripts zur Verfügung stellt (2). Interaktionen des Nutzers mit der Applikation (3+) werden von nun an von dem vorgeladenen JavaScript-Code behandelt und resultieren, wenn nötig in für den Nutzer unsichtbaren \ac{AJAX}-Anfragen an den Server (4+) welcher mit den benötigten Daten antwortet (5+). Meist stellt der Server keine strukturellen Informationen sondern nur noch die rohen Daten zur Verfügung, welche dann auf Client-Seite strukturiert und dargestellt werden. Die gestrichelten Kanten sind von nun an also der neue Kreislauf ohne einen Austausch der eigentlichen Webseite.

Listing: Single-Page-Webapplikation Client-/Server-Kommunikation

```{.dot #lst:spa}
digraph {
  rankdir=BT
  node [shape=none];
  USER [label="User"];
  SERV [label="Content-Server"];
  API [label="API-Server"];
  APP [label="Single-Page-Application"];
  {rank=same;SERV API};
  {rank=same;USER APP};

  USER -> SERV [label="(1) initial request"];
  SERV -> APP [label="(2) response"];
  USER -> APP [label="(3+) interactions" style=dashed];
  APP  -> API [label="(4+) requests" style=dashed];
  API  -> APP [label="(5+) responses" style=dashed];
}
```

Verbreitet und auch in Abbildung @lst:spa dargestellt ist der Ansatz Content- und API-Server zu trennen. Der Content-Server ist für das zur Verfügung stellen von statischen Dateien wie den HTML- und JavaScript-Dokumenten oder auch Bilder verantwortlich. Der API-Server steht in Verbindung zur Datenbank und stellt die eigentlichen inhaltlichen Daten zur Verfügung: Sämtliche Texte oder auch die URLs von darzustellenden Bildern hält er vor.

Durch die zentrale Anforderung an die im Rahmen dieser Arbeit entwickelten Applikation, sich ähnlich nativer Software zu verhalten, ist die Entwicklung einer \ac{SPA} unabdingbar. Durch den Einsatz einer \ac{SPA} ist es Möglich Interaktionen sehr viel flüssiger zu behandeln: Ladezeiten können durch das vorladen von Daten im Hintergrund und die, durch die fehlende Notwendigkeit strukturelle Informationen zu übertragen, kleinere Größe der benötigten Daten verringert werden. TODO: Moar.

### Offline-First {#offline-first}
Ein zentraler Teil der Nutzererfahrung von Mobil- und Desktopanwendungen ist, dass sie auch ohne aktive Internetverbindung nutzbar sind, wenn eventuell auch eingeschränkt. Der zuvor beschrieben Ansatz der \ac{SPA} birgt bereits die Grundlage um offline Funktionalität auch für eine Web-Applikation möglich zu machen: Nach dem initialen laden der Seite werden alle Interaktionen des Nutzers mit der Webseite von dem vorgeladene JavaScript gehandhabt. Interaktionen, für welche die Applikation keine weiteren Anfragen an den Server stellen muss, sind so also schon ohne eine Internetverbindung möglich. Bei einem erneuten Aufruf der Seite und bei Verwendung von Teilen der Applikation welche auf Serveranfragen angewiesen sind ist allerdings eine bestehende Verbindung zum Internet notwendig.

Der von uns verfolgte Ansatz eine \ac{PWA} fordert allerdings mehr: 

  1) Die Applikation soll auch ohne eine aktive Internetverbindung aufrufbar sein.
  2) Zentrale Aspekte und häufig genutzte Funktionen der Applikation sollen auch ohne Internetverbindung zur Verfügung stehen.

Um diese beiden Probleme zu lösen wurden in den letzten Jahren mehrere unterschiedlich verbreitete Standards entwickelt, welche, um das gewünschte Ergebnis zu erzielen, es zu kombinieren gilt.

Bei Punkt 2 kommt die Struktur der \ac{SPA} wieder gelegen: Da alle Anfragen an den Server konzeptionell von dem vorgeladenen JavaScript-Code durchgeführt werden, ist es auch möglich, die Anfrage und Antwort umzuleiten: Antworten werden lokal gecached und zukünftige Anfragen wenn möglich aus diesem Cache beantwortet. 

Bei jeder Interaktion wird so clientseitig getestet ob die notwendigen Daten bereits lokal zur Verfügung stehen. Wenn dies der Fall ist, kann die Nutzeranfrage sofort ohne unnötige Ladezeit beantwortet werden. Dies führt zu einer besseren Nutzererfahrung weil Interaktionen so im besten Fall nicht mehr durch möglicherweise eingeschränkte Qualität der bestehenden Internetverbindung beeinträchtigt werden. Um dieses Nutzungsergebnis weiter zu verbessern werden idealerweise potentiell relevante Daten sofort beim initialen Seitenaufruf vorgeladen: In Bezug auf das im Rahmen dieser Arbeit behandelte Projekt ist dies zum Beispiel der immer relevante Index aller vorhandenen Gesetze und außerdem möglicherweise vom Nutzer zuvor als favorisiert markierte Gesetze.

Zu guter Letzt ist es Notwendig nicht nur bereits alle voraussichtlich relevanten Daten zusammen mit dem initialen Aufruf der Applikation zur Verfügung zu stellen, sondern über mehrere Aufrufe hinweg zu speichern und somit die Applikation auch ohne Internetverbindung verfügbar zu machen. Hieraus ergeben sich zwei neue Problematiken: Einerseits müssen nun vorgehaltene Daten, auf ihre Aktualität getestet und eventuell aktualisiert werden. Anderseits müssen, sobald eine Internetverbindung zum initialen Laden der Applikation nicht mehr relevant ist, auch zwingend Interaktionen welche nicht nur für die aktuelle Instanz relevant sind, lokal gespeichert und beim wieder erlangen einer Verbindung zum Server mit diesem abgeglichen werden.

Um dieser Komplexität entgegen zu treten bietet es sich an die Applikation *offline-first* zu entwickeln. Hierbei gilt es bei der Entwicklung anzunehmen, dass eine aktive Internetverbindung nicht der Standard ist. So werden alle Reaktionen auf Nutzeraktionen initial lokal berechnet und durchgeführt. Erst in einem zweiten Schritt werden diese dann, sobald eine Internetverbindung verfügbar ist, mit dem Server abgeglichen. Hierbei gilt, dass der Server immer "Recht" hat: Falls der Server als Ergebnis einer Aktion etwas anderes präsentiert als der Client, ersetzt das Ergebnis des Servers nachträglich das des Clients. Dies ist relevant da die Integrität des auf Clientseite ausgeführten Codes nicht garantiert werden kann. Somit kann es passieren, dass die Client-Applikation eine bestimmte Interaktion wie zum Beispiel das Löschen eines (wie auch immer gearteten) Eintrages genehmigt und lokal durchführt, der Server aber diese Aktion nicht autorisiert, die Löschung seinerseits also nicht durchführt und damit auch dem Client den Auftrag gibt sie rückgängig zu machen.



### Mobile First {#sec:mobile-first}

<!-- 
Beim Aufbau einer diesen Paradigmen folgenden Applikation ist es von Interesse einem "offline-first" Ansatz zu folgen. Ähnlich wie es bereits Standard ist sich beim Webdesign an "mobile-first" zu orientieren, betrachtet man quasi das schwächste beziehungsweise eingeschränkteste Glied der Kette als den Standard: Im optimalen Fall ist alles, was auf diesem Gerät nicht funktioniert, optional. Bei "mobile-first" ist so das Smartphone-Display meist der Maßstab für den gestaltet wird. An größere Displays passt sich das Layout dann möglichst durch relativ definierte Größen von Schriften und Containern und dynamisches fließen der Elemente, so dass je nach verfügbarer Fläche mehr oder weniger Container nebeneinander angezeigt werden, an.  -->


### Komponenten-Hierarchien
\label{sec:components}

Software Projekte aller Art leiden ab einer gewissen Größe unter ihrem eigenen Funktionsumfang -- der zu Grunde liegende Code läuft Gefahr mit wachsendem Umfang unübersichtlich zu werden. Um dies zu vermeiden ist eine klare Codestruktur notwendig. Für user-facing applications hat sich diesbezüglich für lange Zeit das \ac{MVC} Prinzip etabliert. Dieses beschreibt den Ansatz jede einzelne Ansicht der Applikation in drei miteinander interagierenden Teilen zu beschreiben: Der *View* für die Visualisierung der durch das *Model* beschrieben und mithilfe des *Controllers* zur Verfügung gestellten Daten. 

Mit dem Trend zu immer dynamischeren Applikationen hat sich dieser Ansatz allerdings als sehr grob herausgestellt. Es ist nicht länger der Fall, dass eine einzelne Funktionalität nur in einer bestimmten Ansicht dargestellt und damit nur von einem bestimmten \ac{MVC}-Baustein beschrieben werden kann. Einzelne Bestandteile einer Applikation interagieren immer stärker miteinander was nach dem bisherigen Prinzip schnell in sich wiederholenden Code und unübersichtlichen Datenfluss zwischen einzelnen Komponenten resultieren kann. 

<!-- Ähnliches gilt für OOP -->

Um diese Probleme anzugehen hat sich speziell in der Web\hyp{}Entwicklung in den letzten Jahren ein neuer Trend zu einer sehr viel stärkeren Modularisierung von Applikationen durchgesetzt. Eine Web-Applikation besteht nicht länger aus $n$ \ac{MVC}-Bausteinen, wobei $n$ der Anzahl von Applikations-*seiten* entspricht, sondern aus einer Vielzahl einzelner möglichst einfacher Module welche durch ihre flexibel Kombination ein dynamisches Interface ergeben. Ein einzelnes Modul ist hiernach ein möglichst in sich geschlossenes System welches sein Umfeld nicht beeinflusst und nur von einem klar definierten von außen gegebenen Zustand abhängt. Module können komplexere Funktionalität durch eine hierarchische Vererbung an andere Module implementieren und bleiben so in sich selbst überschaubar. Dieses Prinzip basiert auf der Idee, dass es zu bevorzugen ist, Code zu schreiben welcher eine klar definierte atomare Aufgabe erfüllt, da er dadurch auch für andere Entwickler leichter zu verstehen und auch leichter zu [maintainen](#glossary) ist.

In Abbildung @lst:todo_hierarchy wird exemplarisch die Komponenten-Hierarchie einer fiktiven Applikation zur Aufgabenverwaltung dargestellt. Die Applikation besteht aus einer Liste aktueller Aufgaben, einem Eingabefeld um neue Aufgaben hinzuzufügen und der Möglichkeit erfüllte Aufgaben zu löschen. Die allen übergeordnete Komponente `TodoApp`, die sogenannte Wurzel, vererbt an die `TodoList`- und `TodoInput`-Komponenten. `TodoList` vererbt an die `TodoEntry`-Komponente um mithilfe dieser eine Liste aller vorhandenen Aufgaben darzustellen.

Listing: Aufgabenverwaltungs-Applikation

~~~{#lst:todo_hierarchy .dot}
digraph G {
  node [shape=none];
  TodoApp -> {TodoList TodoInput};
  TodoList -> TodoEntry;
  {rank=same;TodoEntry TodoInput};
}
~~~

<!-- TODO: Add visual outline of TodoApp -->

### Uni-Direktionaler Datenfluss
Eine weitere Problematik ist, dass traditionell jeder Baustein einer Applikation über einen eigenen selbstverwalteten Zustand verfügt den er selbst durch den Controller und Interaktionen mit dem View manipuliert und gegebenenfalls über das Model an den wie auch immer gearteten persistenten Zustand (wie z.B. die Datenbank oder API) weiter gibt. Hieraus resultiert wieder die Schwierigkeit dass der Zustand eventuell von mehreren Teilen der Applikation benötigt und eventuell auch von mehreren manipuliert wird. <!-- TODO: Reasoning auf Deutsch? --> Reasoning über sich durch verschiedene Aktionen ergebende Ereignisse und Zustandsänderungen in der gesamt Applikation werden schwer.

Die moderne Lösung hierfür liegt in einem uni-directional Datenfluss mit einem zentral verwalteten und nur über klar definierte Funktionen zu beeinflussenden Zustand. Bei strengem Befolgen dieses Ansatzes wird der gesamte Zustand der gesamte Zustand der Applikation, also auch wenn er nur für einzelne Komponenten relevant ist, zentral verwaltet und entlang der zuvor beschriebenen Komponenten-Hierarchie vererbt. Die Vererbung findet immer partiell statt, so dass jede Komponente nur die Untermenge des gesamt Zustandes kennt, die für sie beziehungsweise für ihr untergeordnete Komponenten relevant ist. Im gesamten Prozess beeinflusst keine Komponente den ihr übergebenen Zustand direkt, sondern nur über zentral definierte Funktionen, sogenannte Aktionen. Durch diese Zentralisierung von Zustand und Zustand-manipulierenden Aktionen wird die Applikation und insbesondere Zustandsveränderungen innerhalb der Applikation leichter durchschaubar. Zusätzlich entsteht die Möglichkeit den Zustand persistent für zukünftige Aufrufe der Applikation zu speichern, einzelne Aktionen zu simulieren und gegebenenfalls rückgängig zu machen.

Listing: Uni-direktionaler Datenfluss mit zentralem globalen Zustand, partieller Zustandsvererbung und Aktions-basierter Zustandsmanipulation.

```{.dot #lst:dataflow}
digraph {
  rankdir=TB
  node [shape=none]
  S [label="State"]
  A [label="Component A"]
  B [label="Component B"]
  C [label="Component C"]
  {rank=same;A B C}
  S -> A [label="partial state"]
  A -> B [label="partial state"]
  B -> C [label="partial state"]
  A -> S [label="action" style=dashed];
  B -> S [label="action" style=dashed];
  C -> S [label="action" style=dashed];
}
```

Durch die Kombination einer modularen Komponenten-Hierarchie mit uni-direktionalen Datenfluss und zentral verwalteten globalen Zustand ergibt sich ein dem funktionellen Programmieren ähnlichen Einfachheit: Atomare Bestandteile der Applikation generieren deterministisch gegeben dem gleichen Zustand unabhängig vom Rest der Applikation testbar das gleiche Resultat.


### Unveränderbare Daten
\label{sec:immutable}

