# Your task is to create a Vampire class that stores a list of vampires (a coven, if you will).
# Every vampire has a name, age, an in_coffin boolean, and a drank_blood_today boolean.
class Vampire:

    coven = []
# __init__, which creates a new vampire and assigns values for each of its attributes

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

# Every day at sunset the vampires leave their coffins in search of blood.
# If they don't drink blood and get back to their coffins before sunrise, they die.


# create, which creates a new vampire and adds it to the coven
    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

# drink_blood, which sets a vampire's drank_blood_today boolean to true

    def drink_blood(self):
        self.drank_blood_today = True
        return self.drank_blood_today

# sunrise, which removes from the coven any vampires who are out of their coffins or
# who haven't drank any blood in the last day

    @classmethod
    def sunrise(cls):
        for num in range(0, len(cls.coven)):
            current_vampire = cls.coven[num]
            if not current_vampire.in_coffin or not current_vampire.drank_blood_today:
                Vampire.coven.remove(current_vampire)
        return Vampire.coven

# sunset, which sets drank_blood_today and in_coffin to false for the entire coven as
# they go out in search of blood

    @classmethod
    def sunset(cls):
        for num in range(0, len(cls.coven)):
            current_vampire = cls.coven[num]
            current_vampire.drank_blood_today = False
            current_vampire.in_coffin = False

# go_home, which sets a vampire's in_coffin boolean to true
    def go_home(self):
        self.in_coffin = True

vampire1 = Vampire.create("Frank", 12, True, True)
vampire2 = Vampire.create("Josie", 23, True, True)
vampire3 = Vampire.create("Ted", 2, False, True)
print(Vampire.coven)
print(len(Vampire.coven)) # 3
Vampire.sunrise() # vampire3 is removed
print(len(Vampire.coven)) # 2
Vampire.sunset() # turns everything false
print(vampire2.drank_blood_today) # false
print(vampire2.in_coffin) # false
print(vampire1.in_coffin) # false
print(vampire1.drank_blood_today) #false
vampire1.go_home()
print(vampire1.in_coffin) # true
