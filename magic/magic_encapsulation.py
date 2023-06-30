class Wizard:
    def __init__(self, name, level, magic_points, elements):
        self.name = name
        self.level = level
        self.magic_points = magic_points
        self.elements = elements


class Magic:
    def __init__(self, name, element, cost):
        self._name = name
        self._element = element
        self._cost = cost

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    # Getter for element
    @property
    def element(self):
        return self._element

    # Setter for element
    @element.setter
    def element(self, value):
        if not isinstance(value, str):
            raise TypeError("Element must be a string.")
        self._element = value

    # Getter for cost
    @property
    def cost(self):
        return self._cost

    # Setter for cost
    @cost.setter
    def cost(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Cost must be a non-negative integer.")
        self._cost = value

    # Magic method for string representation
    def __str__(self):
        return f"Magic: {self._name}, Element: {self._element}, Cost: {self._cost}"

    # Magic method for formal string representation
    def __repr__(self):
        return f"Magic('{self._name}', '{self._element}', {self._cost})"

    # Magic method for '+' operator
    def __add__(self, other):
        if isinstance(other, Magic):
            return Magic(f"Combined spell: {self._name} and {other._name}",
                         f"{self._element} and {other._element}",
                         self._cost + other._cost)

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


# Now we can encapsulate Wizard related data and behaviors in the Wizard class, and Magic related data and behaviors
# in the Magic class.
# Magic's data attributes are now private (prepended with _), and are manipulated through the cast() method.
# The @property decorator is used to define getter methods for the name, element, and cost attributes.
# he @attribute_name.setter decorator is used to define setter methods for the name, element, and cost attributes.
# In these setters, we also perform some validation to ensure that the name and element are strings, and the cost
# is a non-negative integer.

# In our classes, we've used proper layering (separate classes for Wizard and Magic),
# transparency (clearly named attributes and methods), a
# nd consistency (similar functionality for different instances of the same class).
# However, we've also avoided over-abstracting by not breaking down the classes and their methods more than necessary.


if __name__ == '__main__':
    fireball = Magic("Fireball", "Fire", 50)
    print(fireball.name)  # Fireball
    fireball.name = "Super Fireball"
    print(fireball.name)  # Super Fireball
    fireball.cost = 60
    print(fireball.cost)  # 60
    #fireball.cost = -10  # ValueError: Cost must be a non-negative integer.

    fireball = Magic("Fireball", "Fire", 50)
    ice_shard = Magic("Ice Shard", "Water", 30)
    print(fireball)  # Magic: Fireball, Element: Fire, Cost: 50
    print(repr(fireball))  # Magic('Fireball', 'Fire', 50)

    # Operator overloading
    combined_spell = fireball + ice_shard
    print(combined_spell)  # Magic: Combined spell: Fireball and Ice Shard, Element: Fire and Water, Cost: 80

    # Many wizard can also cast Fireball
    gendalf = Wizard("Gendalf", 12, 130, ["Fire", "Earth", "Air"])
    fireball.cast(gendalf)  # Gendar has casted Fireball!
    saruman = Wizard("Saruman", 16, 120, ["Fire", "Earth", "Air"])
    fireball.cast(saruman)  # Saruman casts Fireball

