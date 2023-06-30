from magic.magic_encapsulation import Wizard, Magic
from magic.magic_inheritance import DarkMagic


class HealingMagic(Magic):
    def invoke_spell(self, wizard):
        print(f"{wizard.name} is casting {self._name}!")
        print(f"The spell uses the {self._element} element to heal!")


class SpellBook:
    def __init__(self):
        self._spells = []

    def add_spell(self, spell):
        self._spells.append(spell)

    def cast_spell(self, wizard, spell_name):
        for spell in self._spells:
            if spell._name == spell_name:
                spell.cast(wizard)
                return
        print(f"No spell named {spell_name} found in the spellbook.")

# HealingMagic is a subclass of Magic that overrides the invoke_spell method.
# This is polymorphism in action: a method with the same name behaves differently depending on the class of the
# object it's called on.

# SpellBook can handle any spell, regardless of its specific type (HealingMagic, ElementalMagic, etc), as long as it has
# a cast method. This is duck typing: SpellBook doesn't care about the actual type of the spell, only about what it can do.

# The Liskov Substitution Principle is respected here because all subclasses of Magic are usable anywhere a Magic
# object is expected.


if __name__ == '__main__':
    heal = HealingMagic("Heal", "Earth", 30)
    resurection = DarkMagic("Resurection", "Dark", 100)
    galadriel = Wizard("Galadriel", 20, 200, ["Fire", "Earth", "Dark"])

    spellbook = SpellBook()
    spellbook.add_spell(heal)
    spellbook.add_spell(resurection)

    spellbook.cast_spell(galadriel, "Heal")  # Galadriel casts Heal and uses the Earth element to heal
    resurection.cast(galadriel)  # Galadriel casts Resurection and uses the Dark element to resurrect
