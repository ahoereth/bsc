## Daten-Aggregation {#sec:data}
Wie in Abschnitt @sec:lawly bereits angesprochen, gilt es vor Beginn der eigentlichen Implementierung die Daten, also die Gesetzestexte, zu aggregieren. Dabei wird auf die von *gesetze-im-internet.de* zur Verfügung gestellten XML-Dateien zurückgegriffen.

Ohne viel Magie wird dabei ein zweistufiger Prozess eingesetzt:

  1. Download der Rohdaten in ein temporäres Verzeichnis.
  2. Normalisieren der Daten und eintragen in die Datenbank.

Für den ersten Schritt gilt es zuerst das zur Verfügung gestellte XML-Inhaltsverzeichnis zu verarbeiten.[^code:fetch] Um mit XML-Dokumenten arbeiten zu können wird `libxml` als Parser mit XPath als Query-Sprache eingesetzt. Aus dem Inhaltsverzeichnis werden so die Links zu einzelnen Gesetzen extrahiert. Diese, zum Zeitpunkt des Verfassens, 6456 Links verweisen auf individuelle ZIP-Dateien welche ihrerseits wieder XML-Dateien beinhalten die die gemeinschaftlich ein Gesetz ergebenden Normen auflisten.

Um den *gesetze-im-internet.de*-Server nicht zu überlasten oder dazu zu verleiten Anfragen des Skriptes zu blockieren, wird maximal eine Datei pro 50 Millisekunden angefordert -- dies wurde durch über Versuche an mehreren Tagen als ein akzeptabler Wert bestimmt. Sequentiell werden geladene ZIP-Dateien in einen Buffer geladen, im Speicher entpackt und, für die weitere Verarbeitung, das enthaltene XML-Dokument in einen temporären Order auf dem System geschrieben.

Sobald alle XML-Dokumente in ihrer aktuellen Form auf dem System zwischengespeichert sind werden diese weiter verarbeitet.[^code:parse] Eine Datei wird zuerst in den Speicher eingelesen und ihr Inhalt mithilfe der `GiiParser`-Klasse[^code:parser] verarbeitet. Diese traversiert den XML-Baum wiederum mit XPath und gleicht beispielsweise Unregelmäßigkeiten in Knoten-Bezeichnungen aus um eine über sämtliche Gesetze hinweg gleichmäßige Datenstruktur zu erhalten. Die eigentlichen in den Normen enthaltenen Fließtexte werden zusätzlich von der verwendeten Auszeichnungssprache, einer Mischung aus HTML und XML, zu Markdown übersetzt -- auch hierbei steht wieder eine Normalisierung über verschiedene zum Einsatz kommende Strukturen im Vordergrund.

[^code:fetch]: [lawly_api: scripts/fetchGiiXmls.js](https://github.com/ahoereth/lawly_api/blob/bsc/scripts/fetchGiiXmls.js)

[^code:parse]: [lawly_api: scripts/parseGiiXmls.js](https://github.com/ahoereth/lawly_api/blob/bsc/scripts/parseGiiXmls.js)

[^code:parser]: [lawly_api: scripts/GiiParser.js](https://github.com/ahoereth/lawly_api/blob/bsc/scripts/GiiParser.js)

Listing: Sequentielles aggregieren der Rohdaten

~~~{#lst:data_fetch .dot}
digraph G {
    rankdir=LR
    node [shape=rect]
    List [label="list of laws"]
    TOC [label="gesetze-im-internet.de"]
    {rank=same;List TOC}
    Memory [label="law"]
    FS [label="filesystem"]
    List -> TOC [xlabel="fetch TOC & extract items" dir=backward]
    List -> Memory [label="fetch zip & unzip in memory"]
    Memory -> FS [label="write xml to temporary folder"]
    FS:n -> List:n [label="continue with next item" style=dashed]

    // Hacks
    FS:s -> List:s [style=invis]
}
~~~

Hierbei fiel die Entscheidung auf den Einsatz von Markdown, da es ein auch ohne jegliche Nachbearbeitung leicht les- und auch verfassbare Auszeichnungssprache ist. Da sie zum Beispiel keine XML-Tags beinhaltet ist es möglich auf den rohen Texten zu suchen. Außerdem ist es geplant Markdown im weiteren Entwicklungsprozess der Applikation möglichst weitflächig einzusetzen. Durch seine natürliche Struktur ist Markdown denkbar einfach für neue Anwender erlernbar und auch Vergleiche (sogenannte *diffs*) verschiedener Textversionen gut visualisierbar.

Aufgrund der schieren Menge an Normen, aktuell über 112.000, traten bei der Implementierung dieses Prozesses gleich mehrere limitierende Faktoren auf. Nicht nur kamen die für die Übersetzung eingesetzten Maschinen an ihre Grenzen, sondern auch auf Datenbank-Seite führten die rasanten Eintragungen tausender Datensätze zu einem massiven Rückstau. Um dies zu vermeiden verfolgt die aktuelle Implementierung einen streng sequentiellen Ansatz bei dem erst eine weitere Datei bearbeitet wird sobald das Ergebnis der vorhergehenden Operation erfolgreich in die Datenbank eingetragen wurde. Aktuell benötigen eine bei \ac{AWS} angemietete `t2.micro` \ac{EC2} Instanz in Verbindung mit einer gleichwertigen \ac{RDS} PostgreSQL Instanz für den gesamten Prozess unter voller Auslastung knapp eine dreiviertel Stunde.

Um diesen Prozess in Zukunft vollständig zu automatisieren ist eine zentrale Optimierung notwendig: Es muss schon vor dem eigentlichen Zugriff auf die eigene Datenbank festgestellt werden können, ob sich Gesetze geändert haben. Entweder muss dies durch die Metadaten der durch die Quelle zur Verfügung gestellten ZIP-Dateien oder am besten noch zuvor beispielsweise durch Analyse der Webseite *gesetze-im-internet.de* oder direkt des Bundesgesetzblattes geschehen. Regelmäßig alle ZIP-Dateien herunterzuladen und zu analysieren kommt nicht in Frage. Im Rahmen dieser Arbeit wurde hierfür noch keine effiziente Lösung gefunden oder gar implementiert.

[^t2micro]: Zum Stand 08/2016 werden diese durch Einkern *Intel Xeon Processors* mit 3.3GHz betrieben. Quelle: https://aws.amazon.com/ec2/instance-types/, abgerufen 08/2016.

