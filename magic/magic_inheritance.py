from magic.magic_encapsulation import Wizard, Magic

class EnhancedMagic(Magic):
    def __init__(self, name, element, cost, enhancement_level):
        super().__init__(name, element, cost)
        self._enhancement_level = enhancement_level

    # Overriding the cast method
    def cast(self, wizard):
        # call the parent class's cast method
        super().cast(wizard)
        print(f"Enhanced power due to enhancement level {self._enhancement_level}!")

#This example follows the good practices mentioned:
# there's a clear "is-a" relationship between EnhancedMagic and Magic,
# and EnhancedMagic can be substituted for Magic without disrupting the program.
# Additionally, EnhancedMagic adds new behavior (the enhancement_level attribute and an enhanced cast method)


class DarkMagic(Magic):
    def cast(self, wizard):
        super().cast(wizard)
        print(f"{wizard.name} has casted dark magic!")


class ElementalMagic(Magic):
    def cast(self, wizard):
        super().cast(wizard)
        print(f"{wizard.name} has casted elemental magic!")


class DarkElementalMagic(ElementalMagic, DarkMagic):
    pass

# When cast is called on a DarkElementalMagic instance, it first looks for the method in DarkElementalMagic.
# Since it's not there, it then looks at the parent classes in the order they're listed in the class declaration.
# It finds the method in ElementalMagic and calls it. The method then calls super().cast(wizard),
# which looks for the method in DarkMagic. It finds it and calls it. The method then calls super().cast(wizard),
# which looks for the method in Magic. It finds it and calls it.


if __name__ == '__main__':
    lightning = EnhancedMagic("Lightning Bolt", "Air", 60, 2)
    ulinilorh = Wizard("Ulinilorh", 15, 100, ["Fire", "Earth", "Air"])
    lightning.cast(ulinilorh)  # Ulinilorh casts Lightning Bolt and shows enhanced power

    firestorm = DarkElementalMagic("Firestorm", "Fire", 80)
    ulinilorh = Wizard("Ulinilorh", 15, 100, ["Fire", "Earth", "Dark"])
    firestorm.cast(ulinilorh)  # Ulinilorh casts Firestorm and it's mentioned as dark magic
