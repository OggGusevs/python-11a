import random

def speelu_kaulinu_simulacija(n):
    lielaka_summu = 0

    for i in range(1, n + 1):
        kaulins1 = random.randint(1, 6)
        kaulins2 = random.randint(1, 6)
        lielaka_vertiba = max(kaulins1, kaulins2)
        summa = kaulins1 + kaulins2
        print(f"Gājiens {i}: Kauliņš 1 = {kaulins1}, Kauliņš 2 = {kaulins2}, Lielākā vērtība = {lielaka_vertiba}, Summa = {summa}")

        if summa > lielaka_summu:
            lielaka_summu = summa

    print(f"Lielākā summa, kas tika uzmesta: {lielaka_summu}")

speelu_kaulinu_simulacija(10)

def uzminet_skaitli():
 
    sakums = 1
    beigas = 100
    izdomatais_skaitlis = random.randint(sakums, beigas)

    print(f"Dators ir iedomājies skaitli intervālā no {sakums} līdz {beigas}.")

    minesanas_reizes = 0
    while True:
        lietotaja_min = int(input("Ievadi savu minējumu: "))
        minesanas_reizes += 1

        if lietotaja_min < izdomatais_skaitlis:
            print("Lielāks")
        elif lietotaja_min > izdomatais_skaitlis:
            print("Mazāks")
        else:
            print("Uzminēts!")
            print(f"Tu uzminēji ar {minesanas_reizes} minējumiem.")
            break

uzminet_skaitli()
