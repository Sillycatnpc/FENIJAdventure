import json

Antwortmöglichkeiten = {
    "ja": {"j", "y", "ja", "yes"},
    "nein": {"n", "nein", "ne", "nope"}
}

# Lade Charaktere aus Spielstand.json
try:
    with open("Spielstand.json", "r", encoding="utf-8") as Datei:
        Spielstand = json.load(Datei)

        Charaktere = Spielstand["Charaktere"]

except FileNotFoundError:  # Wenn die Spielstand.json nicht existiert oder fehlerhaft ist, werden die Variablen neu erstellt
    Charaktere = []
