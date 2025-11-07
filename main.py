# 1-misol
def teskari_royxat(royxat):
    return royxat[::-1]

royxat = list(map(int, input("Raqamlar ro'yxatini kiriting (bo'shliq bilan ajratib): ").split()))
natija = teskari_royxat(royxat)
print(f"Teskari ro'yxat: {natija}")


# 2-misol
def kalkulyator():
    son1 = float(input("Birinchi sonni kiriting: "))
    amal = input("Amalni kiriting (+, -, *, /): ")
    son2 = float(input("Ikkinchi sonni kiriting: "))

    if amal == '+':
        return son1 + son2
    elif amal == '-':
        return son1 - son2
    elif amal == '*':
        return son1 * son2
    elif amal == '/':
        if son2 != 0:
            return son1 / son2
        else:
            return "Nolga bo'lish mumkin emas!"
    else:
        return "Noto'g'ri amal!"

natija = kalkulyator()
print(f"Natija: {natija}")


# 3-misol
def sozlar_soni(satr):
    sozlar = satr.split()
    return len(sozlar)

satr = input("Satr kiriting: ")
natija = sozlar_soni(satr)
print(f"So'zlar soni: {natija}")


# 4-misol
def juft_ikkilantir(royxat):
    natija = []
    for son in royxat:
        if son % 2 == 0:
            natija.append(son * 2)
        else:
            natija.append(son) 
    return natija

royxat = list(map(int, input("Raqamlar ro'yxatini kiriting (bo'shliq bilan ajratib): ").split()))
natija = juft_ikkilantir(royxat)
print(f"Natija: {natija}")

# 5-misol
def kalitlar_royxat(lugat):
    return list(lugat.keys())

lugat = {'ism': 'Ali', 'yosh': 25, 'shahar': 'Toshkent'}
natija = kalitlar_royxat(lugat)
print(f"Kalitlar ro'yxati: {natija}")





