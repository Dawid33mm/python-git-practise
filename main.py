def powitaj(imie):
    return f"Cześć, {imie}!"


def przedstaw_sie(imie, wiek):
    return f"{imie} ma {wiek} lat."

def sprawdz_wiek(wiek):
    if wiek >= 18:
        return "Osoba pełnoletnia"
    return "Osoba niepełnoletnia"

print(powitaj("Paweł"))
print(przedstaw_sie("Paweł", 22))
print(sprawdz_wiek(22))