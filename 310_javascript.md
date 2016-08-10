## JavaScript
Softwaretechnisch wird auf Server- und Client-Seite primär auf JavaScript gesetzt. Die Verwendung der gleichen Sprache erleichtert die Wartung und ermöglicht den Einsatz von universellem, sogenannten isomorphischem, Code: Server und Client können auf die gleichen Bibliotheken zugreifen und gegebenenfalls Funktionen und Klassen teilen. Dies erleichtert den Einstieg für neue Entwickler und im speziellen auch die Vereinigung von Frontend- und Backend-Rollen in Unternehmensstrukturen, welche traditionell getrennt wurden. Ein insbesondere bei jungen Unternehmen bzw. kleineren Unternehmungen großer Vorteil.

TODO: Hier auf mehr Vorteile eingehen, auch wenn sie später noch im Detail erläutert werden. 

Auf Client-Seite ist JavaScript die einzige Programmiersprache mit breiter Unterstützung in allen gängigen Browsern. Um JavaScript auch auf Serverseite zu interpretieren wird auf die Node.js Laufzeitumgebung gesetzt. 

Das Open Source Projekt Node.js (auch einfach *node* genannt) wurde initial 2009 vorgestellt. Ryan Dahl begann die Entwicklung initial auf Grund seiner Frustration mit den zu diesem Zeitpunkt vorherrschenden Webserver Laufzeitumgebungen. Durch die Notwendigkeit zu immer mehr und komplexeren Ein- und Ausgabe (I/O) Operationen, also der Kommunikation eines Programms mit seinem Umfeld, stießen traditionelle Systeme zunehmend an ihre Grenzen.[^nodejstalk]

[^nodejstalk]: Ryan Dahl's original Node.js presentation: [youtu.be/ztspvPYybIY](https://youtu.be/ztspvPYybIY)

Node interpretiert JavaScript-Quelltext mithilfe von Googles JavaScript Engine V8, welche auch in Googles hauseigenem Browser Chrome eingesetzt wird. 

JavaScripts größter Vorteil, dass es in quasi jeder Browser Umgebung verfügbar ist, und dessen rasant fortschreitende Entwicklung, ist auch eine markante Achillesferse: Als Entwickler kann man nicht annehmen, dass Anwender einen Browser einsetzen welcher die aktuellste Iteration der Sprache standardkonform unterstützt. Aus diesem Grund haben sich Tools zur [Transcompilierung](#glossar) des aktuellsten \ac{ES} Standards zu breiter unterstützten, älteren Versionen durchgesetzt. In Kombination mit sogenannten [Polyfills](#glossar), Codes welche noch nicht vorhandene Funktionen mithilfe bestehender Funktionen nach implementieren, ist es so möglich den aktuellsten Stand der Sprache einzusetzen und trotzdem vom Vorteil der breiten Verfügbarkeit zu profitieren.
