# Einleitung {#sec:introduction}
Die vorliegende Arbeit beschäftigt sich mit der Konzeptualisierung und Entwicklung einer Webapplikation zur interaktiven Navigation deutscher Bundesgesetze.

Zu Beginn wird hierfür in Abschnitt @sec:concept der als Zielgruppe bestimmte Markt und die Relevanz einer durch eine solche Applikation angebotenen Dienstleistung analysiert. Hierbei werden besondere Anforderungen und nötige Alleinstellungsmerkmale im Vergleich zu bereits vorhandenen Konkurrenzprodukten hervorgehoben. Dabei wird auch die diese Arbeit übersteigende größere Zielsetzung dargestellt: die hier entwickelte Applikation dient zum Ausloten des am Markt erwarteten Interesses und als Grundlage für eine umfangreichere Softwaredienstleistung.

Im darauf folgenden Abschnitt @sec:paradigms werden bei der Implementierung der Applikation verfolgte Paradigmen und verwendete Technologien diskutiert. Hierbei werden Entscheidungen wiederum auch mit Blick auf die langfristige Ausrichtung der Dienstleistung bezogen. Die entwickelte Webapplikation soll so nur die Grundlage einer ersten Version des Produktes sein und gute Erweiterungsmöglichkeiten in Bezug auf Umfang als auch hin zu nativen Mobilapplikationen bieten. Teil davon ist zum Beispiel die Trennung der Applikation in einen Client, die Webseite mit der der Nutzer interagiert, und einen API-Server, die Schnittstelle von welcher der Client Daten bezieht. In diesem und dem folgenden Abschnitt wird grundlegendes Wissen über Softwarearchitektur und -entwicklung sowie über Webtechnologien vorausgesetzt. Es werden primär Besonderheiten der verwendeten Paradigmen und Technologien und insbesondere deren Unterscheidungsmerkmale zu oft vorherrschenden Alternativen diskutiert.

Abschnitt @sec:implementation beschreibt daraufhin die konkrete Implementation der Applikation. Hier wird neben einer generellen Übersicht über jeweils die Struktur des API-Servers und der Clientapplikation beispielhaft eine einzelne Ansicht der Applikation und das Ineinandergreifen der für sie benötigten Bestandteile beschrieben. Außerdem wird beispielhaft auf eine sich bei der Entwicklung gezeigte Herausforderung und ihre Bewältigung eingegangen.

Abschließend wird in Abschnitt @sec:discussion ein Rück- sowie Ausblick geboten. Auf der Softwareseite werden so beispielsweise die zuvor getroffenen Entscheidungen bezüglich der eingesetzten Werkzeuge auf Grundlage der neu gesammelten Erfahrungen diskutiert. Neben im Rahmen eines solchen Projektes auftretenden auch kritischen Überlegungen bezüglich der Relevanz des Gesamtproduktes wird zum Ende auch eine positive Perspektive zum weiteren Verlauf dargelegt.



\newcommand\blfootnote[1]{
    \begingroup
    \renewcommand\thefootnote{}\footnote{#1}
    \addtocounter{footnote}{-1}
    \endgroup
}
\blfootnote{Hinweis zu gendergerechter Sprache: Bei allen Bezeichnungen von Personengruppen meint, wenn nicht explizit anders angemerkt, die gewählte Formulierung beide Geschlechter.}
