import os
import time
from font_registry import FontRegistry
from constants import FONT_DIRECTORY, CHECKPOINTS

class FontOperations:
    """Handles font registration and deregistration while tracking time."""

    def __init__(self):
        self.font_registry = FontRegistry()

    def register_fonts(self):
        """Registers fonts and logs time at checkpoints."""
        fonts = [f for f in os.listdir(FONT_DIRECTORY) if f.lower().endswith(('.ttf', '.otf'))]
        initial_count = self.font_registry.get_active_fonts()

        registered_count = 0
        start_time = time.time()

        for font in fonts:
            font_path = os.path.join(FONT_DIRECTORY, font)
            self.font_registry.register_font(font, font_path)
            registered_count += 1

            if registered_count in CHECKPOINTS:
                elapsed_time = time.time() - start_time
                final_count = self.font_registry.get_active_fonts()
                print(f"Time taken to register {registered_count} fonts: {elapsed_time:.2f} sec")
                print(f"Total Fonts before: {initial_count}, after: {final_count}, difference: {final_count - initial_count}")

    def deregister_fonts(self):
        """Deregisters fonts and logs time at checkpoints."""
        fonts = [f for f in os.listdir(FONT_DIRECTORY) if f.lower().endswith(('.ttf', '.otf'))]
        initial_count = self.font_registry.get_active_fonts()

        deregistered_count = 0
        start_time = time.time()

        for font in fonts:
            self.font_registry.deregister_font(font)
            deregistered_count += 1

            if deregistered_count in CHECKPOINTS:
                elapsed_time = time.time() - start_time
                final_count = self.font_registry.get_active_fonts()
                print(f"Time taken to deregister {deregistered_count} fonts: {elapsed_time:.2f} sec")
                print(f"Total Fonts before: {initial_count}, after: {final_count}, difference: {initial_count - final_count}")
