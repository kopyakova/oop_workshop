# Metaclass
class MetaWizard(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
            if name in cls._instances:
                raise ValueError(f"Wizard with name {name} already exists!")
        return super().__call__(*args, **kwargs)


class Wizard(metaclass=MetaWizard):
    def __init__(self, name):
        self.name = name
        self.magic_energy = 100
        self.__class__._instances[name] = self

    # Rest of the class stays the same...

# Here, MetaWizard is a metaclass. It overrides the __call__ method, which is called when an
# instance is created from a class (i.e., when the class is called like a function).

# MetaWizard maintains a dictionary of wizard instances _instances. When __call__ is invoked, it checks if a wizard
# with the provided name already exists. If it does, an error is raised; otherwise, a new instance is created as usual.