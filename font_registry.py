import winreg
from constants import *

class FontRegistry:
    """Handles Windows Registry operations related to fonts."""

    @staticmethod
    def get_active_fonts():
        """Fetches the current count of registered fonts from the Windows Registry."""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, FONT_REGISTRY_PATH) as key:
                font_count = winreg.QueryInfoKey(key)[0]  # Number of values (fonts)
            return font_count
        except Exception as e:
            print(f"Error fetching font count: {e}")
            return 0

    @staticmethod
    def register_font(font_name, font_path):
        """Registers a font in the Windows Registry."""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, FONT_REGISTRY_PATH, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, font_name, 0, winreg.REG_SZ, font_path)
        except Exception as e:
            print(f"Error registering font {font_name}: {e}")

    @staticmethod
    def deregister_font(font_name):
        """Deregisters a font from the Windows Registry."""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, FONT_REGISTRY_PATH, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, font_name)
        except FileNotFoundError:
            print(f"Font {font_name} not found in the registry.")
        except Exception as e:
            print(f"Error deregistering font {font_name}: {e}")
