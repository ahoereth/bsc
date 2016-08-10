### Concurrency & Event-Loop 

#### Problemstellung
Bei der Interpretation von Quelltext oder auch der Ausführung von compilierten Code wird sequentiell, also Operation für Operation in der im Quelltext vorgegebenen linearen Ordnung, ausgeführt. Dabei blockiert jede einzelne Operation das fortschreiten der Ausführung bis zu ihrer vollständigen Beendigung. Werden nun I/O-Operationen genauso wie alle anderen Operationen synchron bzw. blockierend ausgeführt, können unkalkulierbare Wartezeiten entstehen: Das ausführende Programm begibt sich in komplette Abhängigkeit zu einem anderen Programm bis dieses seine Berechnungen fertiggestellt hat. Bei linearem Code ist dieses blockierende Vorgehen nicht ohne weiteres vermeidbar, da spätere Zeilen Code in der Regel auf den erfolgreichen Abschluss der Ausführung von vorhergehenden Zeilen angewiesen sind.

Bei einfachen Programmen ist diese Herangehensweise meist unproblematisch und auch anerkannt. Informatiker wird zu Beginn Ein- und Ausgabe als synchrone Operation beigebracht. Das erste Programm für angehende Programmierer ist oft vergleichbar mit dem in Quelltext-Ausschnitt @lst:javaio dargestellten Programm-Quelltext: Die Eingabe-Operation `IO.readInt()` in Zeile 6 unterbricht implizit die Programmausführung, bis die Nutzereingabe (durch einen Zeilenumbruch bzw. das einlesen des `\textbackslash n` Charakters) beendet ist. Zeile 7 kann nur ausgeführt werden, wenn Zeile 5 erfolgreich ausgeführt wurde. Dies gilt unabhängig davon, ob der weitere Verlauf des Programms von dem Ergebnis der Eingabe in Zeile 5 abhängt.

Listing: Java-Programm mit Text Ein- und Ausgabe-Operationen

~~~{#lst:javaio .java}
import java.util.Scanner;
public class JavaIO {
  public static void main(String[] argv) {
    Scanner in = new Scanner(System.in);
    System.out.print("Your name: ");
    String name = in.nextLine();
    System.out.println("Hello " + name);
  }
}
~~~

Der Quelltext-Ausschnitt @lst:pythonio stellt ein etwas komplexeres und ein speziell für Webserver sehr relevantes Beispiel dar: Die Datenbankabfrage in Zeile 6 blockiert bis zu ihrer Fertigstellung die weitere Ausführung des Programmcodes. Hierbei besteht die Gefahr, dass die Anfrage längere Zeit in Anspruch nehmen könnte, falls zum Beispiel die Verbindung zur Datenbank durch schlechte Latenzzeiten Aufgrund großer geographischer Entfernung eingeschränkt wäre. Die folgenden Zeilen des Codes werden folglich erst nach Komplettierung der Anfrage ausgeführt.

Listing: Sequentielle blockierende Datenbank-Operation in Python

~~~{#lst:pythonio .python}
import mysql
db = mysql.connector.connect(*configuration)

try:
  cursor = db.cursor()
  cursor.execute('SELECT * FROM foo')
  # Blocking -- wait for result.
  rows = cursor.fetchAll()
  # Do something with the result rows.
except mysql.connector.Error as e:
  raise e
~~~

Obwohl rein sequentieller Code für Programmierer sehr komfortabel und leicht verständlich ist, ist diese Herangehensweise bei Programmen welche mit vielen Anfragen zu tun haben problematisch. Insbesondere bei Webservern sind solche blockierende Operationen unakzeptabel, da in dieser Zeit durch den blockierten Prozess keine anderen Anfragen beantwortet werden können.

Die Lösung für dieses Problem liegt darin, Code nicht immer sequentiell, sondern, wenn angebracht, gegebenenfalls nichtsequentiell auszuführen. Dieses Konzept nennt sich Nebenläufigkeit bzw. Concurrency.

Concurrency
  : *Nebenläufigkeit*, *Parallelität*
  : Eigenschaft eines Systems, mehrere Berechnungen, Anweisungen oder Befehle gleichzeitig ausführen zu können. Es kann sich dabei um völlig unabhängige Anweisungen handeln, bis hin zur gemeinsamen Bearbeitung einer Aufgabe.[^1]

[^1]: Quelle: [de.wikipedia.org/wiki/Nebenläufigkeit](https://de.wikipedia.org/wiki/Nebenl%C3%A4ufigkeit)


#### Echte Nebenläufigkeit
Eine bei Webservern verbreitete Art der Umsetzung von Concurrency ist es, jede Anfrage mit Hilfe eines einzelnen Prozesses (auch *Thread*) zu beantworten. Diese Herangehensweise wird zum Beispiel vom sehr populären[^2] Apache HTTP Server umgesetzt. Jede HTTP Anfrage an den Server startet einen eigenen Prozess welcher ganz der Beantwortung dieser einen Anfrage gewidmet ist und dessen I/O-Operationen nur ihn selbst blockieren und nicht den gesamten Webserver. Bei viele gleichzeitige Verbindungen, sogenannte *concurrent connections*, ist diese Herangehensweise allerdings extrem Ressourcen hungrig: Jeder Thread benötigt eigene Arbeitsspeicher-Allokation und die bei jeder Anfrage notwendigen Kontextwechsel, also das wechseln zwischen verschiedenen aktiven Prozessen, sind Rechenintensiv.

[^2]: Quelle: [w3techs.com/technologies/overview/web_server/all](https://w3techs.com/technologies/overview/web_server/all); Abgerufen 08/2016.]

TODO: Andere Arten von *echter* Concurrency.

#### Event-Loop
Eine alternative Herangehensweise ist die Verwendung eines Event-Loops.  

In Quelltext @lst:javascriptio wird die Datenbankabfrage aus dem vorhergehenden Python-Quelltext @lst:pythonio in JavaScript umgesetzt. Im Unterschied zum Python-Beispiel blockiert die Datenbankabfrage den Prozess nicht. Dadurch ist es möglich nachdem die Datenbankoperation in Zeile 5 gestartet wurde, ab Zeile 9 mit dem normalen Programmablauf fortzufahren und andere Berechnungen anzustellen. Sobald die Datenbankabfrage beendet ist wird die übergebene Callback-Funktion aufgerufen, welche sich dann innerhalb der anonymen Funktion in Zeile 6 und 7 mit der Handhabung des Ergebnisses beschäftigen kann. Die Ergebnis-Variable `rows` ist nur innerhalb der anonymen Funktion sichtbar. Aufgrund der Funktionsweise des EventlLoops wird der Code ab Zeile 9 noch vor dem innerhalb der anonymen Funktion aufgerufen.

Listing: Nicht-blockierende Datenbank-Operation in JavaScript

~~~{#lst:javascriptio .javascript}
import mysql from 'mysql';
const db = mysql.createConnection(...configuration);
db.connect();

connection.query('SELECT * FROM foo', (err, rows) => {
  if (err) { throw err; }
  // Do something with the result rows.
});

// Non-blocking -- do something else concurrently.
// Result `rows` is not available here.
~~~

