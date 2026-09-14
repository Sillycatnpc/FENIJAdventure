import json
from pathlib import Path

Antwortmöglichkeiten = {
    "ja": {"j", "y", "ja", "yes"},
    "nein": {"n", "nein", "ne", "nope"}
}

Items = {
    ### Waffen ###

    "Holzschwert": {
        "Schaden": 7,
        "Haltbarkeit": 10,
        "Wert": 35,
        "ZerfälltZu": [{"Item": "Holzstück", "Wahrscheinlichkeit": 1}, {"Item": "Holzstück", "Wahrscheinlichkeit": 0.25}],
        "Eigenschaften": {"Brennbar"}
    },
    
    "Stumpfes Eisenschwert": {
        "Schaden": 20,
        "Haltbarkeit": 20,
        "Wert": 100,
        "ZerfälltZu": [{"Item": "Eisenschrott", "Wahrscheinlichkeit": 1}, {"Item": "Eisenschrott", "Wahrscheinlichkeit": 0.25}],
        "Eigenschaften": {}
    },
    
    "Eisenschwert": {
        "Schaden": 37,
        "Haltbarkeit": 20,
        "Wert": 200,
        "ZerfälltZu": [{"Item": "Stumpfes Eisenschwert", "Wahrscheinlichkeit": 1}],
        "Eigenschaften": {}
    },

    ### Rüstung ###

    ### Materialien ###

    "Holzstück": {
        "Schaden": 2,
        "Haltbarkeit": 20,
        "Wert": 8,
        "ZerfälltZu": [],
        "Eigenschaften": {"Brennbar"}
    },

    "Eisenschrott": {
        "Schaden": 5,
        "Haltbarkeit": 50,
        "Wert": 30,
        "ZerfälltZu": [],
        "Eigenschaften": {}
    },

    ### Andere ###

    "Seil": {
        "Schaden": 2,
        "Haltbarkeit": 100,
        "Wert": 20,
        "ZerfälltZu": [],
        "Eigenschaften": {"Brennbar", "Fesseln"}
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
