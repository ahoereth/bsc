# Implementation {#sec:implementation}
Im Folgenden wird auf die konkrete Implementation der zu Beginn angekündigten beiden Phasen, Datenaggregation (Abschnitt @sec:data) und Applikationsimplementation (wieder unterteilt in Server, Abschnitt @sec:server-architecture, und Client, Abschnitt @sec:client-architecture) eingegangen. Besonders im Client-Abschnitt erfolgt dies nicht umfänglich sondern für einzelne Bereiche beispielhaft, da dies sonst den Rahmen diese Dokuments übersteigen würde. Zum Abschluss wird in Abschnitt @sec:deployment auf die Veröffentlichung der beiden Applikationsbestandteile für den Produktiveinsatz eingegangen.

Für die Versionskontrolle des Projekts wird auf drei `git`-Repositories gesetzt, welche über den Anbieter GitHub[^github] verwaltet werden: Einmal für den Server-Quelltext (*lawly_api*) [^servergit], den Client-Quelltext (*lawly_web*)[^clientgit] und das in Markdown verfasste vorliegende Dokument (*bsc*)[^bscgit]. Um die Verbindung zwischen den folgenden Beschreibungen und dem eigentlichen Quelltext zu erleichtern werden besprochene Dateien in den Fußnoten anhand ihres Repositories und Pfades mit Hyperlink direkt zu GitHub referenziert.

[^github]: [github.com](https://github.com)

[^clientgit]: [github.com/ahoereth/lawly_web](https://github.com/ahoereth/lawly_web) 

[^servergit]: [github.com/ahoereth/lawly_api](https://github.com/ahoereth/lawly_api) 

[^bscgit]: [github.com/ahoereth/bsc](https://github.com/ahoereth/bsc)
