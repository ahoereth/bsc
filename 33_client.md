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

Die Wahl der Programmiersprache zum entwickeln einer Web-Anwendung ist einfach: Es gibt keine Auswahl. Nur JavaScript ist in allen Web-Browsern verfügbar und damit die einzige mögliche Wahl. Zwar gibt es eine Hand voll Sprachen welche zu JavaScript [transcompiliert](#glossar), also übersetzt, werden, zu Zeiten zu denen sich der \ac{ES} Standard und seine Adoptionsrate schnell durchsetzt sind diese aber nur bei Notwendigkeit einer sehr speziellen Gruppe von Funktionen interessant. ((Single outstanding feature: Strong Typing from Typescript))

[Transcompilierung](#glossar) ist aber unabhängig von anderen Sprachen relevant. JavaScripts größter Vorteil, dass es in quasi jeder Browser Umgebung verfügbar ist, und dessen rasant fortschreitende Entwicklung, ist auch eine markante Achillesferse: Als Entwickler kann man nicht annehmen, dass Anwender einen Browser einsetzen welcher die aktuellste Iteration der Sprache standardkonform umsetzt. Aus diesem Grund haben sich Tools zur Transcompilierung des aktuellsten \ac{ES} Standards zu breiter unterstützten, älteren Iterationen durchgesetzt. In Kombination mit sogenannten [Polyfills](#glossar), Codes welche noch nicht vorhandene Funktionen mithilfe bestehender Funktionen nach implementieren, ist es so möglich den aktuellsten Stand der Sprache einzusetzen und trotzdem vom Vorteil der breiten Verfügbarkeit zu profitieren.



### Grundlegende Architektur

Software Projekte aller Art leiden ab einer gewissen Größe unter ihrem eigenen Funktionsumfang -- der zu Grunde liegende Code läuft Gefahr mit wachsendem Umfang unübersichtlich zu werden. Um dies zu vermeiden ist eine klare Codestruktur notwendig. Für user-facing applications hat sich diesbezüglich für lange Zeit das \ac{MVC} Prinzip etabliert. Dieses beschreibt den Ansatz jede einzelne Ansicht der Applikation in drei miteinander interagierenden Teilen zu beschreiben: Der *View* für die Visualisierung der durch das *Model* beschrieben und mithilfe des *Controllers* zur Verfügung gestellten Daten. 

Mit dem Trend zu immer dynamischeren Applikationen hat sich dieser Ansatz allerdings als sehr grob herausgestellt. Es ist nicht länger der Fall, dass eine einzelne Funktionalität nur in einer bestimmten Ansicht dargestellt und damit nur von einem bestimmten \ac{MVC}-Baustein beschrieben werden kann. Einzelne Bestandteile einer Applikation interagieren immer stärker miteinander was nach dem bisherigen Prinzip schnell in sich wiederholenden Code und unübersichtlichen Datenfluss zwischen einzelnen Komponenten resultieren kann. 

<!-- Ähnliches gilt für OOP -->

Um diese Probleme anzugehen hat sich speziell in der Web-Entwicklung in den letzten Jahren ein neuer Trend zu einer sehr viel stärkeren Modularisierung von Applikationen durchgesetzt. Eine Web-Applikation besteht nicht länger aus $n$ \ac{MVC}-Bausteinen, wobei $n$ der Anzahl von Applikations-*seiten* entspricht, sondern aus einer Vielzahl einzelner möglichst einfacher Module welche durch ihre flexibel Kombination ein dynamisches Interface ergeben. Ein einzelnes Modul ist hiernach ein möglichst in sich geschlossenes System welches sein Umfeld nicht beeinflusst und nur von einem klar definierten von außen gegebenen Zustand abhängt. Module können komplexere Funktionalität durch eine hierarchische Vererbung an andere Module implementieren und bleiben so in sich selbst überschaubar. Dieses Prinzip basiert auf der Idee, dass es zu bevorzugen ist, Code zu schreiben welcher eine klar definierte atomare Aufgabe erfüllt, da er dadurch auch für andere Entwickler leichter zu verstehen und auch leichter zu [maintainen](#glossary) ist.

In Abbildung \ref{todo_hierarchy} wird exemplarisch die Komponenten-Hierarchie einer fiktiven Applikation zur Aufgabenverwaltung dargestellt. Die Applikation besteht aus einer Liste aktueller Aufgaben, einem Eingabefeld um neue Aufgaben hinzuzufügen und der Möglichkeit erfüllte Aufgaben zu löschen. Die allen übergeordnete Komponente `TodoApp`, die sogenannte Wurzel, vererbt an die `TodoList`- und `TodoInput`-Komponenten. `TodoList` vererbt an die `TodoEntry`-Komponente um mithilfe dieser eine Liste aller vorhandenen Aufgaben darzustellen.

```{.dot caption="Applikation zur \textbf{Aufgabenverwaltung}" label="todo_hierarchy"}
digraph {
  node [shape=none];
  TodoApp -> {TodoList TodoInput};
  TodoList -> TodoEntry;
  {rank=same;TodoEntry TodoInput};
}
```

<!-- TODO: Add visual outline of TodoApp -->

Eine weitere Problematik ist, dass traditionell jeder Baustein einer Applikation über einen eigenen selbstverwalteten Zustand verfügt den er selbst durch den Controller und Interaktionen mit dem View manipuliert und gegebenenfalls über das Model an den wie auch immer gearteten persistenten Zustand (wie z.B. die Datenbank oder API) weiter gibt. Hieraus resultiert wieder die Schwierigkeit dass der Zustand eventuell von mehreren Teilen der Applikation benötigt und eventuell auch von mehreren manipuliert wird. <!-- TODO: Reasoning auf Deutsch? --> Reasoning über sich durch verschiedene Aktionen ergebende Ereignisse und Zustandsänderungen in der gesamt Applikation werden schwer.

Die moderne Lösung hierfür liegt in einem uni-directional Datenfluss mit einem zentral verwalteten und nur über klar definierte Funktionen zu beeinflussenden Zustand. Bei strengem Befolgen dieses Ansatzes wird der gesamte Zustand der gesamte Zustand der Applikation, also auch wenn er nur für einzelne Komponenten relevant ist, zentral verwaltet und entlang der zuvor beschriebenen Komponenten-Hierarchie vererbt. Die Vererbung findet immer partiell statt, so dass jede Komponente nur die Untermenge des gesamt Zustandes kennt, die für sie beziehungsweise für ihr untergeordnete Komponenten relevant ist. Im gesamten Prozess beeinflusst keine Komponente den ihr übergebenen Zustand direkt, sondern nur über zentral definierte Funktionen, sogenannte Aktionen. Durch diese Zentralisierung von Zustand und Zustand-manipulierenden Aktionen wird die Applikation und insbesondere Zustandsveränderungen innerhalb der Applikation leichter durchschaubar. Zusätzlich entsteht die Möglichkeit den Zustand persistent für zukünftige Aufrufe der Applikation zu speichern, einzelne Aktionen zu simulieren und gegebenenfalls rückgängig zu machen.

```{.dot caption="Uni-direktionaler Datenfluss mit zentralem globalen Zustand, partieller Zustandsvererbung und Aktions-basierter Zustandsmanipulation." label="dataflow"}
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




* Redux
* Zentraler Store
* Linearer Datenstrom

#### Actions

#### Reducers

#### Store

### React

* Komponenten Hierarchie
* Virtual DOM

```{.dot caption="\textbf{Home} component layout" label="components_home"}
digraph {
  HomeContainer -> Home;
  Home -> WelcomeMessage;
  Home -> LoginForm;
  Home -> LawList;
}
```

#### Container

* Interaktion mit Redux

#### Components

* *Dumme* Komponenten
* Weiß nichts von Redux --> leicht zu testen
* Zum großen Teil komplett state less -> leicht zu testen


\pagebreak

### Design

* Material Design
