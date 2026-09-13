
Charakteranzahl = int(input("Mit wievielen Charakteren willst du Spielen? 1-5: "))


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


charakter_liste = []

charakter_liste.append(neuer_charakter())

print(charakter_liste)