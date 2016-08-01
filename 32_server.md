## Server
\label{sec:server}

Auf Grund der Anforderung eines flexibel auf mehr Plattformen erweiterbaren Produktes kommt für den Server nur eine rein am \ac{API}-Konzept orientierte Struktur in Frage. Grundlegend gilt hierbei, dass der Server keinerlei Wissen über die eigentliche Darstellung der Daten auf Client-Seite hat, sondern diese nur in ihrer Rohform in flexibler Form und sinnvoll kombiniert bereitstellt. 

Durch diese konzeptionelle Trennung ergibt sich die Möglichkeit Server und Client auch strukturell zu trennen und so zum Beispiel über unterschiedliche Server bereitzustellen und diese unabhängig von einander der unter Betrieb und durch zu erhoffendes Wachstum entstehenden Last anzupassen, das sogenannte [*Scaling*](#glossary).



### REST

  * representational state transfer
  * HTTP verbs


### Sockets

  * Ausblick
  * Strukturelle Problematik bei multi-server setups.
