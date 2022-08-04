def name_isValid(name):
    """Check if the name is valid / Verifica se o nome é válido"""
    if any(char.isdigit() for char in name):
        return False
    else:
        return True