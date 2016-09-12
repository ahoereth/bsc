## Sicherheit {#sec:security}
Sicherheit wird heutzutage immer größer geschrieben. Themen wie Privatsphäre und Verschlüsselung sind in aller Munde und es vergeht kaum ein Monat in dem nicht eine weitere große Firma ein *Datenleck* zu verbüßen hat.[^justanotherbreach] Die Schwierigkeit liegt darin, Sicherheit und Nutzungskomfort in Einklang zu bringen.

[^justanotherbreach]: Für eine mit Referenzen versehene Visualisierung siehe [informationisbeautiful.net/visualizations/worlds-biggest-data-breaches-hacks](http://www.informationisbeautiful.net/visualizations/worlds-biggest-data-breaches-hacks), Stand 08/2016

Im Folgenden sollen drei zentrale Problembereiche und ihre in der Umsetzung dieser Arbeit eingesetzten Lösungen erörtert werden:

  1. Die Kommunikation zwischen Client und Server.
  2. Die physikalische sowie softwaremäßige Integrität der Servers.
  3. Die vom Endnutzer eingesetzte Hardware und die Integrität der an diese ausgelieferten Applikation.

Außer für die abschließende Erläuterung von \acp{JWT} wird in diesem Abschnitt umfänglich auf @Tilkov2015 als Referenz zurückgriffen.

### HTTPS
Zur Absicherung des ersten Bereichs und als Grundpfeiler für die Sicherheit einer modernen Applikation dient die umfassende Verschlüsselung der Kommunikation. Durch *Ende-zu-Ende*-Verschlüsselung ist es möglich den Datenverkehr mit heutigen Mitteln auf recht einfache Art und Weise gegen das Abgreifen durch Dritte (*Man-in-the-Middle Attack*) zu schützen. Um dies zu erreichen, wird auf eine in Abbildung @lst:https dargestellte Kombination aus asymmetrischer und symmetrischer Verschlüsselung gesetzt, das \ac{HTTPS}.

Bevor der Server die Möglichkeit hat eine sichere \ac{HTTPS}-Verbindung anzubieten, muss er ein asymmetrisches Schlüsselpaar generieren und sich durch eine \ac{CA}, einem vertrauenswürdigen Dritten, ein Zertifikat für dieses ausstellen lassen (*a*). Gleichermaßen muss der Client von vertrauenswürdigen \acp{CA} sogenannte Root-Zertifikate einholen (*b*).

Listing: HTTPS-Verschlüsselte Kommunikation

```{.dot #lst:https scale=0.75}
digraph G {
  rankdir=LR
  node [shape=rect];

  Server
  Auth [label="Certificate Authority"]
  Client
  {rank=min;Client}
  {rank=max;Server}

  Server:w -> Auth:e [label="(a) public key certification" dir=both]
  Client:e -> Auth:w [label="(b) exchange trusted root-certificate" dir=both]
  Client:n -> Server:n [label="(1) client hello"]
  Server:nw -> Client:ne [label="(2) server hello with signed public key"]
  Client:se -> Server:sw [label="(3) asymmetrically encrypted symmetric key"]
  Client:s -> Server:s [label="(4+) symmetrically encrypted packets" dir=both]
}
```

Zu Beginn einer individuellen Kommunikationssession meldet sich dann ein Client, unverschlüsselt, mit Informationen zu unterstützten Verschlüsselungsverfahren beim Server (*1*). Dieser antwortet daraufhin zusammen mit dem von der \ac{CA} ausgestellten Zertifikat und mit auf Grundlage der zuvor erhaltenen Informationen bestimmten konkreten Rahmenbedingung für die weitere Kommunikation (*2*).

Bevor der Client auf weitere Kommunikation eingeht, überprüft er mithilfe des Root-Zertifikats der \ac{CA} ob die Signatur des erhaltenen Zertifikats authentisch ist. Wenn dies gilt, generiert er einen neuen, exklusiv für diese Kommunikation zu verwendenden symmetrischen Schlüssel und überträgt ihn, mit dem zuvor erhaltenen öffentlichen Schlüssel verschlüsselt an den Server (*3*). Diesen Schritt nennt man asymmetrische Verschlüsselung: Der Client kann Pakete zwar auf diese Weise verschlüsseln, aber, da er nur den öffentlichen Teil des asymmetrischen Schlüsselpaares kennt, nicht entschlüsseln. Da der private Teil des Schlüsselpaares den Server nie verlassen hat, können auch dritte auf den so übertragenen symmetrischen Schlüssel nicht zugreifen. Die gesamte zukünftig in dieser Session stattfindende Kommunikation wird nun von beiden Seiten mit diesem symmetrischen Schlüssel geschützt, der daher auch *Session-Key* genannt (*4+*). Dadurch, dass dieser zu Beginn nur asymmetrisch verschlüsselt an den Server übertragen wurde, können auch möglicherweise die Kommunikation belauschende Dritte die Daten nicht entschlüsseln.[^As]



### Server-Integrität
Der zweite problematische Bereich, die Integrität des Servers, ist offensichtlich durch das Vermeiden von Sicherheitslücken zu schützen. Obwohl dies selbstverständlich anzustreben ist, ist es, durch den Einsatz von Softwarebibliotheken dritter, selbst bei einfachen Applikationen nicht hundertprozentig zuverlässig umsetzbar. Um trotz eventueller Sicherheitslücken die Risiken einer Ausnutzung im Rahmen zu halten, gilt es, nur die Informationen vorzuhalten, welche für die Verwendung der Applikation unbedingt notwendig sind. So ist es zum Beispiel eine Sache, ob Angreifer Passwörter aus einer Datenbank abgreifen konnten, aber eine ganz andere, wenn diese Passwörter nur in verschlüsselter Form vorliegen. Da Passwörter für einen Servicebetreiber niemals im Klartext benötigt werden sollten, kann kryptographisches Hashing eingesetzt: Das Passwort wird vor seiner Speicherung mit Hilfe einer sogenannten Einwegfunktion unkenntlich gemacht. Notwendige Eigenschaften einer solchen kryptographisches Hashfunktion sind, dass sie immer das gleiche eindeutige Ergebnis produziert und nicht umkehrbar ist. Dadurch ist es zwar möglich Passwörter mit dem gespeicherten Hash zu vergleichen, aber nicht, diese aus dem Hash wieder herzustellen.



### Client-Integrität
Ähnliches gilt für Bereich drei, clientseitige Sicherheit. Auf die Integrität des Mobiltelefons oder Rechners des Nutzers haben Servicebetreiber keinerlei Einfluss und müssen sich hier noch mehr als bei ihren eigenen Systemen darauf verlassen, möglichst wenig sensible Informationen auf dem Endgerät zu speichern. Bei einer modernen Webapplikation ist, wie in Abschnitt @sec:server-theory erläutert, allerdings eine sogenannte zustandslose Kommunikation vorzuziehen. Bei einer solchen ist jede Anfrage an den Server für sich atomar, also muss auch individuell authentifiziert werden. Einer der einfachsten Ansätze ist die sogenannte *HTTP Basic Authentication*[^authentorization], bei welcher mit jeder Anfrage an den Server Nutzername und Passwort im Klartext übertragen werden.

Der offensichtliche Nachteil hieran ist nicht nur die Übertragungsform (Klartext), sondern insbesondere auch, dass der Nutzer entweder für jede Anfrage manuell seine Nutzerdaten eintragen muss (was aus offensichtlichen Gründen kein gute Nutzungserfahrung bietet) oder die Nutzerdaten nach initialer Eingabe auf dem Endgerät gespeichert werden müssen. Im Fall der Entwendung des Gerätes ist der Nutzer in einem solchen Fall auf das Zurücksetzen seines für den Dienst verwendeten Passwortes angewiesen, was besonders aufgrund der Tendenz für viele Dienstleister das gleiche Passwort zu verwenden problematisch ist. Ein Lösung hierfür finden sich in Autorisierungstokens mit vorgeschrieben Lebensdauern. Nach der initialen Authentifizierung des Nutzers auf Grundlage seiner Nutzerdaten wird vom Server ein signierter Token bereitgestellt, welcher bei zukünftigen Serveranfragen mit übertragen wird. Im Fall des Verlustes des Endgerätes wird so nur der in seiner Lebenszeit begrenzte Token kompromittiert, allerdings nicht die Nutzerdaten. Dem Nutzer kann zusätzlich sehr einfach das Widerrufen von alten Tokens angeboten werden.

Die Lawly Applikation setzt hierfür auf den offen Standard von \acfp{JWT}. Ein \ac{JWT} setzt sich aus drei Teilen zusammen: Im ersten Teil, dem Header, finden sich Informationen über den Token selbst, also zum Beispiel die Bezeichnung des Verschlüsselungsalgorithmus, welcher bei der Signierung eingesetzt wurde. Der zweite Teil beinhaltet die *claims*, sogenannte Ansprüche die der Token an seine Zugriffsrechte in der angefragten Ressource stellt. Dies beinhaltet zum Beispiel die E-Mailadresse des Nutzers, da diese für die Verbindung des Nutzers zu seinen vorgenommenen Vermerken herstellt. Der letzte Teil ist die Signatur. Sie ist ein kryptographischer Hash, welcher aus den beiden anderen Teilen und einem geheimen Schlüssel, welcher nur dem Server bekannt ist, generiert wurde. Dadurch, dass dieser Hash eindeutig aus diesen drei Teilen erstellt wurde, kann keiner dieser drei Teile verändert werden, ohne das der Hash seine Gültigkeit verliert. [@Jones2015]

Der Token kann somit sicher auf Nutzerseite gespeichert werden, ohne dass eine Kompromittierung des Gerätes die Aufgabe des Passworts bedeuten würde. Durch ein relativ kurzes Ablaufdatum, im *claim* als *expiration* gespeichert, kann zusätzlich automatisch für ein Verfallen des Tokens gesorgt werden. Bei aufeinanderfolgenden Anfragen wird dabei jedes Mal überprüft ob das Verfallsdatum naheliegt und wenn dem so ist gegebenenfalls ein neuer Token für folgende Anfragen bereitgestellt.

[^As]: Durch den Einsatz von durch die freie [Let's Encrypt](https://letsencrypt.org) \ac{CA} ausgestellte Zertifikate und der konsequenten Befolgung aktueller Sicherheitsempfehlungen erhalten die Lawly API und die Lawly Webapplikation jeweils Bestnoten von den auf das Testen von Sicherheitskonfigurationen von Webservices spezialisierten Anbietern [ssllabs.com](https://www.ssllabs.com/ssltest/analyze.html?d=api.lawly.org) und [securityheaders.io](https://securityheaders.io/?q=api.lawly.org&followRedirects=on).

[^authentorization]:
    *Authentication* und *Authorization* werden, obwohl eigentlich zwei unterschiedliche Dinge, in der HTTP-Spezifikation beziehungsweise ihrer Umsetzung oft ungenau verwendet. Ein Beispiel hierfür sind die HTTP Statuscodes 401 und 403:

      + *401 Unauthorized*: "Request lacks valid authentication credentials." ([tools.ietf.org/html/rfc7235](https://tools.ietf.org/html/rfc7235#section-3.1)) -- wörtlich dann wohl eher ein *unauthenticated* Zugriff (fehlende Authentifizierung).
      + *403 Forbidden*: "The provided authentication credentials are considered insufficient." ([tools.ietf.org/html/rfc7231](https://tools.ietf.org/html/rfc7231#section-6.5.3)) -- gleichermaßen wörtlich also eher ein *unauthorized* oder unerlaubter Zugriff, obwohl die Anfrage eigentlich Authentifiziert ist.

    Eine ausführlichere Diskussion hierzu findet sich zum Beispiel unter [stackoverflow.com/q/3297048](http://stackoverflow.com/q/3297048).

<!-- https://news.ycombinator.com/item?id=11929267 -->
