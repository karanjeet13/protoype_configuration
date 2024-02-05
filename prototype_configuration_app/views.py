from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

class ConfigurationType(Enum):
    BASIC = 'BASIC'
    ADVANCED = 'ADVANCED'
    CUSTOM = 'CUSTOM'
    DEFAULT = 'DEFAULT'

class ClonableObject(ABC):
    @abstractmethod
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

    def get_theme_color(self):
        return self.theme_color

    def get_auto_save(self):
        return self.auto_save

    def get_language(self):
        return self.language

    def get_dark_mode(self):
        return self.dark_mode

    def get_font_size(self):
        return self.font_size

    def get_font_family(self):
        return self.font_family

    def get_configuration_type(self):
        return self.configuration_type

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
        self.configurations[configuration.get_configuration_type()] = configuration

    def get_prototype(self, configuration_type):
        return self.configurations.get(configuration_type)

    def clone(self, configuration_type):
        prototype = self.configurations.get(configuration_type)
        if prototype:
            return prototype.clone_object()
        return None

