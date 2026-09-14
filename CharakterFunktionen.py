#Charakterfunktionen soll später alles handeln was mit dem charakter zu tun hat
def NeuerCharakter():

    Name = input("Gib deinem Charakter einen Namen: ")

    Alter = int(input("Gib deinem Charakter ein Alter: "))

    Klasse = input(
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
        Klasse in ["Magier", "Krieger", "Priester", "Schurke"]
        and SchlechteEigenschaft in ["Faul", "Zornig", "Hyperaktiv", "Gierig", "Besserwisser"]
        and GuteEigenschaft in ["Perfektionist", "Ehrgeizig", "Intelligent", "Stark", "Goldene Zunge"]
    ):
        return {
            "Name": Name,
            "Alter": Alter,
            "Klasse": Klasse,
            "SchlechteEigenschaft": SchlechteEigenschaft,
            "GuteEigenschaft": GuteEigenschaft,
            "Stats": {
                "Leben": 100,
                "Mana": 50,
                "Stärke": 10,
                "Geschick": 10,
                "Intelligenz": 10,
                "Verteidigung": 10
            },
            "Inventar": [],
            "LinkeHand": None,
            "RechteHand": None
        }

    else:
        print("Charaktererstellung ist fehlgeschlagen, versuche es nochmal")
