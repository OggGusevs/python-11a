#2.Uzdevums
n = int(input("Ievadi skaitļi:"))
summa = 0
for i in range(1, 1 + n):
    summa += i
print("Skaitļu summa no 1 lidz n ir:", summa)

#3.Uzdevums
n = int(input("Ievadi skaitļi:"))
faktorials = 1
for i in range(1,1 + n):
    faktorials *= i
print("Skaitļu faktorials no 1 lidz n ir:", faktorials)

#4.Uzdevums
n = int(input("Ievadi skaitļi:"))
for i in range(n, -1, -1):
    print(i)
    
#5. Uzdevums
length = int(input("Lenght: "))
for i in range(length, 0 , -1):
    print("* " * i)

#6.Uzdevums
import random

min_skaitlis = 0
max_skaitlis = 100

izveles_skaitlis = random.randint(min_skaitlis, max_skaitlis)

print ("Uzminejiet skaitli no 0 lidz 100")

uzminets = False

while not uzminets:
    
    skaitlis = int(input("Ievadiet skaitli:"))
    
    if skaitlis < izveles_skaitlis:
        print("Lielaks")
        
    if skaitlis > izveles_skaitlis:
        print("Mazaks")
        
    if skaitlis == izveles_skaitlis:
        print ("Uzminets!")
      
        break
