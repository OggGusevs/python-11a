
#2.uzd
num1 = float(input("Ievadi pirmo skaitli: "))
num2 = float(input("Ievadi otro skaitli: "))

summa = num1 + num2
starpiba = num1 - num2
reizinajums = num1 * num2
dalijums = num1 / num2 if num2 != 0 else "Nedrīkst dalīt ar nulli!"

print("Summas:", summa)
print("Starpība:", starpiba)
print("Reizinājums:", reizinajums)
print("Dalījums:", dalijums)

#3.uzd
skaitlis = float(input("Ievadi skaitli: "))

if skaitlis > 0:
    print("Skaitlis ir pozitīvs.")
elif skaitlis < 0:
    print("Skaitlis ir negatīvs.")
else:
    print("Skaitlis ir nulle.")
    
    #5.uzd un 5.1.uzd
atzime = int(input("Ievadi atzīmi (no 1 līdz 10): "))

if atzime < 0 or atzime > 10:
    print("Nepareiza atzīme. Lūdzu, ievadi skaitli no 0 līdz 10.")
else:
    if 9 <= atzime <= 10:
        print("Līmenis: A")
    elif 7 <= atzime <= 8:
        print("Līmenis: B")
    elif 5 <= atzime <= 6:
        print("Līmenis: C")
    elif 3 <= atzime <= 4:
        print("Līmenis: D")
    elif 1 <= atzime <= 2:
        print("Līmenis: E")
        print("Līmenis: F")