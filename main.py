from font_operations import FontOperations

if __name__ == "__main__":
    font_ops = FontOperations()

    print("\n--- Registering Fonts ---")
    font_ops.register_fonts()

    print("\n--- Deregistering Fonts ---")
    font_ops.deregister_fonts()
