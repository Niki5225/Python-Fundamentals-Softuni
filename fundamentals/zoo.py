class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "fish":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, type_lst):
        if type_lst == "mammal":
            return f"Mammals in {name_of_the_zoo}: {', '.join(self.mammals)}\nTotal animals: {len(self.mammals)}"
        elif type_lst == "fish":
            return f"Fishes in {name_of_the_zoo}: {', '.join(self.mammals)}\nTotal animals: {len(self.fishes)}"
        elif type_lst == "bird":
            return f"Birds in {name_of_the_zoo}: {', '.join(self.mammals)}\nTotal animals: {len(self.birds)}"


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number_animals = int(input())
for animal in range(number_animals - 1):
    current_animal = input().split(" ")
    specie = current_animal[0]
    typed = current_animal[1]
    zoo.add_animal(specie, typed)
type_print = input()
print(zoo.get_info(type_print))
