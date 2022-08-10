import re

def is_city_valid(city):
    """Check if the city is valid / Verifica se a cidade é válida"""
    if any(char.isdigit() for char in city):
        return False
    else:
        return True

def is_zip_code_valid(zip_code):
    """Check if the Zip code is valid / Verifica se o CEP é válido"""
    standard = '[0-9]{5}-[0-9]{3}'
    response = re.findall(standard, zip_code)
    return response

def is_house_number_valid(house_number):
    """Check if the house number is valid / Verifica se o número do local é válido"""
    return house_number.isnumeric()