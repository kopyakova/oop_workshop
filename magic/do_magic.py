# import random module
import random

# define a global dictionary of magic spells
magic_spells = {
    'fireball': ['Fire Element', 50],
    'ice shard': ['Water Element', 40],
    'earthquake': ['Earth Element', 60],
    'wind blade': ['Air Element', 30]
}


# define a function that allows a wizard to do magic
def do_magic(wizard, spell_name):
    if wizard['level'] < 10:
        print('Wizard level is too low to perform any magic.')
        return
    if spell_name not in magic_spells.keys():
        print('Invalid spell name.')
        return
    if magic_spells[spell_name][1] > wizard['magic_points']:
        print('Wizard does not have enough magic points to perform this spell.')
        return
    if magic_spells[spell_name][0] not in wizard['elements']:
        print('Wizard cannot use this element.')
        return

    # spell is successful
    wizard['magic_points'] -= magic_spells[spell_name][1]
    print(f"{wizard['name']} has casted {spell_name}!")
    if random.random() < 0.1:
        print('Critical hit!')
        wizard['level'] += 1

# It heavily relies on a dictionary of magic spells which is defined globally.
# This is not ideal as any part of the script could modify this global variable and cause unexpected behaviour.
# The do_magic() function modifies the wizard's details in place, which makes it harder to predict its outcome.
# Also, if we wanted to have more than one wizard, it'd be quite hard to manage their data.
# The 'wizard' is a dictionary, and the function expects it to have very specific keys.
# This is error-prone and hard to maintain.


if __name__ == '__main__':
    wizard = {
        'name': 'Gandalf',
        'level': 15,
        'magic_points': 100,
        'elements': ['Fire Element', 'Earth Element']
    }

    do_magic(wizard, 'fireball')
    