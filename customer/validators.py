import re
from validate_docbr import CPF

def is_name_valid(name):
    """Check if the name is valid / Verifica se o nome é válido"""
    if any(char.isdigit() for char in name):
        return False
    else:
        return True

def is_telephone_valid(telephone):
    """Check if the Telephone is valid / Verifica se o Telefone é válido"""
    if telephone == "":
        return True
    standard = '\([0-9]{2}\) [0-9]{4}-[0-9]{4}'
    response = re.findall(standard, telephone)
    return response

def phone_number_isValid(phone_number):
    """Check if the Phone_number is valid / Verifica se o número de celular é válido"""
    standard = '\([0-9]{2}\) [0-9]{5}-[0-9]{4}'
    response = re.findall(standard, phone_number)
    return response

def is_cpf_valid(cpf):
    """Check if the cpf is valid / Verifica se o cpf é válido"""
    standard = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
    response = re.findall(standard, cpf)
    cpf_valid = CPF()
    return cpf_valid.validate(cpf)