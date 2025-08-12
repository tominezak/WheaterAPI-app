 # match-case statement er det samme som switch-case i andre språk
# et alternativ istedenfor å bruke if-elif-else

def day_of_week(day):
    match day:
        case 1:
            return "Mandag"
        case 2:
            return "Tirsdag"
        case 3:
            return "Onsdag"
        case 4:
            return "Torsdag"
        case 5:
            return "Fredag"
        case 6:
            return "Lørdag"
        case 7:
            return "Søndag"
        case _:
            return "Ugyldig dag"  # Fanger alle andre tilfeller
    