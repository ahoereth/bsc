## Daten-Aggregation
Wie in Abschnitt @sec:lawly bereits angekündigt, gilt es, vor Beginn der eigentlichen Implementierung die Daten, also die Gesetzestexte, zu aggregieren. Dabei wird auf die von *gesetze-im-internet.de* zur Verfügung gestellten XML-Dateien zurückgegriffen.

Ohne viel Magie wird dabei ein zweistufiger Prozess eingesetzt:

  1. Download der Rohdaten in ein temporäres Verzeichnis
  2. Normalisieren der Daten und eintragen in der Datenbank

Für Schritt 1 gilt es zuerst das direkt als XML-Text zur Verfügung gestellte Inhaltsverzeichnis zu verarbeiten. Um mit solchen rohen XML-Dokumenten arbeiten zu können wird libxml als Parser und die XPath als Query-Sprache eingesetzt. Aus dem Inhaltsverzeichnis werden alle Links zu einzelnen Gesetzen extrahiert. Diese, zum Zeitpunkt des Verfassens, 6456 Links verweisen auf ZIP Dokumente welche ihrerseits wieder XML-Dateien enthalten welche jeweils die für ein Gesetz notwendigen Normen auflisten.

Um den \ac{GII}-Server nicht zu überlasten oder dazu zu verleiten Anfragen des Skriptes zu blockieren, wird im folgenden nur eine Datei pro 50 Millisekunden angefordert. Die geladene Datei wird in einen Buffer geladen, entpackt und, für die weitere Verarbeitung, das enthaltene XML-Dokument in einen temporären Order auf dem System geschrieben.

Sobald alle XML-Dokumente in ihrer aktuellen Form auf dem System zwischen gespeichert sind, werden diese sequentiell weiter verarbeitet. Eine Datei wird zuerst in den Speicher eingelesen und ihr Inhalt mithilfe der `GiiParser`-Klasse verarbeitet. Diese verarbeitet den XML-Baum und gleicht zum Beispiel unnötige Unregelmäßigkeiten in Knoten-Bezeichnungen aus um eine über alle Normen hinweg gleichmäßige Datenstruktur zu erhalten. Der Text individueller Normen wird zusätzlich von der verwendeten Auszeichnungssprache, einer Mischung aus HTML und XML, zu Markdown übersetzt -- auch hierbei steht wieder eine Normalisierung über verschiedene zum Einsatz kommende Strukturen im Vordergrund.

Listing: Sequentielles aggregieren der Rohdaten

~~~{#lst:data_fetch .dot}
digraph G {
    rankdir=LR
    node [shape=rect]
    TOC [label="GII.de"]
    List [label="list of laws"]
    Memory [label="law"]
    FS [label="filesystem"]
    TOC -> List [label="fetch TOC & \n extract items \n"]
    List -> Memory [label="fetch zip & \n unzip in memory \n"]
    Memory -> FS [label="write xml to temporary folder \n"]
    FS:n -> List:n [label="continue with next item" style=dashed]

    // Hacks
    FS:s -> List:s [style=invis]
}
~~~

Außerdem ist es geplant, Markdown im weiteren Entwicklungsprozess der Applikation möglichst weitflächig einzusetzen. Durch seine natürliche Struktur ist Markdown denkbar einfach für neue Anwender erlernbar und auch Vergleiche (sogenannte *diffs*) verschiedener Textversionen gut visualisierbar.^[>\color{red}Why markdown?]

<!-- Listing: Sequentielles normalisieren von Gesetzen

~~~{#lst:data_process .dot}
digraph G {
    rankdir=LR
    node [shape=rect]
}
~~~ -->

Aufgrund der schieren Menge an Normen, aktuell über 112.000, traten bei der Implementierung dieses Prozesses gleich mehrere limitierende Faktoren auf. Nicht nur kam die für die Übersetzung eingesetzten Maschinen an ihre Grenzen, sondern auch auf Datenbank-Seite führten die rasanten Eintragungen tausender Datensätze zu einem massiven Rückstau. Um dies zu vermeiden verfolgt die aktuelle Implementierung einen streng sequentiellen Ansatz, bei welchem erst eine weitere Datei bearbeitet wird, sobald das Ergebnis der vorhergehenden Operation erfolgreich in die Datenbank eingetragen wurde. Aktuell benötigen eine \ac{AWS} `t2.micro` \ac{EC2} Instanz in Verbindung mit einer gleichwertigen \ac{RDS} PostgreSQL Instanz für den gesamten Prozess unter voller Auslastung knapp eine dreiviertel Stunde.

Von der vollständigen Automatisierung und regelmäßigen automatischen Ausführung dieses Prozesses wurde so bisher abgesehen, mehr dazu in Abschnitt @sec:discussion.

