#Charakterfunktionen soll später alles handeln was mit dem charakter zu tun hat

def neuer_charakter():

    name = input("Gib deinem Charakter einen Namen: ")

    alter = int(input("Gib deinem Charakter ein Alter: "))

    klasse = input(
        "Gib deinem Charakter eine Klasse, wähle einen Klassenpfad aus: "
        "Magier, Krieger, Priester, Schurke: "
    )

    schlechte_eigenschaft = input(
        "Gib deinem Charakter eine manchmal schädliche persönliche Eigenschaft: "
        "Faul, Zornig, Hyperaktiv, Gierig, Besserwisser: "
    )

    gute_eigenschaft = input(
        "Gib deinem Charakter eine persönliche nützliche Eigenschaft: "
        "Perfektionist, Ehrgeizig, Intelligent, Stark, Goldene Zunge: "
    )

    if (
        klasse in ["Magier", "Krieger", "Priester", "Schurke"]
        and schlechte_eigenschaft in ["Faul", "Zornig", "Hyperaktiv", "Gierig", "Besserwisser"]
        and gute_eigenschaft in ["Perfektionist", "Ehrgeizig", "Intelligent", "Stark", "Goldene Zunge"]
    ):
        return {
            "name": name,
            "alter": alter,
            "klasse": klasse,
            "s.Eigenschaft": schlechte_eigenschaft,
            "g.Eigenschaft": gute_eigenschaft,
            "stats": {
                "leben": 100,
                "mana": 50,
                "stärke": 10,
                "geschick": 10,
                "intelligenz": 10,
                "verteidigung": 10
            }
        }

    else:
        print("Charaktererstellung ist fehlgeschlagen, versuche es nochmal")