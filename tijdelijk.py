prijzen = {
    "aardbei" : 1,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["vanille"] * 0.8
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1liter - slechts €"
reclame_tekst3 = reclame_tekst.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el) <= 4:
        print(el.lower())
    else:
        print(el.upper())
