import os

def get_font_files(directory):
    """Returns a list of font files in the given directory."""
    return [f for f in os.listdir(directory) if f.lower().endswith(('.ttf', '.otf'))]
