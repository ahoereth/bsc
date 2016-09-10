# Konzeptualisierung {#sec:concept}
Im folgenden Abschnitt wird der Zustand des Marktes im Allgemeinen für juristische Softwaredienstleistungen und im Speziellen für ein digitales Konkurrenzprodukt zu klassischen Gesetzbüchern analysiert. Abschnitt @sec:digitalrevolution geht dabei auf den sich im Rechtswesen generell anbahnenden digitalen Umschwung und die sich dadurch ergebende Chance und Notwendigkeit für moderne Softwarelösungen ein. Anschließend beschäftigt sich Abschnitt @sec:market mit dem konkreten traditionellen Markt für Gesetzestexte und -kommentare, bevor in Abschnitt @sec:saas der aktuelle Zustand des digitalen Marktes für solche und die in ihm bereits etablierten und aktuell aufkommenden Konkurrenzprodukte betrachtet werden. Zum Abschluss dieses Kapitels wird in Abschnitt @sec:lawly die Zielsetzung für eine neue digitale Dienstleistung in diesem Bereich dargelegt und der Rahmen des als Teil dieser Arbeit umgesetzten Softwareprojektes konkretisiert.



## Die digitale Revolution des Rechtswesens {#sec:digitalrevolution}
Für den sich anbahnenden Paradigmenwechsel hin zu einer verstärkt digitalen Arbeitsweise im Rechtswesen gibt es viele Anhaltspunkte. Im Folgenden werden exemplarisch Vorstöße von drei unterschiedlichen Akteuren in Richtung einer elektronischen rechtlichen Kommunikation aufgeführt: von Seiten des Gesetzgebers, der \ac{BRAK} und, beispielhaft an einer einzelnen, modernen Kanzleien.

Die deutsche Bundesregierung hat im letzten Jahrzehnt verstärkt Interesse gezeigt, dass moderne digitale Werkzeuge im Rechtswesen Einzug halten. Einerseits wird dies durch Gesetzesänderungen deutlich, welche den Einsatz digitaler Hilfsmittel dort legalisieren, wo er zuvor undenkbar war. Andererseits durch den Versuch, die Realisierung von geeigneten Softwarelösungen durch neue Gesetze gewissermaßen zu erzwingen.

Ein Beispiel hierfür ist unter anderem die Kommunikation im Rechtsverkehr zwischen Kanzleien und Gerichten: Bereits seit 2001 besteht das *Zustellungsreformgesetz* [@BGBL_2001_ZustRG] und seit 2005 das *Justizkommunikationsgesetz* [@BGBL_2005_JKmG]. Ersteres legte bereits sehr früh den Grundstein für kleinere Pilotprojekte zum Einsatz elektronischer Kommunikationsverfahren an einzelnen Gerichten. Das Justizkommunikationsgesetz hingegen sollte diese für die breite Masse an Juristen verfügbar machen. Durch die einerseits hohen Anforderungen an Datenschutz und Privatsphäre sowie die Notwendigkeit der Rechtsverbindlichkeit (z.B. durch digitale Signaturen) und den anderseits fehlenden bundesweiten Standards und die daraus resultierende hohe Einstiegshürde für potenzielle Nutzer hielt sich die Adoptionsrate stark in Grenzen ^[>\color{red}citation needed].

Um dem entgegen zu wirken, wurde ab 2004 vom Bundesverwaltungsgericht und dem Bundesamt für Sicherheit in der Informationstechnik das elektronische Gerichts- und Verwaltungspostfach (\acsu{EGVP}) entwickelt. Dieses sollte auf Grundlage der neuen rechtlichen Möglichkeiten erstmals einen Standard schaffen, welcher die digitale Rechtskommunikation einer breiteren Masse zur Verfügung stellt. Auch hier führten allerdings rechtliche Hindernisse wie die Notwendigkeit einer vorhergehenden individuellen Registrierung der Gerichte für das Verfahren und auch die Art der Implementierung zu Problemen. Obwohl das \ac{EGVP} als eine Standardisierung für rechtliche Kommunikation geplant war, orientiert es sich selbst nicht an technologischen Standards, sondern setzte auf proprietäre Software und zeigte starke Mängel in Bezug auf die Anwenderfreundlichkeit [@10PunkteAkzeptanz].

Erst 2013 folgte mit dem *Gesetz zur Förderung des elektronischen Rechtsverkehrs mit den Gerichten* [@BGBL_2013_FördElRV] der nächste Vorstoß: Der Gesetzgeber verpflichtete hierin die \ac{BRAK} zur Einrichtung des sogenannten *besonderen elektronischen Anwaltspostfaches* (\acs{beA}) für jeden in Deutschland zugelassenen Rechtsanwalt. Das \acs{beA} soll im Großen und Ganzen nichts anderes zur Verfügung stellen als verschlüsselte E-Mail-Kommunikation zwischen Kanzleien und Gerichten. Geplagt von Problemen wurde das gesetzlich festgelegte Ziel die Plattform bis zum 01.01.2016 fertigzustellen wegen "nicht ausreichender Qualität" der Software zuerst verfehlt [@BRAK_beAkommtSpaeter] und dann, kurz vor der für 10 Monate später angesetzten Fertigstellung im zweiten Anlauf [@BRAK_beAStart], durch ein einstweiliges Verfahren erneut gestoppt: Zwei Rechtsanwälte hatten beantragt, dass ihr \ac{beA} nur mit ihrer ausdrücklichen Zustimmung freigeschaltet werde. Laut \ac{BRAK} ist diese individuelle Freischaltung allerdings technisch nicht möglich, womit sich die Einrichtung des \acp{beA} weiter verzögert [@BRAK_beAVerfahren].

Obwohl der Werdegang des \acp{beA} nicht unproblematisch ist, zeigt es zusätzlich eine andere Seite: Das Interesse an der Umsetzung des \ac{beA}s geht klar auch von der \ac{BRAK} und damit den Rechtsanwälten aus. Schon vor dem Beginn der Entwicklung des Postfaches bemühte sich die \ac{BRAK} um eine Stärkung der Akzeptanz des elektronischen Rechtsverkehrs -- mit vielversprechenden Hinweisen auf die Zielsetzung des Postfaches als eine benutzerfreundliche, an bereits etablierten Standards orientierte Plattform [@BRAK2008_Akzeptanz]. Diese Forderungen galten zu Beginn noch einer Weiterentwicklung des \ac{EGVP}, resultierten endgültig aber in der Entwicklung des \ac{beA}.

Ein dritter Akteur, welcher eine wichtige Rolle bei einem solchen Paradigmenwechsel hin zu einer verstärkt elektronischen Kommunikation im Rechtswesen spielt, sind die Kanzleien. Obwohl sie ein immenses wirtschaftliches Interesse an einer breiten Verfügbarkeit des elektronischen Rechtsverkehrs haben, sind sie an seiner Realisierung primär durch die \ac{BRAK} beteiligt. Kanzleiintern hingegen kann die elektronische Kommunikation von ihnen selbstständig umgesetzt werden. Aus persönlichen Unterhaltungen mit Rechtsanwälten der multinational agierenden Kanzlei *Osborne Clarke* hat sich ergeben, dass der Einsatz moderner Hilfsmittel zur Kommunikation bei vielen Kanzleien nicht bei E-Mails stehen geblieben ist. Vielfach wird auch schon, ähnlich zu modernen Technologieunternehmen, auf erst in den letzten Jahren aufgekommene Kommunikationsplattformen wie *Slack* gesetzt. Dies deutet auf einen immensen Innovationswillen hin -- solange die Innovation mit einer Effizienzsteigerung einhergeht.



## Gesetzbücher und -kommentare {#sec:market}
Neben der weiterhin fast ausschließlich papiergestützten rechtlichen Kommunikation stechen besonders die *roten Bücher*, offiziell *Schönfelder -- Deutsche Gesetze*, des Beck-Verlages ins Auge: ^[>So schwer, dass es zentral mit ausklappbarem Aufsteller vermarktet wird.] Mit einer Masse von fast 2,5 Kilogramm gilt es als das Standardwerk des deutschen Rechtswesens. Da das deutsche Recht kein stehendes Konstrukt ist, sondern laufend Änderungen unterliegt, erscheinen drei bis vier Mal jährlich sogenannte *Ergänzungslieferungen*: Nach dem kostenpflichtigen Erwerb gilt es, diese in das als Loseblattsammlung konzipierte Ursprungswerk in Kleinstarbeit manuell einzusortieren. Dabei ist der Schönfelder nur eines von vielen ähnlich umfassenden und auf aktuellem Stand zu haltenden Werken. Aufgrund der Notwendigkeit dieser regelmäßigen Aktualisierung bewirbt der Beck Verlag die von ihm vertriebenen Gesetzessammlungen primär in Kombination mit Abonnements des hauseigenen *Aktualisierungsservices*.[^schoenfeldershop] Zu Marketingzwecken empfiehlt der Verlag angehenden Juristen mit dieser und ähnlichen Gesetzessammlungen "einen Bund fürs Leben zu schließen [...] ^[>Zitat gekürzt, weil zu abstrus.] und die Beziehung als Freundschaft mittels Kommunikation und Interesse aufrecht und lebendig zu gestalten".[^buecherliebe]

Die Zielgruppe für diesen Kassenschlager ist schlichtweg jeder, der mit dem Rechtswesen zu tun hat: das sind bundesweit ca. 165.000 aktive Rechtsanwälte [@BRAK_Mitglieder_2015], über 25.000 Richter und Staatsanwälte im öffentlichen Dienst [@BFJ_ZahlRichterStaatsanwaelte] und über 70.000 weitere Juristen, welche anderweitige juristische Tätigkeiten im öffentlichen Dienst und der freien Wirtschaft ausüben (vergleiche Abbildung @fig:juristischeberufe aus @BFA_2012_Chancen<!--, s. 76-->). Außerdem gibt es aktuell über 100.000 Jurastudenten [@Wissenschaftsrat2012]<!--, s. 80-->. In all diesen Bereichen ist die Tendenz weiterhin steigend [@BFA_2012_Chancen]<!--, s. 75-78-->.

^[>\color{red} Long and short caption?]

![Erwerbstätige mit juristischer Ausbildung](assets/berufschancen_rechtswissenschaften.png){#fig:juristischeberufe}

Beispielhaft ergeben sich aus diesen Zahlen alleine durch die von Land und Bund beschäftigten Richter und Anwälte jährliche Kosten von über 1 Millionen Euro für den öffentlichen Dienst. Dabei ist wichtig zu bemerken, dass die für diese Schätzung angenommenen Werte mit pro Jurist einer Gesetzessammlung mit je drei Ergänzungslieferungen pro Jahr zu je 15 € niedrig angesetzt sind.[^ergaenzungshop] Ausübende Juristen sind meist auf drei oder mehr solcher Werke angewiesen.^[>\color{red} Citation needed]

Da die eigentlichen Normen eines Gesetzes, um möglichst viele Alltagssituationen abzudecken, meist abstrakt gehalten sind, ist ihre Auslegung für Juristen oft schwierig. Um diesem Problem entgegen zu wirken, haben sich bereits früh sogenannte Gesetzeskommentare etabliert und nehmen großen Einfluss auf das Rechtswesen [@Henne2006]. Sie beschäftigen sich mit der Erläuterung und Interpretation der eigentlichen Gesetze in Bezug auf konkrete Gegebenheiten und verwenden gerichtliche Entscheidungen und dem Gesetz vorhergegangene Regierungsentwürfe als Referenzen. In ihrem Umfang übersteigen diese meist die Gesetze, zu welchen sie Stellung beziehen, und sind für kaum einen Juristen vernachlässigbar [@Spiegel1981].

[^buecherliebe]: Quelle: Artikel im Beck Blog, *Das Leben mit Loseblattwerken – eine erfüllte Liebesbeziehung*, [blog.beck-shop.de/?p=18760](http://blog.beck-shop.de/wirtschaft/leben-mit-loseblattwerken/), abgerufen 01/2016.

[^schoenfeldershop]: Quelle: *Schönfelder* im Beck Shop, [beck-shop.de/productview.aspx?product=2205](http://beck-shop.de/Schoenfelder-Deutsche-Gesetze/productview.aspx?product=2205), abgerufen 01/2016.

[^ergaenzungshop]: Quelle: Verschiedene *Ergänzungslieferungen* gelistet im Beck Shop, z.B. Stand 08/2016, [beck-shop.de/productview.aspx?product=16454788](http://www.beck-shop.de/Schoenfelder-Deutsche-Gesetze-165-Ergaenzungslieferung-Stand-08-2016/productview.aspx?product=16454788), abgerufen 08/2016.



## Gesetzestext -- Open Data? {#sec:resources}
Die rechtliche Grundlage für die freie Verwendung von Gesetzen ist durch das deutsche Urheberrecht gegeben. Die so geartete Rechtslage wurde im Rahmen dieses Projektes auch anwaltlich, speziell in Bezug auf eine eventuell auch kommerzielle Nutzung, bestätigt. Gleiches gilt auch für Rechtsprechungen durch öffentliche Gerichte.

> Gesetze, Verordnungen, amtliche Erlasse und Bekanntmachungen sowie Entscheidungen und amtlich verfaßte Leitsätze zu Entscheidungen genießen keinen urheberrechtlichen Schutz.
>
> --- Urheberrechtsgesetz (UrhG), § 5, Satz 1

Wo sich die Gesetzgebung auf den ersten Blick ganz im Sinne von Open Data und Creative Commons erst einmal hervorragend anhört, erweist sie sich auf den zweiten als nur unzureichend umgesetzt: Obwohl Gesetze und Urteile rechtlich frei von Urheberrechten sind, ist es nicht möglich, diese ohne Umweg über private Anbieter mit eigenen wirtschaftlichen Interessen zu beziehen.

Als optimale Quelle würde man initial das vom \ac{BMJV} herausgegebene \ac{BGBL} ^[>\color{red} Line break! watch out.]annehmen. Es dient der verpflichtenden Verkündung aller Bundesgesetze, welche erst durch eben diese Veröffentlichung in Kraft treten können (Grundgesetz, Artikel 82). Zwar ist das \ac{BMJV} Herausgeber des \ac{BGBL}, allerdings wird der Vertrieb durch die 2006 vollständig privatisierte *Bundesanzeiger Verlag GmbH* vertrieben.[^privatanzeiger] Durch einen kostenpflichtigen Abonnentenzugang und den Vertrieb der Papierversion verdient der Verlag an dem Blatt. Die freie Weiterverwendung der veröffentlichten Gesetze schränkt der Verlag einmal im kostenlos zugänglichen *Bürgerzugang* durch technische Mittel[^saferpdf] und im *Abonnentenzugang* mutmaßlich durch seine AGB[^noopendata] ein. Eine Klärung der Tragweite der AGB und der Rechtmäßigkeit solcher Einschränkungen würde einen größeren, dem Umfang dieser Arbeit unangemessenen, rechtlichen Aufwand mit sich bringen.

Die zweite eng mit dem Bund verknüpfte mutmaßlich freie Quelle für Gesetze ist die Webseite *gesetze-im-internet.de*. Von der Juris GmbH betrieben, an welcher der Bund $50,1 \%$ Anteile hält, gibt es hier die Möglichkeit die aktuelle Version der Gesetze einzusehen. Zusätzlich werden alle Gesetze auch im maschinell besser konsumierbaren XML-Dateiformat zur Verfügung gestellt. In Rücksprache mit dem \ac{BMJV} wurde zu diesen Daten bestätigt, dass sie vollständig für die Weiterverwendung durch Dritte auch für gegebenenfalls kommerzielle Unterfangen freigegeben sind. Auch hierbei ist wiederum als problematisch zu betrachten, dass die Juris GmbH ein wirtschaftliches Unternehmen ist und so zum Beispiel für den Zugriff auf überholte Versionen der Gesetzestexte ein Abonnement (mit ungewissen Einschränkungen) notwendig ist. Allerdings: Für das konkrete Ziel dieser Arbeit sind über *gesetze-im-internet.de* alle notwendigen Daten verfügbar.

Ähnlich ist die Situation bei eigentlich laut Gesetz urheberrechtsfreien Gerichtsentscheidungen. Zwar sind diese nicht für das konkrete Ziel der im Rahmen dieser Arbeit entwickelten Software notwendig, wären aber ein erster Schnittpunkt für eine mögliche Erweiterung. Das \ac{BMJV} stellt auch hier zumindest "ausgewählte Entscheidungen des Bundesverfassungsgerichts, der obersten Gerichtshöfe des Bundes sowie des Bundespatentgerichts"^[>\color{red}quote right away] in Zusammenarbeit mit der Juris GmbH zur privaten und kommerziellen Nutzung im Internet bereit.[^RII] Dies ist allerdings ein Novum. Für Rechtsprechungen anderer Gerichte ist es notwendig im Einzelfall zu klären wie das Gericht die Veröffentlichung und die Möglichkeiten der Weiterverwendung zum Beispiel in Form einer Wiederveröffentlichung kommerziell sowie nicht kommerziell handhabt.^[>\color{red}More citations needed.] Viele Gerichte setzen hierbei auf eine Art Freemium-Modell, bei welchem die kostenlose Nutzung für Privatpersonen möglich ist. Für die Weiterverwendung werden jedoch individuelle Absprachen bis hin zu einer Gebühr pro Entscheidung nötig. Vielversprechend hierbei ist allerdings, dass viele Gerichte eine freie umfängliche Nutzung in Aussicht stellen, wenn "Entscheidungen für Zwecke abgerufen werden, deren Verfolgung überwiegend im öffentlichen Interesse"^[>\color{red}quote right away] liegt.[^nrwrechtsprechungen]

Hierbei kritisch, aber in den letzten Jahren rechtlich ins Wanken gekommen, sind exklusive Vereinbarungen von Bund und Gerichten mit privaten Anbietern. So ist nicht nur die Verbindung des Bundes zur Juris GmbH als direkter Teilhaber zu sehen, sondern auch, dass zwischen beiden lange Zeit beispielhafte Verträge über eine exklusive Belieferung mit aufbereiteten Urteilen bestand [@LexxpressJuris2013]. Diesbezüglich gibt es dem folgenden Zitat wenig hinzuzufügen:

> Es gibt keinen Grund für den Staat sich auf diesem Gebiet wirtschaftlich zu betätigen. Er sollte Rechtsnormen und Urteile, die nicht dem Urheberrecht unterliegen, von einer gemeinnützigen Organisation digitalisieren lassen und jedermann kostenlos zur Verfügung stellen.
>
> --- Markus Reithwiesner, Geschäftsführer Rudolf-Haufe-Verlag [@FAZ2009]


[^privatanzeiger]: Der Spiegel: M. DuMont Schauberg Verlag schluckt Bundesanzeiger (2006), [spiegel.de/kultur/gesellschaft/a-448095.html](http://www.spiegel.de/kultur/gesellschaft/m-dumont-schauberg-koelner-verlag-schluckt-bundesanzeiger-a-448095.html), abgerufen 08/2016.

[^noopendata]: Quelle: [bgbl.de](http://www1.bgbl.de/fileadmin/Betrifft-Recht/Dokumente/BGBl/bgbl_agb_online.pdf), abgerufen 08/2016.

[^saferpdf]: Ausschnitt aus *Fragen & Antworten* von [bgbl.de](http://www1.bgbl.de/fragen-antworten/fragen-antworten.html#c46073), abgerufen 08/2016:

    > Wie dürfen die Daten aus BGBl. Online weiterverwendet werden?
    >
    > Die Version im Bürgerzugang ist gegen Weiterverarbeitung geschützt. Die entgeltliche Version ermöglicht es Ihnen, Textausschnitte zu markieren und mittels „copy & paste“ in andere Programme einzufügen und entsprechend unserer AGB [...] für das Online-Abonnement weiter zu verarbeiten.

[^RII]: Quelle und Zitat: [rechtsprechung-im-internet.de](https://www.rechtsprechung-im-internet.de), abgerufen 08/2016

[^nrwrechtsprechungen]: Beispiel einer solchen Regelung in NRW und Zitat von: [justiz.nrw.de/BS/nrwe2/gewerbl_nutzer/index.php](https://www.justiz.nrw.de/BS/nrwe2/gewerbl_nutzer/index.php), abgerufen 08/2016

---
# \nocite{UrhG} hack.
# See: http://pandoc.org/MANUAL.html#citations
nocite: |
  @UrhG
  @Grundgesetz
---




## Software-as-a-Service {#sec:saas}
Der Markt für elektronische Rechtsinformationen wird, ähnlich dem Markt für traditionelle Formate, von wenigen Akteuren dominiert. Zusätzlich liegt eine starke Überschneidung zwischen den großen Anbieter im digitalen und den traditionellen Verlagen im analogen Bereich vor. Dies resultiert daraus, dass die meisten Anbieter auf die Verbindung von Gesetzestexten mit den in ihrem Verlagsrepertoire befindlichen ergänzenden Werken wie Gesetzeskommentare setzen. Neben der Erweiterung des Angebots um verlagseigene und eingekaufte Gesetzeskommentare wird stark auf die direkte Verknüpfung von Gesetzen zu Rechtsprechungen gesetzt.

Als Zielgruppe haben diese Systeme allesamt professionelle Anwender, welche zur Zahlung der teils immensen Gebühren gewillt sind. So kostet beispielsweise der Bezug des gesamten deutschen Bundesrechtes, welches, wie in Abschnitt @sec:resources beschrieben, urheberrechtsfrei ist, 40 € pro Anwender monatlich -- ohne jegliche ergänzende Literatur [@Beck2011]<!--, s. 13-->.

Dabei mangelt es den bestehenden Anbietern stark an digitaler Innovation. So bieten sie beispielsweise keine umfassenden Mobillösungen an -- außer einigen Nischenprodukten sind die elektronischen Rechtsinformationssysteme allesamt schwergewichtige Webseiten. An diesem Punkt setzt dieses Projekt an: Lawly, so der Name, verfolgt das Ziel einer modernen mobilen und insbesondere auch vollständig offenen Lösung.



## Lawly -- Freies Recht {#sec:lawly}
Als initiales Produkt wird eine Plattform zur interaktiven Navigation deutscher Bundesgesetzen entwickelt. In einem zweiten Schritt soll diese um Verknüpfungen mit Rechtsprechungen erweitert werden.

Zentrale Aspekte der Plattform sind Open Data und Open Source. Der verfolgte Ansatz ist hierbei vielschichtig. Es gilt, komplett auf frei verfügbare Daten (Open Data) aufzubauen und diese mit Hilfe von frei verfügbaren Technologien (Open Source) aufzubereiten. Damit geht auch einher, dass die Entwicklung der Plattform selbst offen gestaltet wird sowie auch freie Schnittstellen zu den aufbereiteten Daten zur Verfügung stellt und somit zu der Open Access Bewegung beiträgt. So soll sie zum Start nicht nur als Plattform, sondern auch im Quelltext offen sein und im Idealfall Dritte in die Entwicklung einbinden. Neben solchen ideellen Ansätzen gilt es zusätzlich, konkrete für den Endnutzer spürbare Alleinstellungsmerkmale gegenüber bestehenden Angeboten zu schaffen.

Hierbei steht im Vordergrund, dass aktuelle digitale Anbieter auf traditionelle Webseiten setzen. Daraus ergeben sich starke Einschränkungen für die Benutzererfahrung: Die Handhabung von Informationsmengen, wie sie bei juristischen Informationen vorliegen, muss interaktiv gestaltet sein. Unterbrechungen durch Ladezeiten, die beispielsweise beim Wechsel zwischen einzelnen Normen, dem Aufruf verknüpfter Rechtsprechungen oder dem Durchsuchen der verfügbaren Daten entstehen, stören den Interaktionsfluss.

Zusätzlich spielt Portabilität heutzutage eine immer größere Rolle. Webseiten bestehender Anbieter sind zur Verwendung an eine bestehende und zuverlässige Internetverbindung gebunden. Genauso wie traditionelle Buchformate, welche aufgrund ihrer Größe und Masse nur schwer portabel sind, kommen diese somit nicht für den mobilen Einsatz infrage.

Es gilt also die Vorteile bestehender digitaler Angebote, also Aktualität und Umfang der Inhalte, mit modernen Ansätzen der Portabilität zu verbinden. Um dies zu erreichen, verfolgt der praktische Aspekt dieser Arbeit zwei Phasen.

Zu Beginn muss die Akkumulation der Bundesgesetze von *gesetze-im-internet.de* in zumindest teil-automatisierter Form umgesetzt werden. Hierbei gilt es, die rohen XML-Daten abzugreifen, in ein einheitliches leichter zu verarbeitendes Format zu übersetzen und in die eigene Datenbank einzuspeisen. Außerhalb dieser Arbeit ist es nötig, einen vollständig automatisierten Prozess zu entwickeln, welcher die bei diesem Vorgang gesammelten Datensätze auf ähnlichem Weg tagesaktuell erneuert.

Sobald der Datensatz akkumuliert wurde, wird auf dessen Grundlage eine Applikation entwickelt, welche auf einer möglichst großen Auswahl an Geräten mit gleichermaßen vollem Funktionsumfang einsetzbar ist. Dabei ist es wichtig ein Nutzungserlebnis zu ermöglichen, welches dem eines für eine Plattform nativ entwickelten Programms möglichst gleichkommt. Dies spiegelt sich nicht nur in der allgemeinen Performance der Applikation wieder, sondern auch in der Möglichkeit zentrale Teile der Applikation ohne bestehende oder mit nur unzuverlässiger Internetverbindung nutzen zu können. So sollen zum Beispiel die Gesamtübersicht und insbesondere die vom Nutzer zuvor abgerufenen oder für die weitere Verwendung explizit vorgemerkten Gesetze immer verfügbar sein. Zusätzlich müssen diese Daten gleichermaßen online als auch offline durchsuchbar sein.

Obwohl sich die im Rahmen dieser Arbeit entwickelte Software auf eine Webapplikation zum interaktiven Navigieren deutscher Bundesgesetze beschränkt, wird bei der Implementierung und den ihr vorhergehenden technischen Entscheidungen vorausschauend geplant: Neben der Integration von Rechtsprechungen wird auch die Möglichkeit der Erweiterung um native Applikationen für iOS- und Android-Geräte bedacht. In persönlichen Gesprächen hat sich insbesondere für eine native iPad-Anwendung bei professionellen Anwendern großes Interesse gezeigt.

Neben den oben benannten technischen Anforderungen soll die initiale Plattform für den Nutzer die folgenden konkreten Ansichten und Funktionen bieten:

  * Eine Gesetzesübersicht, welche nach vordefinierten Sammlung (zum Beispiel von traditionellen Büchern bekannte zusammenstellungen oder Themengebiete), Kürzeln und Bezeichnungen filterbar ist.
  * Eine Ansicht, auf welcher individuelle Gesetze in ihrem gesamten Umfang betrachtet und mithilfe einer Inhaltsübersicht navigiert werden können.
  * Eine Volltextsuche, die sowohl online als auch offline während der Eingabe in Echtzeit Ergebnisse liefert.
  * Die Möglichkeit sich als Nutzer zu registrieren, Gesetze zu speichern und diese auch ohne Internetverbindung zu betrachten und zu durchsuchen.

\begin{figure}[H]
  \subfloat[Startseite]{
    \tikz\node[blur shadow={shadow blur steps=5}, style={inner sep=0, outer sep=0}]{
      \includegraphics[width=0.5\textwidth, frame]{assets/home.png}
    };
    \label{fig:appoverviewHome}
  }
  \subfloat[Gesetzesübersicht]{
    \tikz\node[blur shadow={shadow blur steps=5}, style={inner sep=0, outer sep=0}]{
      \includegraphics[width=0.5\textwidth, frame]{assets/lawindex_phone.png}
    };
    \label{fig:appoverviewIndex}
  }

  \subfloat[Gesetzesansicht]{
    \tikz\node[blur shadow={shadow blur steps=5}, style={inner sep=0, outer sep=0}]{
      \includegraphics[width=0.5\textwidth, frame]{assets/urhg_horizontal.png}
    };
    \label{fig:appoverviewLaw}
  }
  \subfloat[Volltextsuche]{
    \tikz\node[blur shadow={shadow blur steps=5}, style={inner sep=0, outer sep=0}]{
      \includegraphics[width=0.5\textwidth, frame]{assets/search.png}
    };
    \label{fig:appoverviewSearch}
  }

  \caption{Vorschau der zentralen Ansichten der Applikation (Smartphone, horizontal)}
  \label{fig:appoverview}
\end{figure}
