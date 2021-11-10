print("Guten Tag, un ihnen zu helfen benötigen wir nur einige Daten um richtig los zu legen. \nDas wäre: \n     Nachname \n     Vorname \n     Kundennummer")

print("Legen wir mit dem Nachnamen los:")
Nachname = input()
print("Nun der Vorname:")
Vorname = input()
print("Und zu aller letzt die Kundennummer:")
Kundennummer = input()

print("\nNun nochmal zusammengefasst: \n    Sie sind " + Nachname + ", " + Vorname + " mit der Kundennummer " + Kundennummer + ". \n    Ist das Korrekt? Wenn nicht, pech gehabt.")

print("\n\nNun da die uns ihre Daten gegeben haben kann mit dem eigentliche Grund weshalb Sie hier sind losgehen. \n\nWir vermuten sehr stark das Sie ein problem mut unserem Produkt haben. Deswegen bitten Wir Sie eines der folgenden Problem anzugeben um Sie direkt zu einem unserer Spezialisten weiter zu leiten.")
print("Haben Sie eines der Folgenden Probleme:")
print("    Problem beim Straten")
print("    Softwareprobleme")
print("    Harwareprobleme")
print("    Anderes")

Problem = input()

if Problem == "Harwareproblem" :
    {
    print("du bist Scheiße")
    }


if Problem == "Softwareproblem" :
    {
        print("Im übrigen bin ich der...")
    }