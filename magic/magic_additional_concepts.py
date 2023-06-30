class Wizard:
    total_wizards = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        self.magic_energy = 100
        Wizard.total_wizards += 1

    @classmethod
    def show_total_wizards(cls):
        print(f"There are currently {cls.total_wizards} wizards.")

    @staticmethod
    def create_spell(name, element, energy_cost):
        return Magic(name, element, energy_cost)


# Decorators
def log_cast(func):
    def wrapper(self, wizard):
        print(f"{wizard.name} is about to cast a spell!")
        func(self, wizard)
        print(f"{wizard.name} has finished casting a spell!")
    return wrapper


class Magic:
    def __init__(self, name, element, energy_cost):
        self._name = name
        self._element = element
        self._energy_cost = energy_cost

    @log_cast
    def cast(self, wizard):
        if wizard.magic_energy >= self._energy_cost:
            wizard.magic_energy -= self._energy_cost
            self.invoke_spell(wizard)
        else:
            print(f"{wizard.name} does not have enough energy to cast {self._name}!")

    def invoke_spell(self, wizard):
        print(f"{wizard.name} is casting {self._name}! The spell uses the {self._element} element.")


if __name__ == '__main__':
    fireball = Magic("Fireball", "Fire", 50)
    gandalf = Wizard("Gandalf")
    fireball.cast(gandalf)
    Wizard.show_total_wizards()
