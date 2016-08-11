### Laufzeit {#sec:js:runtime}

Listing: JavaScript Runtime Environment Model

~~~{#lst:js_model .dot}
digraph G {
  node [shape=square];
  splines=false;

  somenode [style=invis];
  script [shape=none];
  execution [shape=none];
  callstack [label="Call Stack"];
  native [label="Native APIs"];
  eventloop [label="Event Loop"];
  taskqueue [label="Task Queue"];

  {rank=same;script execution};
  {rank=same;callstack native};
  {rank=same;eventloop taskqueue};

  callstack -> execution [label="pop()"];
  callstack -> native [label="pop(): nativeFunc, callback"];
  native -> taskqueue [label="enqueue(callback, result)"];

  // Hack 1: Label on the left. Bonus: Whitespace fun.
  script -> callstack [label="push()"];
  script -> callstack [label="          "];

  // Hack 2: 2 bend arrows with labels on either side.
  callstack:s -> eventloop:n [label="notify() when empty" color=white];
  eventloop:n -> callstack:s [label="push(callback, result)" color=white];
  eventloop:c -> callstack:c [topath="bend right"];
  callstack:c -> eventloop:c [topath="bend right"];

  // Hack 3...
  taskqueue -> eventloop [label="invisible massively long label" style=invis];
  taskqueue -> eventloop [label="dequeue(): callback, result"];
  eventloop -> taskqueue [label="waitForEvent()"];
}
~~~


#### Script
Das Skript beinhaltet alle vom Programmierer spezifizierten Aufgaben. Seine Interpretation erfolgt abhängig von der jeweiligen Umgebung, es wird also in Quelltextform an den Browser ausgeliefert und dann von seiner JavaScript Laufzeit interpretiert -- heutzutage ist eine \ac{JIT} verbreitet: Das Skript wird kurz vor Ausführung zu Maschinencode compiliert, also zum Beispiel bei jedem individuellen Seitenaufruf.

Listing: JavaScript Quelltext mit synchroner und asynchroner Funktion.

~~~{#lst:js_script .javascript}
console.log('start');
function foo() {
  console.log('in foo');
  setTimeout(function callback() { 
    console.log('timedout'); 
  }, 3000);
}
foo();
console.log('end');
~~~


#### Callstack
Beim Aufruf einer Funktion aus dem Skript diese gemeinsam mit ihren Parametern als sogenannter *Stack Frame* auf den Callstack gelegt und ausgeführt. Immer der oberste Frame auf dem Stack befindet sich aktuell in Ausführung und bei Fertigstellung wieder vom Stack heruntergenommen.[^ecma_callstack] In Abbildung @lst:js_model ist dieser $push()/pop()$ Prozess in der $script \rightarrow Call\,Stack \rightarrow execution$ Route oben links sichtbar. Abbildung @lst:js_callstack1 zeigt einen Teil des durch den Quelltext in Listing @lst:js_script entstehenden Callstacks und seinen Auf- und Abbau von links nach rechts.

[^ecma_callstack]: Quelle [ECMA Spezifikation](http://www.ecma-international.org/ecma-262/5.1/#sec-10.3]

Listing: Callstack-Ausschnitt \\#1 zu Listing \\ref{lst:js_script}

~~~{#lst:js_callstack1 .dotpng scale=.33}
digraph structs {
  rankdir=LR;
  node [shape=record];

  a [xlabel=a label="||"];
  b [xlabel=b label="||console.log"];
  c [xlabel=c label="||"];
  d [xlabel=d label="||foo"];
  e [xlabel=e label="|console.log|foo"];
  f [xlabel=f label="||foo"];
  g [xlabel=g label="..." shape=none];

  a -> b [label="push"];
  b -> c [label="pop"];
  c -> d [label="push"];
  d -> e [label="push"];
  e -> f [label="pop"];
  f -> g;
}
~~~


#### Native APIs
JavaScript stellt eine Vielzahl Schnittstellen zu asynchronen \ac{API}s zur Verfügung. Diese sind nicht in der JavaScript Laufzeit selbst sonder in dem sie ausführenden Umgebung implementiert. Die in Listing @lst:js_script verwendete `setTimeout`-Funktion wird zum Beispiel von Browsern und der Node.js Umgebung zur Verfügung gestellt und ruft die ihr übergebene Funktion als Callback nach der definierten Zeit in Millisekunden auf. Andere derartige asynchrone Funktionen stehen zum Beispiel für Netzwerkanfragen (Browser und Node.js), Dateisystem Lese- und Schreiboperationen (Node.js), DOM-Manipulationen (Browser) und vieles mehr zur Verfügung. 

DOM
: Document Object Model
: Objektbasiertes hierarchisches Schema zur Darstellung von HTML- oder XML-Dokumenten. Stellt Definitionen von Schnittstellen zum lesen und bearbeiten dieser zur Verfügung.

Der in Abbildung @lst:js_callstack1 dargestellte Callstack behandelt nur synchrone Codeausführung. Abbildung @lst:js_callstack2 stellt nun den Callstack ab dem Aufrufen der `setTimeout` Funktion dar. Diese wird nun allerdings nicht direkt ausgeführt, sondern über den alternativen Pfad $Call\,Stack \rightarrow Native\,APIs$ abgearbeitet.

Während sich das umgebende System nun also mit dem Ausführen des Timeouts beschäftigt, wird auf JavaScript-Ebene der Callstack, wie in Abbildung @lst:js_callstack2 dargestellt, weiter abgearbeitet ohne für für die Wartezeit blockiert zu sein. Der Callstack schreitet also mit der sequentiellen Abarbeitung des Scripts fort, bis die letzte dort definierte Operation ausgeführt, egal ob direkt oder über die lokalen APIs, wurde. Sobald er keine weiteren Aufgaben hat, benachrichtigt er die Ereignisschleife (eng. Event Loop), vrgl. Abbildung @lst:js_model: $Call\,Stack \rightarrow Event\,Queue$.

Listing: Callstack-Ausschnitt \\#2 zu Listing \\ref{lst:js_script}

~~~{#lst:js_callstack2 .dotpng scale=.33}
digraph structs {
  rankdir=LR;
  node [shape=record];

  f [xlabel=f label="..." shape=none];
  g [xlabel=g label="|setTimeout|foo"];
  h [xlabel=h label="||foo"];
  i [xlabel=i label="||"];
  j [xlabel=j label="||console.log"];
  k [xlabel=k label="||"];

  f -> g [label="push"];
  g -> h [label="pop"];
  h -> i [label="pop"];
  i -> j [label="push"];
  j -> k [label="pop"];
}
~~~


#### Event Loop & Task Queue
Sobald die eine native \ac{API} ihre Berechnungen beendet hat, reiht sie es inklusive den ihr zuvor übergebenen Callback-Pointer an die Aufgabenwarteschlange (eng. Task-Queue) an. Die Ereignisschleife (eng. Event Loop) überwacht die Task-Queue und wartet darauf, vom Callstack über seine vollständige Abarbeitung benachrichtigt zu werden. Sobald diese Benachrichtigung erfolgt nimmt der Loop das am längsten in der Schlange wartende Element und legt es als Stack Frame wieder auf den Callstack auf, siehe Abbildung @lst:js_callstack3 und die Route $Call\,Stack \rightarrow Event\,Loop \leftrightarrow Task\,Queue \leftarrow Native\,APIs$ in Abbildung @lst:js_model.

Listing: Callstack-Ausschnitt \\#3 zu Listing \\ref{lst:js_script}

~~~{#lst:js_callstack3 .dotpng scale=.33}
digraph structs {
  rankdir=LR;
  node [shape=record];

  k [xlabel=k label="..." shape=none];
  l [xlabel=l label="||callback"];
  m [xlabel=m label="|console.log|callback"];
  n [xlabel=n label="||callback"];
  o [xlabel=o label="||"];

  k -> l [label="push"];
  l -> m [label="push"];
  m -> n [label="pop"];
  n -> o [label="pop"];
}
~~~

In Listing @lst:js_console wird die Ausgabe des Skripts aus Listing @lst:js_script dargestellt. Hier ist es interessant zu bemerken, dass durch die Struktur des hier beschriebenen Ausführungsprozesses die Ausgabe mit einer in Zeile 6 definierten Auszeit der Dauer $0$ (`setTimeout(callback, 0)`) die gleiche wäre: Der `setTimeout` Aufruf würde immer noch den gleichen Weg rechts durch den Graphen über die nativen APIs beschreiten, wodurch die Callback-Funktion bis zur vollständigen Abarbeitung des restlichen Quelltextes in der Ereigniswarteschlange verweilen würde.

Listing: Ausgabe durch den in Listing 1 (TODO) dargestellten Quelltext.

~~~{#lst:js_console .javascript}
start
in foo
end
timedout
~~~

Dieses Verständnis ist besonders für die Verwendung von JavaScript im Browser wichtig: Wenn der Callstack durch langwierige Berechnungen blockiert ist und der Nutzer gleichzeitig mit der Webseite interagiert, kann der Browser (Abbildung @lst:js_model: Native APIs) die durch die den Interaktionen zugeordneten Ereignisse zwar in die Task Queue einreihen, sie werden aus dieser allerdings nicht abgearbeitet. Dies führt dazu, dass die Webseite keine Reaktion auf die Nutzer-Aktionen zeigt -- selbst das wechseln auf eine andere Webseite über Hyperlinks kann dadurch blockiert werden. Sobald der Callstack wieder frei ist und der Event Loop beginnt die Task Queue abzuarbeiten, wird der Nutzer plötzlich mit allen Effekten seiner sich zwischenzeitlich durch möglicherweise verzweifeltes Wiederholen angehäuften Aktionen konfrontiert.

Gleiches gilt auf Webserver-Seite für das behandeln von Netzwerkanfragen: Der Callstack behandelt immer nur eine Anfrage auf einmal, bis diese entweder beantwortet oder, bis zum wieder auflegen durch den Event Loop, an die durch Node.js zur Verfügung gestellten nativen APIs übergeben wurde.
