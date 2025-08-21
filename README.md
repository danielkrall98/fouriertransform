# PS Grundlagen Bildverarbeitung
Gruppe Fourier Transform: Andrassik, Krall

------------------------------------------------------------------------------------------------------

### Beschreibung:
Ein Classifier mit Bildern von Fingervenen soll verwendet werden, um zwischen echten, gefälschten und
synthetisch-erstellten Bildern unterscheiden zu können.\
Für die Baseline-Variante wird mit echten (genuine) und gefälschten (spoofed) Daten trainiert und nur
zwischen diesen Unterschieden.\
Für das eigentliche Projekt werden die gefälschten Daten (spoofed) durch synthetisch-erstellte Daten
(synthetic) ersetzt. Die synthetischen Daten sollen dabei gefälschte Daten imitieren, ohne, dass die
tatsächlichen gefälschten Daten umständlich per Hand erzeugt werden müssen
(einscannen, abfotografieren, etc.)\
Dabei soll mit echten und synthetischen Daten trainiert und dann zwischen echten und gefälschten Daten
unterschieden werden.\
<br>
Leider hat das Projekt gezeigt, dass die Fourier-Transformation (aufgrund der enstehenden Artefakte) 
für diese Klassifizierung nicht wirklich geeignet ist. <br>

[Ergebnisse in der Präsentation](./presentation/Presentation.pdf)

------------------------------------------------------------------------------------------------------

### Besprechungen:

------------------------------------------------------------------------------------------------------

30.10.\
Bandpassfilter -> Ring -> Koeffizient -> Mittelwert/Abweichung/Energie/Histogramme\
-> in verschiedenen Bändern (Radien) mit Magnitude der Fourier Transform

Bis nächstes Mal mit verschiedenen Filtern 

------------------------------------------------------------------------------------------------------

13.11.\
Bandpassfilter an Bilder anpassen (nicht quadratisch)\
Ob Abweichung passt erst bei größeren Experimenten sichtbar\
Mehr als drei Bänder\
Bis nächstes Mal in KNN -> und erste Ergebnisse\
Bei Featurevektor alles in einen Vektor, aber schauen, wie passt

------------------------------------------------------------------------------------------------------

27.11.\
KNN umschreiben (Scikit? -> LeaveOneOut)\
Energie statt Abweichung!!! (Summe von n² von Koeffizienten) im Band\
Synthetische einberechnen\
Genuine vs Spoof im Ergebnis\
Bis zum nächsten Mal: eine Datenbank mit synth. vergleichen

------------------------------------------------------------------------------------------------------

11.12.\
Bei quadratischen synthetischen Bildern Größe anpassen (Python Code von Prof)\
Scikit KNN!\
Nächster Schritt: LeaveOutOut -> LeaveOneSubjectOut/LeaveOnePersonOut Cross Validation
	-> Keine Bilder von dieser Person in Trainingsdaten!

1. Genuine vs Spoofed
2. Genuine vs Synthetisch\
Ziel: Genuine + Synthetisch -> Spoofed erkennen

Bis 08.01. alle Daten -> Auswertungen

------------------------------------------------------------------------------------------------------

08.01.\
Vollstaendige Ergebnisse\
Einfluss von Anzahl Bändern und k\
Präsentation bis zum naechsten Mal\

------------------------------------------------------------------------------------------------------

22.01.\
Balanciert -> Nur Genuine verwenden, die auch in synthetisch/spoofed sind (gleich viele)\
LeaveOneSubjectOut UND LeaveOneOut\
Schauen in welchen Baendern unterschiede (nicht alle 30 Baender verwenden) -> diese Baender rekonstruieren\
Ein Band rekonstruieren?\
Praesentation an Prof schicken (nicht erst am letzten Tag)

------------------------------------------------------------------------------------------------------














