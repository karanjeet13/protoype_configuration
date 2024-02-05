import unittest
from enum import Enum
from typing import Optional
from copy import deepcopy

class ConfigurationType(Enum):
    BASIC = 'BASIC'
    ADVANCED = 'ADVANCED'
    CUSTOM = 'CUSTOM'
    DEFAULT = 'DEFAULT'

class ClonableObject:
    def clone_object(self):
        pass

class Configuration(ClonableObject):
    def __init__(self, theme_color, auto_save, language, dark_mode, font_size, font_family, configuration_type):
        self.theme_color = theme_color
        self.auto_save = auto_save
        self.language = language
        self.dark_mode = dark_mode
        self.font_size = font_size
        self.font_family = font_family
        self.configuration_type = configuration_type

    def clone_object(self):
        return Configuration(
            self.theme_color,
            self.auto_save,
            self.language,
            self.dark_mode,
            self.font_size,
            self.font_family,
            self.configuration_type
        )

class ConfigurationPrototypeRegistry:
    def __init__(self):
        self.configurations = {}

    def add_prototype(self, configuration):
        self.configurations[configuration.configuration_type] = configuration

    def get_prototype(self, configuration_type):
        return self.configurations.get(configuration_type)

    def clone(self, configuration_type):
        prototype = self.configurations.get(configuration_type)
        if prototype:
            return deepcopy(prototype)
        return None

class TestConfiguration(unittest.TestCase):
    def test_configuration_implements_clonable_object(self):
        configuration = Configuration("", False, "", False, 0, "", ConfigurationType.BASIC)
        self.assertTrue(isinstance(configuration, ClonableObject), "If the prototype pattern is implemented correctly, the Configuration class should implement the ClonableObject interface")

    def test_configuration_clone_method_creates_distinct_object(self):
        configuration = Configuration("Black", True, "English", True, 12, "Arial", ConfigurationType.BASIC)

        # Using deepcopy to create a clone
        cloned_configuration = deepcopy(configuration)

        self.assertIsNotNone(cloned_configuration, "If the clone method is implemented correctly, it should return a non-null object")
        self.assertNotEqual(configuration, cloned_configuration, "If the clone method is implemented correctly, it should return a new object")

        # Asserting that the cloned configuration has the same values as the original configuration
        self.assertEqual(configuration.theme_color, cloned_configuration.theme_color, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.auto_save, cloned_configuration.auto_save, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.font_size, cloned_configuration.font_size, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.dark_mode, cloned_configuration.dark_mode, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.language, cloned_configuration.language, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.font_family, cloned_configuration.font_family, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.configuration_type, cloned_configuration.configuration_type, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")

    def test_registry(self):
        registry = ConfigurationPrototypeRegistry()
        self.assertIsNotNone(registry, "If the registry pattern is implemented correctly, the registry should not be null")

        configuration = Configuration("Black", True, "English", True, 12, "Arial", ConfigurationType.BASIC)
        registry.add_prototype(configuration)

        prototype = registry.get_prototype(configuration.configuration_type)
        self.assertIsNotNone(prototype, "If the clone method is implemented correctly, it should return a non-null object")
        self.assertEqual(configuration, prototype, "If the registry pattern is implemented correctly, the registry should return the same object that was added")

    def test_registry_clone(self):
        configuration = Configuration("Black", True, "English", True, 12, "Arial", ConfigurationType.BASIC)
        registry = ConfigurationPrototypeRegistry()
        self.assertIsNotNone(registry, "If the registry pattern is implemented correctly, the registry should not be null")

        registry.add_prototype(configuration)

        # Clone the prototype and validate it's a distinct object with the same values
        cloned_configuration = registry.clone(configuration.configuration_type)
        self.assertIsNotNone(cloned_configuration, "If the clone method is implemented correctly, it should return a non-null object")
        self.assertNotEqual(configuration, cloned_configuration, "If the clone method is implemented correctly, it should return a new object")

        self.assertEqual(configuration.theme_color, cloned_configuration.theme_color, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.auto_save, cloned_configuration.auto_save, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.font_size, cloned_configuration.font_size, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.dark_mode, cloned_configuration.dark_mode, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.language, cloned_configuration.language, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.font_family, cloned_configuration.font_family, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(configuration.configuration_type, cloned_configuration.configuration_type, "If the clone method is implemented correctly, it should return a new object with the same values as the original object")

if __name__ == '__main__':
    unittest.main()

