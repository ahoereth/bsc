## Sicherheit {#sec:security}
Sicherheit wird heutzutage immer größer geschrieben. Themen wie Privatsphäre und Verschlüsselung sind in jeder Munde und es vergeht kaum ein Monat in dem nicht eine weitere große Firma ein *Datenleck* zu verbüßen hat. Der Knackpunkt ist, Sicherheit und Nutzungskomfort verbunden zu kriegen.

Die Sicherheit hat im Endeffekt 3 konkrete Problemzonen:

  1. Die Kommunikation zwischen Client und Server
  2. Die Integrität des Servers (Hard- sowie Softwareseitig) und der dort gespeicherten Daten.
  3. Die Hardware des Nutzers und die darauf laufende Clientapplikation.

Als Lösung für Punkt 1 und als Grundpfeiler für die Sicherheit einer modernen Applikation dient die umfassende Verschlüsselung der Kommunikation. Durch sogenannte *Ende-zu-Ende* Verschlüsselung ist es möglich den Datenverkehr auf heutzutage für Dienstleister recht einfache Art und Weise gegen das Abgreifen durch Dritte (*Man-in-the-Middle Attack*) zu schützen. Um dies zu erreichen wird auf eine in Abbildung @lst:https dargestellte Kombination aus asymmetrischer und symmetrischer Verschlüsselung gesetzt, das \ac{HTTPS}.

Bevor der Server die Möglichkeit hat eine sichere \ac{HTTPS}-Verbindung anzubieten, muss er ein für asymmetrische Verschlüsselung benutzbares Schlüsselpaar generieren und sich mit diesem bei einer Certificate Authority, einem vertrauenswürdigen Dritten, zertifizieren lassen (*0*). Zu Beginn einer individuellen Kommunikationsession meldet sich dann ein Client, unverschlüsselt, mit einigen Informationen zu unterstützten Verschlüsselungsverfahren und ähnlichem beim Server (*1*). Dieser Antwortet daraufhin mit, auf Grundlage der erhaltenen Informationen, konkreten Rahmenbedingung (wie zum Beispiel zu verwendende Verschlüsselungsverfahren) für die weitere Kommunikation und dem öffentlichen Teil seines zertifizierten *private-public* Schlüsselpaares (*2*). Bevor der Client auf weitere Kommunikation eingeht, lässt er sich den erhaltenen öffentlichen Schlüssel durch die Certificate Authority verifizieren (*3*). Daraufhin generiert er, unter Anwendung der zuvor in Absprache mit dem Server festgelegten Parameter, einen neuen, exklusiv für diese Kommunikation verwendete, diesmal symmetrischen, Schlüssel und überträgt ihn, mit dem zuvor erhaltenen öffentlichen Schlüssel verschlüsselt, an den Server (*4*)^[>\color{red}Komisch kompliziert verschachtelte Sätze.]. Diesen Schritt nennt man asymmetrische Verschlüsselung: Der Client kann Pakete zwar auf diese Weise verschlüsseln, aber, da er nur den öffentlichen Teil des Schlüsselpaares kennt, nicht entschlüsseln. Da der private Teil des Schlüsselpaares den Server nie verlassen hat, können auch dritte auf den neuen Schlüssel nicht zugreifen. Alle zukünftige in dieser Session stattfindende Kommunikation wird nun von beiden Seiten mit diesem symmetrischen Schlüssel geschützt (*5*). Dadurch, dass dieser zu Beginn nur asymmetrisch verschlüsselt an den Server übertragen wurde, können mögliche die Kommunikation belauschende Dritte die Daten nicht entschlüsseln.^[>\color{red}Kryptop-Citation needed.]

Listing: HTTPS-Verschlüsselte Kommunikation

```{.dot #lst:https}
digraph G {
  rankdir=LR
  node [shape=rect];

  Server
  Auth [label="Certificate Authority"]
  Client
  {rank=min;Client}
  {rank=max;Server}

  Server:w -> Auth:e [label="(0) public key certification" dir=both]
  Client:n -> Server:n [label="(1) client hello"]
  Server:nw -> Client:ne [label="(2) server hello with public key"]
  Client:e -> Auth:w [label="(3) server public key verification" dir=both]
  Client:se -> Server:sw [label="(4) asymmetrically encrypted symmetric key"]
  Client:s -> Server:s [label="(5+) symmetrically encrypted packets" dir=both]
}
```

Punkt 2 ist offensichtlich durch das vermeiden von Sicherheitslücken lösbar. Obwohl dies selbstverständlich anzustreben ist, ist der Ansatz, nur die Informationen zu speichern, für welche dies auch notwendig ist, sehr viel grundlegender. So ist es zum Beispiel eine Sache, ob Angreifer alle Daten aus der Datenbank abgreifen konnten, aber eine ganz andere, wenn diese Daten verschlüsselt und für niemanden, auch nicht den Servicebetreiber, lesbar sind. Dies ist für Passwörter, welche von einem Service-Provider niemals im Klartext benötigt werden sollten, durch kryptologisches Hashing erreichbar: Das Passwort wird vor seiner Speicherung mit Hilfe einer Einweg-Hashfunktion unkenntlich gemacht. Notwendige Eigenschaften einer solchen kryptlogischen Hashfunktion sind, dass sie immer das gleiche eindeutige Ergebnis produziert und nicht umkehrbar ist. Dadurch ist es möglich Passwörter mit dem gespeicherten Hash zu vergleichen.^[>\color{red}Kryptop-Citation needed.]

Ähnliches gilt für Punkt 3, clientseitige Sicherheit. Auf die Integrität des Mobiltelefons oder Rechners des Nutzers haben Servicebetreiber keinerlei Einfluss und müssen sich hier noch mehr als bei ihren eigenen Systemen darauf verlassen, möglichst wenig sensible Informationen dort zu speichern. Bei einer modernen Webapplikation ist, wie in Abschnitt @sec:server, allerdings eine sogenannte Zustandslose-Kommunikation vorzuziehen. Bei einer solchen ist jede Anfrage an den Server für sich atomar, muss also auch jede für sich authentifiziert werden. Einer der einfachsten und auch ein sehr verbreiteter Ansatz hierfür ist die sogenannte HTTP Basic Authentication, bei welcher mit jeder Anfrage an den Server im `Authentication`-Header Nutzername und Passwort übertragen werden. Der Nachteil hieran ist ganz klar, dass der Nutzer entweder für jede Anfrage manuell seine Nutzerdaten eintragen muss (was aus offensichtlichen Gründen kein gutes \ac{UX} bietet) oder die Nutzerdaten nach initialer Eingabe auf dem Clientseite gespeichert werden müssen. Im Fall der Entwendung des Gerätes ist der Nutzer in einem solchen Fall auf die Änderung seines Passwortes angewiesen, was besonders problematisch ist, da Nutzer weiterhin dazu tendieren für viele Dienstleister das gleiche Passwort zu verwenden. Ein modernerer Ansatz sind sogenannte Authentication-Tokens mit vorgeschrieben Lebensdauern. Nach der initialen Authentifizierung des Nutzers auf Grundlage seine Nutzerdaten wird vom Server ein eindeutiger verschlüsselter Token bereitgestellt, welcher bei zukünftigen Serveranfragen mit übertragen wird. Im Fall des Verlustes des Endgerätes wird so nur der in seiner Lebenszeit begrenzte Token kompromittiert, allerdings nicht die Nutzerdaten. Dem Nutzer zusätzlich sehr einfach über eine neue Verbindung das Widerrufen von alten Tokens angeboten werden.

JWT Spec: https://tools.ietf.org/html/rfc7519

https://news.ycombinator.com/item?id=11929267
