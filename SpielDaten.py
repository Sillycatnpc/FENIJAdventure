import json
from pathlib import Path

Antwortmöglichkeiten = {
    "ja": {"j", "y", "ja", "yes"},
    "nein": {"n", "nein", "ne", "nope"}
}

Items = {
    # ==================== WAFFEN ====================
    "holzschwert": {
        "Name": "Holzschwert",
        "Kategorie": "Waffen",
        "Wert": 15,
        "Schaden": 10,
        "Wurfschaden": 5,
        "Haltbarkeit": 10,
        "MaxHaltbarkeit": 10,
        "Eigenschaften": {"brennbar"},
        "Beschreibung": "Ein einfaches Übungsschwert aus Holz."
    },
    "stumpfes_eisenschwert": {
        "Name": "Stumpfes Eisenschwert",
        "Kategorie": "Waffen",
        "Wert": 45,
        "Schaden": 15,
        "Wurfschaden": 5,
        "Haltbarkeit": 60,
        "MaxHaltbarkeit": 100,
        "Eigenschaften": {"minderwertig"},
        "Beschreibung": "Eine abgenutzte Klinge, die schon bessere Tage gesehen hat."
    },
    "eisenschwert": {
        "Name": "Eisenschwert",
        "Kategorie": "Waffen",
        "Wert": 75,
        "Schaden": 25,
        "Wurfschaden": 8,
        "Haltbarkeit": 100,
        "MaxHaltbarkeit": 100,
        "Eigenschaften": {"hochwertig"},
        "Beschreibung": "Eine solide, scharfe Eisenklinge."
    },
    # ==================== RÜSTUNG ====================
    "lederrüstung": {
        "Name": "Lederrüstung",
        "Kategorie": "Rüstung",
        "Slot": "Brust",
        "Wert": 50,
        "Verteidigung": 8,
        "Haltbarkeit": 80,
        "MaxHaltbarkeit": 80,
        "Eigenschaften": {"leicht"},
        "Beschreibung": "Bietet grundlegenden Schutz, ohne die Bewegung einzuschränken."
    },
    # ==================== TRÄNKE ====================
    "kleiner_heiltrank": {
        "Name": "Kleiner Heiltrank",
        "Kategorie": "Tränke",
        "Wert": 20,
        "Heilung": 30,
        "Stapelbar": True,
        "MaxStapel": 10,
        "Eigenschaften": {"verbrauchbar"},
        "Beschreibung": "Stellt sofort 30 Lebenspunkte wieder her."
    },
    # ==================== SAMMELGEGENSTÄNDE & WERKZEUGE ====================
    "seil": {
        "Name": "Seil",
        "Kategorie": "Sammelgegenstände",
        "Wert": 10,
        "Stapelbar": True,
        "MaxStapel": 5,
        "Eigenschaften": {"fesseln", "klettern"},
        "Beschreibung": "Ein reißfestes Hanfseil. Nützlich zum Klettern oder Fesseln."
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
