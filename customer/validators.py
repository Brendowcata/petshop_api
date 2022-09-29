import re
from urllib import response
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
    standard = r'\(\d{2}\) \d{4}-\d{4}'
    response = re.findall(standard, telephone)
    return response

def is_phone_number_valid(phone_number):
    """Check if the Phone_number is valid / Verifica se o número de celular é válido"""
    standard = r'\(\d{2}\) \d{5}-\d{4}'
    response = re.findall(standard, phone_number)
    return response

def is_cpf_valid(cpf):
    """Check if the cpf is valid / Verifica se o cpf é válido"""
    standard = r'\d{3}.\d{3}.\d{3}-\d{2}'
    response = re.findall(standard, cpf)
    cpf_valid = CPF()
    if (cpf_valid.validate(cpf)):
        return response