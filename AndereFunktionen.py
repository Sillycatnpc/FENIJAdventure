from SpielDaten import Charaktere, SpielStandDateipfad
import json

# Speichere das Spiel
def SpeichereSpiel():
    with open(SpielStandDateipfad, "w", encoding="utf-8") as Datei:
        Spielstand = {
            "Charaktere": Charaktere
        }
        
        json.dump(Spielstand, Datei, indent=2, ensure_ascii=False)
