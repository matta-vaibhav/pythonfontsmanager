import os
import time
from font_registry import FontRegistry
from constants import FONT_DIRECTORY

class FontOperations:
    """Handles font registration and deregistration while tracking time."""

    def __init__(self):
        self.font_registry = FontRegistry()

    def register_fonts(self):
        """Registers fonts and logs time at checkpoints."""
        fonts = [f for f in os.listdir(FONT_DIRECTORY) if f.lower().endswith(('.ttf', '.otf'))]

        registered_count = 0

        for font in fonts:
            font_path = os.path.join(FONT_DIRECTORY, font)
            self.font_registry.register_font(font, font_path)
            registered_count += 1

        print(f"{registered_count} Fonts registered.")

    def deregister_fonts(self):
        """Deregisters fonts and logs time at checkpoints."""
        fonts = [f for f in os.listdir(FONT_DIRECTORY) if f.lower().endswith(('.ttf', '.otf'))]

        deregistered_count = 0

        for font in fonts:
            self.font_registry.deregister_font(font)
            deregistered_count += 1

        print(f"{deregistered_count} Fonts De-Registered.")
        
