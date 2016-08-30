## Client {#sec:client-theory}
Im folgenden Abschnitt werden die bei der Implementierung der Applikation verfolgten Paradigmen erläutert. 

Zentral orientiert sich die angestrebte Nutzererfahrung der Applikation an dem 2015 von Alex Russel beschrieben Gesamtkonzept einer \ac{PWA}: Eine \ac{SPA} welche die besten Seiten von nativen mobilen Applikationen und Web-Applikationen vereint.[^pwa] Hierbei handelt es sich nicht um ein völlig neues Konzept, sondern vielmehr um eine clevere Kombination von bereits zuvor etablierten Einzelansätzen. Im Mittelpunkt dieser steht eine \ac{SPA} (@sec:spa), mit offline- (@sec:offline-first) sowie mobile-first (Abschnitt @sec:mobile-first) Grundsätzen entwickelt und durch serverseitiges Rendering und App-Shells (@sec:ssr-and-shells) erweitert.  (TODO: Manifest? Links? "Progessive"?)

[^pwa]: Quelle: [infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/); Abgerufen 08.2016

Bezüglich der Implementierung wird ein zum traditionell verbreiteten \ac{MVC}-Konzept im Kontrast stehender Ansatz einer Komponenten-Hierarchien (@sec:components) mit Uni-Direktionalem Datenfluss (@sec:dataflow) von unveränderbaren Datenstrukturen (@sec:immutable) vorgestellt und eingesetzt.



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



### Komponenten-Hierarchien {#sec:components}
Software Projekte aller Art leiden ab einer gewissen Größe unter ihrem eigenen Funktionsumfang -- der zu Grunde liegende Code läuft Gefahr mit wachsendem Umfang unübersichtlich zu werden. Um dies zu vermeiden ist eine klare Codestruktur notwendig. Für user-facing applications hat sich diesbezüglich für lange Zeit das \ac{MVC} Prinzip etabliert. Dieses beschreibt den Ansatz jede einzelne Ansicht der Applikation in drei miteinander interagierenden Teilen zu beschreiben: Der *View* für die Visualisierung der durch das *Model* beschrieben und mithilfe des *Controllers* zur Verfügung gestellten Daten. 

Mit dem Trend zu immer dynamischeren Applikationen hat sich dieser Ansatz allerdings als sehr grob herausgestellt. Es ist nicht länger der Fall, dass eine einzelne Funktionalität nur in einer bestimmten Ansicht dargestellt und damit nur von einem bestimmten \ac{MVC}-Baustein beschrieben werden kann. Einzelne Bestandteile einer Applikation interagieren immer stärker miteinander was nach dem bisherigen Prinzip schnell in sich wiederholenden Code und unübersichtlichen Datenfluss zwischen einzelnen Komponenten resultieren kann. 

Um diese Probleme anzugehen hat sich speziell in der Web\hyp{}Entwicklung in den letzten Jahren ein neuer Trend zu einer sehr viel stärkeren Modularisierung von Applikationen durchgesetzt. Eine Web-Applikation besteht nicht länger aus $n$ \ac{MVC}-Bausteinen, wobei $n$ der Anzahl von Applikations-*seiten* entspricht, sondern aus einer Vielzahl einzelner möglichst einfacher Module welche durch flexibel Kombination ein dynamisches Interface ergeben. Ein einzelnes Modul ist hiernach ein möglichst in sich geschlossenes System welches sein Umfeld nicht beeinflusst und nur von einem klar definierten von außen gegebenen Zustand abhängt. Module können komplexere Funktionalität durch mithilfe von hierarchischer Vererbung an andere Module implementieren und bleiben so in sich selbst überschaubar. Dieses Prinzip basiert auf der Idee, dass es zu bevorzugen ist, Code zu schreiben welcher eine klar definierte atomare Aufgabe erfüllt, da er dadurch auch für andere Entwickler leichter zu verstehen und auch leichter zu [maintainen](#glossary) ist.

In Abbildung @lst:todo_hierarchy wird exemplarisch die Komponenten-Hierarchie einer fiktiven Applikation zur Aufgabenverwaltung dargestellt. Die Applikation besteht aus einer Liste aktueller Aufgaben, einem Eingabefeld um neue Aufgaben hinzuzufügen und der Möglichkeit erfüllte Aufgaben zu löschen. Die allen übergeordnete Komponente `TodoApp`, die sogenannte Wurzel, vererbt an die `TodoList`- und `TodoInput`-Komponenten. `TodoList` vererbt an die `TodoEntry`-Komponente um mithilfe dieser eine Liste aller vorhandenen Aufgaben darzustellen.

Listing: Aufgabenverwaltungs-Applikation

~~~{#lst:todo_hierarchy .dot width=!}
digraph G {
  node [shape=none];
  TodoApp -> {TodoList TodoInput};
  TodoList -> TodoEntry;
  {rank=same;TodoEntry TodoInput};
}
~~~

~~~{#lst:law_index_components .dot}
digraph G {
  node [shape=none];
  LawIndex -> {LawInitialChooser LawCollectionChooser LawIndexLead LawList};
  {rank=same; LawInitialChooser LawCollectionChooser LawIndexLead LawList};
  LawList -> {Pagination DataTable};
  {LawInitialChooser LawCollectionChooser Pagination} -> Button
}
~~~

<!-- TODO: Add visual outline of TodoApp -->



### Uni-Direktionaler Datenfluss {#sec:dataflow}
Eine weitere Problematik ist, dass traditionell jeder Baustein einer Applikation über einen eigenen selbstverwalteten Zustand verfügt, welchen er selbst über einen Controller und Interaktionen mit dem View manipuliert und gegebenenfalls über das Model an den wie auch immer gearteten persistenten Zustand (wie z.B. die Datenbank oder API) weitergibt. Hieraus resultiert wieder die Schwierigkeit, dass der Zustand von mehreren Teilen der Applikation benötigt und auch von mehreren manipuliert werden könnte. Bei komplexen Applikationen kann hierdurch das Verständnis von über sich durch verschiedene Aktionen ergebende Ereignisse und Zustandsänderungen schnell schwer werden. Die moderne Lösung hierfür liegt in einem uni-direktionalem Datenfluss mit einem zentral verwalteten und nur über klar definierte Funktionen beeinflussbaren Zustand. 

Bei strengem Befolgen dieses Ansatzes wird der gesamte Zustand der Applikation, also auch wenn er nur für einzelne Komponenten relevant ist, zentral verwaltet und entlang der zuvor beschriebenen Komponenten-Hierarchie vererbt. Die Vererbung findet partiell statt, so dass jede Komponente nur den Teil des gesamt Zustandes kennt, die für sie beziehungsweise für ihr untergeordnete Komponenten relevant ist. Im gesamten Prozess beeinflusst keine Komponente den ihr übergebenen Zustand direkt, sondern greift hierfür auf zentral definierte Funktionen, sogenannte Aktionen, zurück. Durch diese Zentralisierung von Zustand und Zustand-manipulierenden Aktionen wird die Applikation und insbesondere Zustandsveränderungen innerhalb der Applikation leichter durchschaubar. Zusätzlich entsteht die Möglichkeit den Zustand persistent für zukünftige Aufrufe der Applikation zu speichern, einzelne Aktionen zu simulieren und gegebenenfalls rückgängig zu machen.

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

Durch die Kombination einer modularen Komponenten-Hierarchie mit uni-direktionalen Datenfluss und zentral verwalteten globalen Zustand ergibt sich ein dem funktionellen Programmieren ähnlichen Einfachheit: Atomare Bestandteile der Applikation generieren deterministisch gegeben dem gleichen Zustand unabhängig vom Rest der Applikation testbar das gleiche Resultat. Komponenten, welche diese Eigenschaft erfüllen, werden im folgenden auch *reine Komponenten* oder *pure components* genannt.

Initial wurde dieser Ansatz 2014 von Facebook unter dem Namen *flux* präsentiert.[^flux] Seitdem wurde das Konzept von der JavaScript Gemeinschaft aufgegriffen und hat sich in einer weniger komplexen Form durch die *Redux* Bibliothek[^redux] durchgesetzt und in diesem Projekt eingesetzt wird.

[^flux]: https://facebook.github.io/flux/docs/overview.html

[^redux]: http://redux.js.org/



### Unveränderbare Daten {#sec:immutable}
Als drittes Standbein neben dem Uni-Direktionalen Datenfluss und der Komponenten Hierarchie dienen in der entwickelten Anwendung unveränderbare Objekte, sogenannte *immutable objects* oder *immutables*.

Der verbreitetere und aus er objektorientierten Programmierung bekannte Ansatz ist es, mit Instanzen von Objekten zu arbeiten, welche während der Laufzeit eines Programms manipuliert werden. Sehr bekannt ist dieses Modell aus der objektorientierten Programmierung, bei welcher Objekte meist Methoden zur Verfügung stellen um ihren eigenen Zustand zu manipulieren. Das Problem hierbei ist, dass veränderbare Daten in nicht vorhersehbaren Zuständen resultieren können. In @lst:mutable_javascript ist Beispielhaft die Funktion `take` definiert, welche den Wert eines Attributes eines ihr übergebenen Objektes zurückgibt und den Wert des Attributes allerdings auch nachträglich verändert. Falls diese Funktion nicht vom sie einsetzenden Programmierer geschrieben wurde, könnte dies zu unvorhersehbaren Resultaten im weiteren Programmablauf führen.

Interessant hierbei ist auch, dass die Variable `obj` als `const`, also Konstante, definiert wurde: Konstant bedeutet hier allerdings nicht, dass der Wert des Objektes unverändert bleibt, sondern die in der Variable gespeicherte Referenz zu einem bestimmten Objekt. Das referenzierte Objekt ist allerdings veränderbar. Obwohl dieses verhalten bei angehenden Programmierern oft für Verwirrung sorgt, ist es ein auch aus anderen Sprachen wie C++ (`const`) oder Java (`final`) bekanntes Verhalten.

Listing: Pass-by-reference und veränderbare Daten in JavaScript

~~~{.javascript #lst:mutable_javascript}
function take(ref, key) {
  return ref[key]--;
}
const obj = { foo: 42 };
const foo = take(obj, 'foo');
// obj: { foo: 41 }
// foo: 42
~~~

Unveränderbare Datenstrukturen lösen dieses Problem, indem jede auf ihnen ausgeführte Operation ein neues Objekt zurückgibt, anstatt das alte direkt zu manipulieren (siehe Listing @lst:immutable_list).

Listing: Veränderbares Array und unveränderbare Liste in JavaScript

~~~{.javascript #lst:immutable_list}
import { List } from 'immutable';

const arr = [1, 2, 3];
arr.push(4);
// arr: [1, 2, 3, 4]

const list1 = List([1, 2, 3]);
const list2 = list1.push(4);
// list1: [1, 2, 3]
// list2: [1, 2, 3, 4]
~~~

Für ein besseres Verständnis kann man *immutables* statt als Objekte als individuelle Werte betrachten. Objekte sind Strukturen welche in ihren Attributen Referenzen auf andere Objekte beinhalten. Der Wert von Attributen eines Objektes sind also Referenzen, welche verändert werden können, ohne das jeweilige referenzierte Objekt zu ändern. Einzelne Werte wie der aus Java bekannte `String` oder `int` sind an sich unveränderbar -- gleiches gilt für *immutables*. Wird also die Änderung eines Attributes einer unveränderbaren Datenstruktur beauftragt, wird ein neues unveränderbares Objekt zurück gegeben welches diese Änderung reflektiert.
  
Deep Copy
:  Tiefe Kopie
:  Bei einer tiefen Kopie eines Objektes werden sämtliche vom Objekt beinhaltete Objekte ihrerseits tief kopiert. Im Kontrast zur tiefen Kopie werden bei einer flachen Kopie (*shallow copy*) nur das eigentliche Objekt mit den in seinen Attributen gespeicherten Referenzen kopiert, wobei die Referenzen aber weiterhin auf die selben Objekte zeigen.^[>\color{red}Definitionen im Text wie hier oder nur in ein eigenes Verzeichnis?]

Um nicht bei jeder Mutation eine veränderte tiefe Kopie des originalen Objektes zu erstellen und damit unnötig Speicher zu belegen wird bei der verwendeten Bibliothek, *immutablejs*, für die interne Repräsentation unveränderbarer Objekte auf sogenannte gerichtete azyklische Graphen mit gemeinschaftlicher Nutzung (eng.: *directed azyclic graphs (DAG) with structural sharing*) gesetzt. In Abbildung @lst:dag_mutation wurde hierfür ein Beispiel visualisiert: Im originalen Graph mit Wurzel *a* soll der verschachtelte Kind-Knoten *g* verändert werden. Um dies mit möglichst wenig Aufwand zu erreichen und den ursprünglichen Graphen unverändert zu lassen, werden die hier gestrichelt dargestellten Knoten, *a*, *c* und *g* in Form der gestrichelten Knoten, respektive *a2*, *c2* und *g2*, kopiert. Die Mutation findet auf dem neu erstellten Knoten *g2* statt und der neue Graph mit Wurzel *a2* setzt sich so Speicher sparend im dargestellten Beispiel zu über 50% aus bereits existierende unveränderte Knoten zusammen (durchgezogene Umrandung).

Listing: Mutation eines gerichteten azyklischen Graphen mit gemeinschaftlicher Nutzung

~~~{#lst:dag_mutation .dot format=png width=.8\\textwidth}
digraph G {
  node [shape=circle];
  splines=false;
  a -> {b c}
  b -> {d e f}
  c -> g
  g -> h

  a [style=dashed]
  c [style=dashed]
  g [style=dashed]
  a2 [style=dotted]
  c2 [style=dotted]
  g2 [style="dotted,filled"]
  a2 -> {b c2} [style=dotted]
  c2 -> g2 [style=dotted]
  g2 -> h [style=dotted]

  // Formatting hacks
  a -> a2 [style=invis]
  b -> c [style=invis]
  c -> c2 [style=invis]
  g -> g2 [style=invis]
  h2 [style=invis]
  h -> h2 [style=invis]
  g2 -> h2 [style=invis]
  bc [style=invis]
  b -> bc [style=invis]
  {rank=same;a a2}
  {rank=same;b bc c c2}
  {rank=same;g g2}
  {rank=same;h h2}
}
~~~

Insgesamt ergibt sich aus der Verwendung von unveränderbaren Datenstrukturen so gleich mehrere Vorteile: Einerseits ist es, wie bereits erläutert, für Entwickler leichter über Veränderungen von Datenstrukturen zu urteilen. Zusätzlich ist es bei der internen Verwendung der oben beschriebenen \ac{DAG}s für unveränderbare Objekte möglich, Objekte per nur anhand ihrer Identität zu Vergleichen, was zu starken Performance Vorteilen führt: Bei traditionellen veränderbaren Datenstrukturen ist es nötig eine tiefen Vergleich (eng: *deep comparison*) durchzuführen, bei dem jedes Attribut-Paar der zu vergleichenden Datenstrukturen individuell miteinander, wiederum tief, verglichen werden muss.

Listing: Identitätsvergleiche mit *immutablejs*

~~~{.javascript #lst:immutable_equality}
import { Map } from 'immutable';
const map1 = new Map({ a: 1, b: 2, c: 3 });
const map2 = map1.set('b', 2);
const map3 = map1.set('b', 50);
// map1 === map2
// map1 !== map3
~~~



### Zusammenfassung
^[>\color{red}Besserer Name, bessere Abschnitt-Strukturierung.]
Zusammenfassend lässt sich der verfolgte Ansatz einer Komponenten-Hierarchie mit uni-direktionaler Datenfluss und unveränderbaren Datenstrukturen in einem ähnlichen Kontrast zu einem Model-View-Controller Ansatz beschreiben, wie funktionelle Programmierung zu objektorientierter Programmierung:

Bei \ac{OOP} wird mit Instanzen von Objekten gearbeitet, welche jeweils ihren eigenen Zustand verwalten und durch Instanzmethoden die Manipulation von diesem ermöglichen. Referenzen auf Instanzen von Objekten werden vielfach an Funktionen übergeben welche die referenzierte Instanz manipulieren. Bei der funktionellen Programmierung hingegen werden Objekte als unveränderbar betrachtet. Der Aufruf einer Funktion verändert die ihm übergebenen Objekte nicht direkt, sondern gibt eine veränderte Kopie dieser zurück, welche solange benötigt in einem globalen Zustand gehalten werden.

Vergleichbar stellt ein \ac{MVC}-Triplet eine Instanz dar, welche ihren eigenen Zustand hält und diesen von sich aus und über von ihr zur Verfügung gestellte Methoden verändert. Im von uns verfolgten Ansatz hingegen sind einzelne Komponenten funktional und hängen nur von ihrem Input ab. Da alle Komponenten von einem gemeinsamen Zustand abhängen, ist der Zustand der gesamten Applikation allein durch diesen zu jedem Zeitpunkt klar definiert.


