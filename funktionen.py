import ast

def speichere_spiel(spiel_daten):
    with open("spiel-daten.txt", "w", encoding="utf-8") as datei:
        datei.write(repr(spiel_daten))

def lade_spiel():
    try:
        with open("spiel-daten.txt", "r", encoding="utf-8") as datei:
            spiel_daten = ast.literal_eval(datei.read())

    # Wenn die Datei nicht existiert oder fehlerhaft ist, werden die Spieldaten neu erstellt
    except (FileNotFoundError, SyntaxError, ValueError):
        print("\033[95mFehler beim einlesen von spiel-daten.txt, datei wird neu erstellt ...\033[0m")

        spiel_daten = {
            "charaktere": []
        }

        speichere_spiel(spiel_daten)

    return spiel_daten

def neuer_charakter():

    name = input("Gib deinem Charakter einen Namen: ")

    alter = int(input("Gib deinem Charakter ein Alter: "))

    klasse = input(
        "Gib deinem Charakter eine Klasse, wähle einen Klassenpfad aus: "
        "Magier, Krieger, Priester, Schurke: "
    )

    SchlechteEigenschaft = input(
        "Gib deinem Charakter eine manchmal schädliche persönliche Eigenschaft: "
        "Faul, Zornig, Hyperaktiv, Gierig, Besserwisser: "
    )

    GuteEigenschaft = input(
        "Gib deinem Charakter eine persönliche nützliche Eigenschaft: "
        "Perfektionist, Ehrgeizig, Intelligent, Stark, Goldene Zunge: "
    )

    if (
        klasse in ["Magier", "Krieger", "Priester", "Schurke"]
        and SchlechteEigenschaft in ["Faul", "Zornig", "Hyperaktiv", "Gierig", "Besserwisser"]
        and GuteEigenschaft in ["Perfektionist", "Ehrgeizig", "Intelligent", "Stark", "Goldene Zunge"]
    ):
        return {
            "name": name,
            "alter": alter,
            "klasse": klasse,
            "s.Eigenschaft": SchlechteEigenschaft,
            "g.Eigenschaft": GuteEigenschaft
        }

    else:
        print("Charaktererstellung ist fehlgeschlagen, versuche es nochmal")
