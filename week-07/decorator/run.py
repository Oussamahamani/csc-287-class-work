"""Run the example decorator pattern."""

from component import SecuritySystem
from decorator import EncryptionDecorator
from decorator import JapaneseDecorator
from decorator import UpperCaseDecorator


def get_message(component):
    """Get the latest component message."""
    print(f"MESSAGE: {component.get_message()}")


# Here we try the original component
simple = SecuritySystem()
get_message(simple)

# Then we wrap the original component with encryption
encrypt_decorator = EncryptionDecorator(simple)
get_message(encrypt_decorator)

# Wrap the original component with Japanese translation
japanese_decorator = JapaneseDecorator(simple)
get_message(japanese_decorator)


# Nesting
nested_decorators = EncryptionDecorator(japanese_decorator)
get_message(nested_decorators)

triple_nested_decorator = UpperCaseDecorator(nested_decorators)
print("printing nested")
get_message(triple_nested_decorator)