### Concurrency
Bei der Interpretation von Quelltext oder auch der Ausführung von compilierten Code wird sequentiell, also Operation für Operation in der im Quelltext vorgegebenen linearen Ordnung, ausgeführt. Dabei blockiert jede einzelne Operation das fortschreiten der Ausführung bis zu ihrer vollständigen Beendigung. Werden nun I/O-Operationen genauso wie alle anderen Operationen synchron bzw. blockierend ausgeführt, können unkalkulierbare Wartezeiten entstehen: Das ausführende Programm begibt sich in komplette Abhängigkeit zu einem anderen Programm bis dieses seine Berechnungen fertiggestellt hat. Bei linearem Code ist dieses blockierende Vorgehen nicht ohne weiteres vermeidbar, da spätere Zeilen Code in der Regel auf den erfolgreichen Abschluss der Ausführung von vorhergehenden Zeilen angewiesen sind.

Bei einfachen Programmen ist diese Herangehensweise meist unproblematisch und auch anerkannt. Informatiker wird zu Beginn Ein- und Ausgabe als synchrone Operation beigebracht. Das erste Programm für angehende Programmierer ist oft vergleichbar mit dem in Listing @lst:javaio dargestellten: Die Eingabeoperation `IO.readInt()` in Zeile 6 unterbricht implizit die Programmausführung, bis die Nutzereingabe durch einen Zeilenumbruch beendet wird. Code in Zeile 7ff kann nur ausgeführt werden, wenn Zeile 6 erfolgreich ausgeführt wurde. Dies gilt unabhängig davon, ob der weitere Verlauf des Programms von dem Ergebnis der Eingabe in Zeile 6 abhängt.

Listing: Blockierende I/O-Operationen in Java

~~~{#lst:javaio .java}
import java.util.Scanner;
public class JavaIO {
  public static void main(String[] argv) {
    Scanner in = new Scanner(System.in);
    System.out.print("Your name: ");
    String name = in.nextLine();
    // Blocking -- wait for user input.
    System.out.println("Hello " + name);
  }
}
~~~

Listing @lst:pythonio stellt ein etwas komplexeres und ein speziell für Webserver sehr relevantes Beispiel dar: Die Datenbankabfrage in Zeile 4 blockiert bis zu ihrer Fertigstellung die weitere Ausführung des Programmcodes. Hierbei besteht die Gefahr, dass die Anfrage längere Zeit in Anspruch nehmen könnte, falls zum Beispiel die Verbindung zur Datenbank durch schlechte Latenzzeiten Aufgrund großer geographischer Entfernung eingeschränkt wäre. Die auf die Datenbankoperation folgenden Zeilen des Quelltextes werden erst nach vollständigem Abschluss der Anfrage ausgeführt.

Listing: Blockierende Datenbankoperation in Python

~~~{#lst:pythonio .python}
from mysql import connector
db = connector.connect(*configuration)
cursor = db.cursor()
cursor.execute('SELECT * FROM foo')
# Blocking -- wait for result.
rows = cursor.fetchAll()
~~~

Obwohl rein sequentieller Code für Programmierer sehr komfortabel und leicht verständlich ist, ist diese Herangehensweise bei Programmen welche mit vielen Anfragen zu tun haben problematisch. Insbesondere bei Webservern sind solche blockierende Operationen unakzeptabel, da in dieser Zeit durch den blockierten Prozess keine anderen Anfragen beantwortet werden können.

Die Lösung für dieses Problem liegt darin, Code nicht immer sequentiell, sondern, wenn angebracht, gegebenenfalls nichtsequentiell auszuführen. Dieses Konzept nennt sich Nebenläufigkeit bzw. Concurrency.

Concurrency
  : *Nebenläufigkeit*, *Parallelität*
  : Eigenschaft eines Systems, mehrere Berechnungen, Anweisungen oder Befehle gleichzeitig ausführen zu können. Es kann sich dabei um völlig unabhängige Anweisungen handeln, bis hin zur gemeinsamen Bearbeitung einer Aufgabe.[^concurrencywiki]

[^concurrencywiki]: Quelle: [de.wikipedia.org/wiki/Nebenläufigkeit](https://de.wikipedia.org/wiki/Nebenl%C3%A4ufigkeit)


#### Echte Nebenläufigkeit
Eine bei Webservern verbreitete Art der Umsetzung von Concurrency ist es, jede Anfrage mit Hilfe eines einzelnen Prozesses (auch *Thread*) zu beantworten. Diese Herangehensweise wird zum Beispiel vom sehr populären[^webserverstats] Apache HTTP Server umgesetzt. Jede HTTP Anfrage an den Server startet einen eigenen Prozess welcher ganz der Beantwortung dieser einen Anfrage gewidmet ist und dessen I/O-Operationen nur ihn selbst blockieren und nicht den gesamten Webserver. Bei viele gleichzeitige Verbindungen, sogenannte *concurrent connections*, ist diese Herangehensweise allerdings extrem Ressourcen hungrig: Jeder Thread benötigt eigene Arbeitsspeicher-Allokation und die bei jeder Anfrage notwendigen Kontextwechsel, also das wechseln zwischen verschiedenen aktiven Prozessen, sind Rechenintensiv.

[^webserverstats]: Quelle: [w3techs.com/technologies/overview/web_server/all](https://w3techs.com/technologies/overview/web_server/all); Abgerufen 08/2016.]

TODO: Andere Arten von *echter* Concurrency.

#### Event-Loop
Eine alternative Herangehensweise ist einer Art der gewissermaßen simulierten Nebenläufigkeit: Mithilfe von asynchronen I/O-Operationen und eines Event Loops wird dem Anwender eine Art Parallelität vorgegaukelt, obwohl der Programmcode weiterhin nur auf einem einzelnen Thread ausgeführt wird.

Diese Herangehensweise ist einer der essentiellen Bestandteile von JavaScript. Dies gilt nicht nur Serverseitig innerhalb von Node.js, sondern insbesondere auch Clientseitig im Browser. Browser sind traditionell Programme welche nur in einem einzelnen Prozess ausgeführt wurden. Dadurch ,dass sie gewissermaßen die Laufzeitumgebung von clientseitigen JavaScript-Programmen darstellen, sind auch diese an den gleichen, einzelnen Prozess gebunden. Zwar setzen aktuelle Versionen des Firefox und Chrome Browsers auf einzelne Prozesse für individuelle Tabs, allerdings jedes Tab weiterhin nur auf einen einzelnen. Auch in solchen modernen Browsern ist die diese Einschränkung noch immer leicht provozierbar: Wenn ein auf einer Webseite ausgeführtes Script komplexe sequentielle Berechnungen durchführt, ist schnell merklich, dass die Interaktion mit der Webseite eingeschränkt ist. Klicks auf Links führen in einer solchen Situation zum Beispiel nicht mehr zu einem Seitenwechsel. Erst sobald die Berechnungen abgeschlossen sind, werden die angestauten Aktionen abgearbeitet. Mehr dazu in Abschnitt @sec:js:runtime, JavaScript Runtime.

Listing: Asynchrone Datenbankoperation in JavaScript

~~~{#lst:javascriptio .javascript}
import { createConnection } from 'mysql';
const db = createConnection(...configuration);
db.connect();
db.query('SELECT * FROM foo', function(err, rows) {
  // Do something with the result rows.
});
// Non-blocking -- do something else concurrently.
~~~

In Listing @lst:javascriptio wird die Datenbankabfrage aus dem vorhergehenden Python Listing @lst:pythonio in JavaScript umgesetzt. Im Kontrast zum Python-Beispiel blockiert hier die Datenbankoperation in Zeile 4 den Prozess nicht, wodurch es möglich ist parallel in Zeile 7ff mit dem normalen Programmablauf mit von dem Ergebnis der Datenbankabfrage unabhängigen Berechnungen fortzufahren. Sobald die Datenbankabfrage beendet ist, wird die in Zeile 4 als zweiter Parameter übergebene anonyme Funktion aufgerufen, ein sogenannter Callback. Innerhalb dieser kann dann in Zeile 5 mit dem Ergebnis gearbeitet werden. Wichtig als Unterscheidung zu Python anzumerken ist, dass die Ergebnis-Variable `rows` nur innerhalb dieser anonymen Funktion sichtbar ist; Code außerhalb dieser Funktion kann nicht auf das Ergebnis zugreifen. Auch intuitiv macht diese Sichtbarkeit (auch *scope* genannte) Sinn, da das Ergebnis ja erst zu einem zeitlich späteren Zeitpunkt verfügbar ist. Aufgrund der Funktionsweise des Event-Loops werden Operationen in Zeile 7ff noch vor solchen ausgeführt, die innerhalb der anonymen Funktion definiert sind.
