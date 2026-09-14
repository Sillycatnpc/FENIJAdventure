from SpielDaten import Charaktere, Antwortmöglichkeiten
from AndereFunktionen import SpeichereSpiel
from CharakterFunktionen import NeuerCharakter
import sys

print()
print("### Willkommen, Passant! ###")
print()

# Wenn es keine Charaktere gibt, soll einer hinzugefügt werden
if len(Charaktere) == 0:
    SollNeuesSpielErstellen = input("Kein Spielstand gefunden. Möchtest du einen neuen erstellen? ")

    if SollNeuesSpielErstellen.lower() in Antwortmöglichkeiten["ja"]:
        # Charakteranzahl = int(input("Mit wievielen Charakteren willst du Spielen? 1-5: "))
        Charaktere.append(NeuerCharakter())

        SpeichereSpiel()
    
    else:
        sys.exit()

print(Charaktere)
