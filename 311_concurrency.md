### Concurrency
Bei der Interpretation von Quelltext oder auch der Ausführung von compilierten Code wird sequentiell, also Operation für Operation in der im Quelltext vorgegebenen linearen Ordnung, ausgeführt. Dabei blockiert jede einzelne Operation das fortschreiten der Ausführung bis zu ihrer vollständigen Beendigung. Werden nun I/O-Operationen genauso wie alle anderen Operationen synchron bzw. blockierend ausgeführt, können unkalkulierbare Wartezeiten entstehen: Das ausführende Programm begibt sich in komplette Abhängigkeit zu einem anderen Programm bis dieses seine Berechnungen fertiggestellt hat. Bei linearem Code ist dieses blockierende Vorgehen nicht ohne weiteres vermeidbar, da spätere Zeilen Code in der Regel auf den erfolgreichen Abschluss der Ausführung von vorhergehenden Zeilen angewiesen sind.

Bei einfachen Programmen ist diese Herangehensweise meist unproblematisch und auch anerkannt. Informatiker wird zu Beginn Ein- und Ausgabe als synchrone Operation beigebracht. Das erste Programm für angehende Programmierer ist oft vergleichbar mit dem in Quelltext-Ausschnitt @lst:javaio dargestellten Programm-Quelltext: Die Eingabe-Operation `IO.readInt()` in Zeile 4 unterbricht implizit die Programmausführung, bis die Nutzereingabe (durch einen Zeilenumbruch bzw. das einlesen des `\textbackslash n` Charakters) beendet ist. Zeile 5 kann nur ausgeführt werden, wenn Zeile 4 erfolgreich ausgeführt wurde. Dies gilt unabhängig davon, ob der weitere Verlauf des Programms von dem Ergebnis der Eingabe in Zeile 4 abhängt.

Listing: Java-Programm mit grundlegenden Ein- und Ausgabe-Operationen für Text

~~~{#lst:javaio .java}
import AlgoTools.IO;
public class HelloWorldIO {
  public static void main(String[] argv) {
    int name = IO.readInt("Name: ");
    IO.println("Hello " + name);
  }
}
~~~

Der Quelltext-Ausschnitt @lst:pythonio stellt ein etwas komplexeres und ein speziell für Webserver sehr relevantes Beispiel dar: Die Datenbankabfrage in Zeile 6 blockiert bis zu ihrer Fertigstellung die weitere Ausführung des Programmcodes. Hierbei besteht die Gefahr, dass die Anfrage längere Zeit in Anspruch nehmen könnte, falls zum Beispiel die Verbindung zur Datenbank durch schlechte Latenzzeiten Aufgrund großer geographischer Entfernung eingeschränkt wäre. Die folgenden Zeilen des Codes werden folglich erst nach Komplettierung der Anfrage ausgeführt.

Listing: Sequentielle blockierende Datenbank-Operation in Python.

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

Eine bei Webservern verbreitete Art der Umsetzung von Concurrency ist es, jede Anfrage mit Hilfe eines einzelnen Prozesses (auch *Thread*) zu beantworten. Diese Herangehensweise wird zum Beispiel vom sehr populären[^2] Apache HTTP Server umgesetzt. Jede HTTP Anfrage an den Server startet einen eigenen Prozess welcher ganz der Beantwortung dieser einen Anfrage gewidmet ist und dessen I/O-Operationen nur ihn selbst blockieren und nicht den gesamten Webserver. Bei viele gleichzeitige Verbindungen, sogenannte *concurrent connections*, ist diese Herangehensweise allerdings extrem Ressourcen hungrig: Jeder Thread benötigt eigene Arbeitsspeicher-Allokation und die bei jeder Anfrage notwendigen Kontextwechsel, also das wechseln zwischen verschiedenen aktiven Prozessen, sind Rechenintensiv.

[^2]: (Quelle: [w3techs.com/technologies/overview/web_server/all](https://w3techs.com/technologies/overview/web_server/all); Abgerufen 08/2016.])

TODO: Andere Arten von *echter* Concurrency.
