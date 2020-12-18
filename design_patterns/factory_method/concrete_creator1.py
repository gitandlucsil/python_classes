from creator import Creator
from concrete_product1 import ConcreteProduct1
"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""
class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factory_method(self):
        return ConcreteProduct1()

