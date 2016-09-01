## Client Architektur {#sec:client-architecture}
Ähnlich dem @sec:server-architecture setzt auch die Client Applikation im Sinne einer besseren Übersichtlichkeit und Testbarkeit auf stark modularen Code. Im folgenden wird auf die einzelnen Bestandteile und auf den Buildprozess, also der Schritt von rohem Quelltext zu für die Auslieferung vorbereiteten Paket, eingegangen.

### Struktur
Listing: Vereinfachte Ordnerstruktur der Client-Applikation

~~~{#lst:folders}
components/
containers/
helpers/
modules/
store/
client.js
server.js
~~~

Der Quelltext der Anwendung setzt sich vereinfacht durch die in Listing @lst:folders dargestellte Ordnerstruktur zusammen. Hierbei sind die beiden aufgeführten JavaScript-Dateien, `client.js` und `server.js` die jeweiligen Einstiegspunkte für den Bundler (siehe @sec:bundler). Respektive sind sie für einerseits die Generierung des an den Browser zu übertragene JavaScript-Paket und andererseits die Generierung der HTML-Shells und das Zurverfügungstellen der statischen Dateien (JavaScript-Paket, HTML-Shells, Stylesheets) verantwortlich.

Hinter den oben aufgeführten Ordnern befinden sich die reinen React-Komponenten (siehe @sec:react), die Redux-Module (siehe @sec:redux) und die React-Redux-Container, welche für die Verbindung der beiden letzteren Verantwortlich sind. Der Store ist der zentrale Anlaufpunkt für den kompletten Datenfluss auf Clientseite und Helpers sind sonstige allgemein relevante Funktionalitäten welche nicht den vorhergehenden Kategorien zuordenbar sind.



### Transkompilierung & Bundling {#sec:bundler}
Wie in @sec:javascript beschrieben werden bei der Entwicklung der Single-Page-Webapplikation auf moderne, noch nicht in allen gängigen Browsern verfügbare JavaScript Funktionalitäten eingesetzt. Um trotzdem eine möglichst große Bandbreite an Browsern unterstützen zu können wird hierbei auf Transkompilierung gesetzt. Zusätzlich ist es von Interesse den benötigten Quelltext in einer Einzeldatei zu bündeln, um beim initialen Seitenaufruf möglichst wenige HTTP-Anfragen durchführen zu müssen. Bei jeder HTTP-Anfrage kommt es zu Wartezeiten zwischen Anfrage und Beginn des Antworterhalts, so dass das Übertragen von vielen Einzeldateien mehr Zeit in Anspruch nehmen würde als einer einzelnen welche alle vereinigt. Um die Dateigröße weiter zu verringern ist es wichtig, nur Code in das endgültige Paket zu übernehmen, welcher wirklich notwendig ist. Dies ist besonders beim einsetzen externer Bibliotheken nicht trivial, da diese oft unübersichtlich verschachtelt sind. Durch den Einsatz von \ac{ES6} Modulen und dem Ansatz von einem Einstiegspunkt aus den Modul-Baum zu traversieren ergibt sich die Möglichkeit nur eingesetzen Code zu übernehmen.

Um diese Schritte im Entwicklungsprozess zu automatisieren wird *Webpack* als sogenannter Bundler eingesetzt: Webpack traversiert von einem Einstiegspunkt aus den Modul-Baum und lädt die einzelnen Module mit Hilfe von verschiedenen Erweiterungen. Als eine dieser Erweiterungen wird *Babel* eingesetzt. Babel übersetzt zu ladenden JavaScript-Code von \ac{ES6} in eine Version mit breiter Unterstützung und rüstet je nach Anforderung Funktionen mithilfe von Polyfills nach.


Offline available
Im Rahmen dieser Arbeit fällt diese Entscheidung leicht: Gestarrte Gesetze.

**React Komponenten {#sec:react}**


**Redux Store & Module {#sec:redux}**
Der in @sec:dataflow beschriebene Datenfluss wird zentral durch den Redux-Store gehandhabt, welcher sich aus 3 primären Bestandteilen zusammensetzt:

  1. Der Zustand (*state*)
  2. Die Aktionen (*actions*)
  3. (*reducer*)

Der State ist ein einzelnes JavaScript Objekt, welches den gesamten Zustand der Applikation beinhaltet. React Komponenten lösen actions aus, welche mithilfe der reducer den Zustand beeinflussen.


* Redux
* Zentraler Store
* Linearer Datenstrom

* Actions
* Reducers
* Store

**React**

* Komponenten Hierarchie
* Virtual DOM
* SSR

```{.dot caption="\textbf{Home} component layout" label="components_home"}
digraph {
  HomeContainer -> Home;
  Home -> WelcomeMessage;
  Home -> LoginForm;
  Home -> LawList;
}
```

**Container**

* Interaktion mit Redux

**Components**

* *Dumme* Komponenten
* Weiß nichts von Redux --> leicht zu testen
* Zum großen Teil komplett state less -> leicht zu testen


\pagebreak

### Design

* Material Design
