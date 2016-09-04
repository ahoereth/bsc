## Client {#sec:client-theory}
Zentral orientiert sich die angestrebte Nutzererfahrung der Applikation an dem 2015 von Alex Russel beschrieben Gesamtkonzept einer \ac{PWA}: Eine \ac{SPA} welche die besten Seiten von nativen mobilen Applikationen und Web-Applikationen vereint.[^pwa] Hierbei handelt es sich nicht um ein völlig neues Konzept, sondern vielmehr um eine clevere Kombination von bereits zuvor etablierten Einzelansätzen. Im Mittelpunkt dieser steht eine \ac{SPA} (Abschnitt @sec:spa), mit offline- (Abschnitt @sec:offline-first) sowie mobile-first (Abschnitt @sec:mobile-first) Grundsätzen entwickelt.

<!--  und durch serverseitiges Rendering und App-Shells (Abschnitt @sec:ssr-and-shells) erweitert.  (TODO: Manifest? Links? "Progessive"?) -->

Bei der Umsetzung dieser Paradigmen wird ein zum traditionell verbreiteten \ac{MVC}-Konzept im Kontrast stehender Ansatz einer Komponenten-Hierarchien (@sec:components) mit Uni-Direktionalem Datenfluss (@sec:dataflow) von unveränderbaren Datenstrukturen (@sec:immutable) vorgestellt und eingesetzt.

[^pwa]: Quelle: [infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/); Abgerufen 08.2016



### Single Page Applications {#sec:spa}
Traditionell wird bei dem Aufruf einer Webseite ein einzelnes HTML-Dokument vom Server an den Client übertragen, welches alle Informationen in einer bereits für die Darstellung strukturierten Form beinhaltet. Jede Interaktion mit einer solchen Webseite führt zu einer neuen Anfrage an den Server, welcher anhand der vom Clienten zur Verfügung gestellten Informationen eine neue Seite gegebenenfalls individuell generiert und zur Verfügung gestellt. Diesen Kreislauf von Anfrage an den Server, Darstellung der Webseite und Nutzerinteraktion mit dieser bezeichnet man als *vollständigen Rundtrip*, da bei jede Wiederholung quasi einen Neustart darstellt.

In Abbildung @lst:website wird dieser Kreislauf beispielhaft durchnummeriert dargestellt: Nach einer initialen Anfrage an den Server (1) antwortet dieser mit einer Webseite (2) mit welcher der Nutzer interagiert (3). Diese Interaktion löst eine Anfrage an den Server aus (4) welcher anhand dieser eine neue Webseite bereitstellt (5). Diese neue Webseite kann sich zwar inhaltlich mit der alten überschneiden, muss aber vom Clienten komplett neu dargestellt werden. An dieser Stelle beginnt der Kreislauf erneut: Der Nutzer interagiert mit der Seite (6), was in einer Anfrage an den Server resultiert (7) und so weiter.

Listing: Synchrone Client-/Server-Kommunikation

```{#lst:website .dot}
digraph G {
  node [shape=rect]
  SERV [label="Server"]
  APP1 [label="Website"]
  APP2 [label="Website"]
  APP3 [label="[...]" shape=none]
  USER [label="User"]
  VOID [style=invis]

  VOID -> SERV [label="(1) initial req."]
  SERV:sw -> APP1 [label="(2) res."]
  USER -> APP1 [label="(3) action"]
  APP1 -> SERV:s [label="(4) req."]
  SERV -> APP2:nw [label="(5) res."]
  USER -> APP2 [label="(6) action"]
  APP2 -> SERV [label="(7) req."]
  SERV -> APP3 [style=dashed]
  APP1 -> APP2 [style=dotted]
  APP2 -> APP3 [style=dotted]

  // Formatting hacks.
  USER -> APP3 [style=invis]
  VOID [label=""]
  VOID -> USER [style=invis]
  {rank=min;SERV}
  {rank=same;APP1 APP2 APP3}
  {rank=same;VOID USER}
  {rank=max;USER}
}
```

Nachdem dieser Ansatz zu Beginn der Verbreitung von \ac{AJAX} vielmals mit einzelnen interaktiven Elementen erweitert wurde, wird bei einer \ac{SPA} der Rundtrip vollständig abgelöst. Dieses Modell wird in Abbildung @lst:spa dargestellt. Hierbei wird initial wieder eine initiale Anfrage an den Server gestellt (1) woraufhin dieser die Webseite mit allen benötigten Skripts zur Verfügung stellt (2). Im Kontrast zur normalen Webseite schaltet sich nun die JavaScript-Applikation zwischen Nutzerinteraktionen und Server (gestrichelte Kanten). Über Reaktionen auf Nutzerinteraktionen wird hierbei also direkt von der Applikation selbst, anstatt durch den Server geurteilt (3+). Hierbei ist nun der JavaScript-Code dafür verantwortlich, eventuell notwendige Serveranfragen zu stellen (4+) und die dargestellte Ansicht entsprechend ankommender Daten (5+) zu aktualisieren. Serveranfragen in Folge von Nutzeraktionen sind von nun an allerdings oftmals optional, da nicht für jede Änderung der Ansicht neue Daten notwendig sind.

Die Abbildung stellt den Content- und \ac{API}-Server bereits als zwei strukturell unabhängige Instanzen dar. Obwohl diese Trennung optional ist, ist sie oft erstrebenswert. Siehe hierzu Abschnitt @sec:server, Server.

Listing: Asynchrone Client-/Server-Kommunikation

```{.dot #lst:spa}
digraph G {
  rankdir=BT
  node [shape=rect]
  USER [label="User"]
  SERV [label="Content-Server"]
  API [label="API-Server"]
  APP [label="Single-Page-Application"]
  {rank=same;SERV API}
  {rank=same;USER APP}

  USER -> SERV [label="(1) initial req."]
  SERV -> APP [label="(2) res.   "]
  USER -> APP [label="(3+) actions" style=dashed]
  APP  -> API [label="(4+) req.   " style=dashed]
  API  -> APP [label="(5+) res." style=dashed]
}
```

Durch die zentrale Anforderung an die im Rahmen dieser Arbeit entwickelten Applikation, sich ähnlich nativer Software zu verhalten, ist die Entwicklung einer \ac{SPA} unabdingbar. Durch den Einsatz einer \ac{SPA} ist es Möglich Interaktionen sehr viel flüssiger zu behandeln: Ladezeiten können durch das Vorladen von Daten im Hintergrund und die, durch die fehlende Notwendigkeit strukturelle Informationen zu übertragen, kleinere Größe der benötigten Daten verringert werden. Außerdem ist es möglich durch visuelle Anpassungen wie Animationen ein flüssigeres Nutzungserlebnis zu simulieren, wo bei traditionellen Webseiten eine von Stillstand geprägte Wartezeit zu finden war.



### Offline-First {#offline-first}
Ein zentraler Teil der Nutzererfahrung von Mobil- und Desktopanwendungen ist, dass sie zu einem gewissen Maße auch ohne aktive Internetverbindung nutzbar sind. Der zuvor beschrieben Ansatz der \ac{SPA} birgt bereits die Grundlage um solche Funktionalität auch für eine Web-Applikation möglich zu machen: Nach dem initialen Laden der Seite werden alle Interaktionen des Nutzers mit der Webseite von dem vorgeladene JavaScript gehandhabt. Interaktionen, für welche die Applikation keine weiteren Anfragen an den Server stellen muss, sind so also schon ohne eine Internetverbindung durchführbar. Bei einem erneuten Aufruf der Seite und bei der Verwendung von Teilen der Applikation, welche auf Serveranfragen angewiesen sind, ist allerdings eine bestehende Internetverbindung notwendig.

Initial gilt es, den wiederholte Seitenaufrufe auch ohne Internetverbindung zu ermöglichen. Hierfür gibt es zwei standardisierte Technologien: Den *Application Cache* sowie *Service Worker*. Obwohl der Service Worker die mächtigere Technologie ist, wird für Lawly, aufgrund der mangelnden Verfügbarkeit von Service Workern auf Apple Geräten, auf den Application Cache gesetzt.[^cantuseserviceworker] Der Application Cache erlaubt es, mithilfe eines *Cache Manifest* zuverlässig Dateien zu definieren, welche auch ohne Internetverbindung verfügbar sein sollen. Dabei werden, nachdem diese Dateien initial gecached wurden, zukünftige Anfragen ohne Verbindungslatenzen aus diesem Cache beantwortet und nur gezielt bei Aktualisierung des Manifestes aktualisiert.

[^cantuseserviceworker]: Safari, welcher unter iOS auch als Grundlage für Browser Dritter dient, implementiert noch keine Service Worker. Quelle: [caniuse.com](http://caniuse.com/#feat=serviceworkers); Abgerufen 08/2016.

Um nicht nur statische Dateien bei fehlender Internetverbindung zur Verfügung stellen zu können, gilt es, Anfragen innerhalb der Applikation so zu gestalten, dass sie nicht nur durch Zugriff auf die \ac{API}, sondern auch aus einem auf dem Gerät zur Verfügung stehenden Speicher beantwortet werden. Dafür ist es am einfachsten eine zentrale Klasse zu entwickeln, über welche sämtliche Anfragen aus der Applikation verwaltet werden. Diese bevorzugt dabei den lokalen Speicher gegenüber der externen \ac{API}. Falls also die gesuchten Daten im lokalen Speicher vorhanden sind, werden diese unmittelbar verarbeitet. Gleichzeitig hierzu wird auch eine Frage an die externe Schnittstelle gestellt, mit deren eventueller Antwort gegebenenfalls die zuvor eventuell bereits durchgeführte Verarbeitung sowie die lokal vorgehaltenen Daten auf aktualisiert werden.

Zu guter Letzt ist es nicht nur notwendig, relevanten Daten ohne Internetverbindung verfügbar zu machen, sondern auch Interaktionen mit der getrennten Applikation bei Wiedererlangen einer Verbindung mit dem Server abzugleichen. Auch hierbei ist wieder die im letzten Absatz beschrieben zentrale Klasse zum verwalten von Anfragen hilfreich. Falls diese feststellt, dass eine Anfrage an den Server fehlgeschlagen ist, werden die für die Anfrage notwendigen Parameter serialisiert und gespeichert. Sobald wieder eine Internetverbindung verfügbar ist, werden die gespeicherten Anfragen abgearbeitet und damit der lokale Zustand mit dem des Servers abgeglichen.

Da die Umsetzung solcher lokaler Speicher in den verschiedenen Browser sehr variieren, wird hierfür die *localForage* Bibliothek der Mozilla Foundation eingesetzt. Zwar bieten manche Browser bereits eloquente lokale Datenbanken, allerdings kommt für dieses Projekt eine Einschränkung auf solche Plattformen nicht in Frage. *localForage* ermöglicht es, in allen verbreiteten Browsern[^browsers], zuverlässig einen implementationsunabhängigen key-value store einzusetzen.

[^browsers]: Die einzigen durch *localForage* nicht unterstützten Browser sind Versionen <8 des Internet Explorers, welche auf einen Marktanteil von unter 1% kommen. Quelle: https://www.netmarketshare.com/browser-market-share.aspx; Abgerufen 08/2016.



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

Listing: Uni-direktionaler Datenfluss

```{.dot #lst:dataflow}
digraph G {
  rankdir=TB
  node [shape=rect]
  S [label="State" shape=ellipse]
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

Um nicht bei jeder Mutation eine veränderte tiefe Kopie des originalen Objektes zu erstellen und damit unnötig Speicher zu belegen wird bei der verwendeten Bibliothek, *immutablejs*, für die interne Repräsentation unveränderbarer Objekte auf sogenannte gerichtete azyklische Graphen mit gemeinschaftlicher Nutzung (eng.: *directed azyclic graphs (DAG) with structural sharing*) gesetzt. In Abbildung @lst:dag_mutation wurde hierfür ein Beispiel visualisiert: Im originalen Graph mit Wurzel *a* soll der verschachtelte Kind-Knoten *g* verändert werden. Um dies mit möglichst wenig Aufwand zu erreichen und den ursprünglichen Graphen unverändert zu lassen, werden die hier gestrichelt dargestellten Knoten, *a*, *c* und *g* in Form der gestrichelten Knoten, respektive *a2*, *c2* und *g2*, kopiert. Die Mutation findet auf dem neu erstellten Knoten *g2* statt und der neue Graph mit Wurzel *a2* setzt sich so Speicher sparend im dargestellten Beispiel zu über 50% aus bereits existierende unveränderte Knoten zusammen (durchgezogene Umrandung).

Deep Copy
:  Tiefe Kopie
:  Bei einer tiefen Kopie eines Objektes werden sämtliche vom Objekt beinhaltete Objekte ihrerseits tief kopiert. Im Kontrast zur tiefen Kopie werden bei einer flachen Kopie (*shallow copy*) nur das eigentliche Objekt mit den in seinen Attributen gespeicherten Referenzen kopiert, wobei die Referenzen aber weiterhin auf die selben Objekte zeigen.^[>\color{red}Definitionen im Text wie hier oder nur in ein eigenes Verzeichnis?]

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


### React Native

* Interface & Computational thread
