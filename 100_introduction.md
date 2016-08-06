# Einleitung
\label{sec:introduction}

**Lawly ^[Arbeitstitel] gibt Juristen moderne Mittel an die Hand.**

Das Rechtswesen ist seit jeher ein eher konservativer Bereich und tut sich in seiner Gesamtheit schwer aus alten Mustern auszubrechen. Trotz mehrerer zögerlicher Vorstöße ins digitale Zeitalter findet ein großer Teil der Arbeit in Kanzleien und an Gerichten weiterhin analog statt (vrgl. Kapitel \ref{sec:digitalrevolution}, \textit{Die digitale Revolution des Rechtswesens}).

Neben der weiterhin fast ausschließlich papiergestützten offiziellen rechtlichen Kommunikation stechen besonders die *roten Bücher*, offiziell *Schönfelder -- Deutsche Gesetze*, des Beck Verlages ins Auge: \marginpar{So schwer, dass es über einen ausklappbaren Aufsteller verfügt.} Mit seinen fast 2,5 Kilogramm Masse gilt es als das Standardwerk des deutschen Rechtswesens. Da das deutsche Recht kein stehendes Konstrukt ist, sondern laufend Änderungen unterliegt, erscheinen drei bis vier mal im Jahr sogenannte *Ergänzungslieferungen*: Nach der kostenpflichtigen Erwerbung gilt es, diese in das als Loseblattsammlung konzipierte Ursprungswerk in Kleinstarbeit manuell einzusortieren. Auf Grund dieser Notwendigkeit werden solche Gesetzessammlungen vom Beck Verlag primär in Kombination mit Abonnements des hauseigenen *Aktualisierungsservices* beworben. ^[Quelle: [beck-shop.de/productview.aspx?product=2205](http://beck-shop.de/Schoenfelder-Deutsche-Gesetze/productview.aspx?product=2205), Abgerufen 01/2016]. Zu marketingtechnischen Zwecken empfiehlt der Verlag angehenden Juristen mit dieser und ähnlichen Gesetzessammlungen \marginpar{Zitat gekürzt, weil zu abstrus.} ``einen Bund fürs Leben zu schließen [...] und die Beziehung als Freundschaft mittels Kommunikation und Interesse aufrecht und lebendig zu gestalten'' ^[Quelle: [blog.beck-shop.de/wirtschaft/leben-mit-loseblattwerken](http://blog.beck-shop.de/wirtschaft/leben-mit-loseblattwerken/), Abgerufen 01/2016].

Die \marginpar{Kosten für den öffentlichen Dienst: $25.000 * (3 * ~15\euro{}) \linebreak \approx 1.125.000 \euro{} PA$} Zielgruppe für diesen Kassenschlager ist schlichtweg jeder, der mit dem Rechtswesen zu tun hat:^[Hinweis zu Gender-Formulierungen: Bei allen Bezeichnungen von Personengruppen meint, wenn nicht explizit anders angemerkt, die gewählte Formulierung beide Geschlechter.] Grob sind das bundesweit mindestens über 160.000 aktiven Rechtsanwälte [@BRAK_Mitglieder_2015], über 100.000 Jura-Studenten [@Wissenschaftsrat2012, Seite 80] und noch einmal über 25.000 Richter und Staatsanwälte im öffentlichen Dienst [@BFJ_ZahlRichterStaatsanwaelte] -- Tendenz in allen drei Bereichen steigend.^[citation needed]

Der erste Teil dieser Arbeit beschäftigt sich mit der Konzeptualisierung eines innovativen \ac{SaaS} Unternehmens, welches als Dienstleister für alle Schichten des Rechtswesens auftritt und in aktive Konkurrenz zu den klassischen Gesetzbüchern tritt.

Der Fokus in diesem Abschnitt liegt auf dem vorhandenen Markt, die in diesem gegebene Nachfrage und das entsprechend fehlende Angebot.

Neben verschiedenen Möglichkeiten und Ansätzen der Monetarisierung eines digitalen Angebots in diesem Bereich wird im speziellen diskutiert, wie es sich von aktuell bestehenden Konkurrenzprodukten abhebt. Initial geht es in dieser Arbeit um eine digitale Dienstleistung rund um Gesetzsammlungen. \marginpar{Verkaufsschlager \#2: Gesetzeskommentare} Die Gestaltung dieser Dienstleistung geschieht allerdings zukunftsorientiert um sie flexibel um weitere für die Zielgruppe relevante Angebote zu ergänzen.

Im zweiten Teil der Arbeit wird auf die konkrete Implementierung eines \ac{MVP} eingegangen -- eine mit möglichst geringem Aufwand verbundene Version des Produktes, welche genug der Gesamtidee beinhaltet, um den Markt zu testen. Im Rahmen dieser Arbeit setzt dieses sich aus zwei einzelnen Konstrukten zusammen:

  a)  API-Server
  b)  Web-Applikation

Die bewusste Trennung der beiden Komponenten ist für die Flexibilität des Produkts unabdingbar. Möglicherweise langfristig folgende native Applikationen für verschiedene Plattformen müssen so nur noch eine Schnittstelle zu dem bestehenden API-Server implementieren und sind von den individuellen Implementationen für andere Plattformen unabhängig. <!-- Außerdem ist durch die konzeptionelle auch eine strukturelle Trennung möglich: Applikation und Server (und Datenbank) können auf von einander physikalisch unabhängigen Systemen betrieben werden und sind so individuell skalier- und austauschbar. -->

