from funktionen import lade_spiel, speichere_spiel, neuer_charakter

spiel_daten = lade_spiel()
charakter_liste = spiel_daten["charaktere"]

# Wenn es keine Charaktere gibt, soll einer hinzugefügt werden
if len(charakter_liste) == 0:
    Charakteranzahl = int(input("Mit wievielen Charakteren willst du Spielen? 1-5: "))
    charakter_liste.append(neuer_charakter())
    speichere_spiel(spiel_daten)

print(charakter_liste)
