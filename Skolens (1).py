class Skolens:
    id_counter = 1

    def __init__(self, name, surname, sekmes):
        self.name = name
        self.surname = surname
        self.sekmes = sekmes
        self.id = Skolens.id_counter
        Skolens.id_counter += 1

    def pievienot_jauno_atzime(self, atzime):
        self.sekmes.append(atzime)

    def videja_atzime(self):
        return sum(self.sekmes) / len(self.sekmes)

    def __str__(self):
        return f"{self.id} - {self.name} {self.surname} - {self.sekmes}"


class Skola:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.skoleni = []

    def pievienot_skolenu(self, skolens):
        self.skoleni.append(skolens)

    def paradit_visus_skolenus(self):
        for skolens in self.skoleni:
            print(skolens)

    def labakais(self):
        return max(self.skoleni, key=lambda s: s.videja_atzime())


skola = Skola("Ventspils 6.vidusskola")

skolens1 = Skolens("Daniels", "Zamuelis", [9, 8, 10])
skolens2 = Skolens("Mārtiņs", "Bibļivs", [7, 6, 8])
skolens3 = Skolens("Elza", "Bērziņa", [10, 10, 9])

skola.pievienot_skolenu(skolens1)
skola.pievienot_skolenu(skolens2)
skola.pievienot_skolenu(skolens3)

print("Visi skolēni:")
skola.paradit_visus_skolenus()

skolens1.pievienot_jauno_atzime(10)
print("\nDaniels pēc jaunas atzīmes:")
print(skolens1)

print("\nVidējā atzīme Elzai:", skolens1.videja_atzime())

print("\nLabākais skolēns Elza:", skolens1.videja_atzime())