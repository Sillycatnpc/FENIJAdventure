import json
from pathlib import Path

Antwortmöglichkeiten = {
    "ja": {"j", "y", "ja", "yes"},
    "nein": {"n", "nein", "ne", "nope"}
}

Items = {
    #Waffen
    "Holzschwert": {
        "Schaden": 10,
        "Wurfschaden": 5,
        "Haltbarkeit": 10,
        "Wert": 15,
        "Eigenschaften": {"brennbar"}
    },
    
    "Stupmfes Eisenschwert": {
        "Schaden": 20,
        "Wurfschaden": 5,
        "Haltbarkeit": 100,
        "Wert": 75,
        "Eigenschaften": {"Minderwertig"}
    },
    
    "Eisenschwert": {
        "Schaden": 10,
        "Wurfschaden": 5,
        "Haltbarkeit": 10,
        "Wert": 15,
        "Eigenschaften": {"hochwertig"}
    },
        "Holzschwert": {
        "Schaden": 10,
        "Wurfschaden": 5,
        "Haltbarkeit": 10,
        "Wert": 15,
        "Eigenschaften": {}
    },
    #Rüstung
    "Seil": {
        "Schaden": 2,
        "Wurfschaden": 1,
        "Haltbarkeit": 100,
        "Wert": 15,
        "Eigenschaften": {"Fesseln"}
    }

}

SpielStandDateipfad = Path(__file__).parent / "Spielstand.json"

# Lade Charaktere aus Spielstand.json
try:
    with open(SpielStandDateipfad, "r", encoding="utf-8") as Datei:
        Spielstand = json.load(Datei)

        Charaktere = Spielstand["Charaktere"]

except FileNotFoundError:  # Wenn die Spielstand.json nicht existiert oder fehlerhaft ist, werden die Variablen neu erstellt
    Charaktere = []
