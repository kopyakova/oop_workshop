from abc import ABC, abstractmethod

from magic.magic_encapsulation import Wizard


class Magic(ABC):
    def __init__(self, name, element, cost):
        self._name = name
        self._element = element
        self._cost = cost

    @abstractmethod
    def invoke_spell(self, wizard):
        pass

    def cast(self, wizard):
        if wizard.level < 10:
            print('Wizard level is too low to perform any magic.')
            return
        if self._cost > wizard.magic_points:
            print('Wizard does not have enough magic points to perform this spell.')
            return
        if self._element not in wizard.elements:
            print('Wizard cannot use this element.')
            return

        # spell is successful
        wizard.magic_points -= self._cost
        print(f"{wizard.name} has casted {self._name}!")


class Elemental(ABC):
    @abstractmethod
    def invoke_element(self):
        pass


class ElementalMagic(Magic, Elemental):
    def invoke_spell(self, wizard):
        print(f"{wizard.name} is casting {self._name}!")
        self.invoke_element()

    def invoke_element(self):
        print(f"The power of the {self._element} element is invoked!")


# Magic is an abstract base class (ABC) that declares an abstract method invoke_spell.
# This method is a placeholder that doesn't do anything in Magic but needs to be implemented by any subclass.
# Elemental is an abstract base class that serves as an interface. It promises the invoke_element method.
# ElementalMagic is a concrete class that inherits from both Magic and Elemental.
# It provides an implementation for both invoke_spell and invoke_element.
# Now every magic spell that is a subclass of Magic has to implement the invoke_spell method.
# If it's also a subclass of Elemental, it has to implement the invoke_element method as well.


if __name__ == '__main__':
    fireball = ElementalMagic("Fireball", "Fire", 50)
    gandalf = Wizard("Gandalf", 15, 100, ["Fire", "Earth", "Air"])
    fireball.cast(gandalf)  # Gandalf casts Fireball and invokes the power of the Fire element

