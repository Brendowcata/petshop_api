from enum import Enum


class States_Type(Enum):
    
    SC = "Santa Catarina"
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapa"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceara"
    ES = "Espirito Santo"
    GO = "Goias"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Para"
    PB = "Paraiba"
    PE = "Pernambuco"
    PI = "Piaui"
    RJ = "Rio de Janeiro"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RO = "Rondônia"
    RR = "Roraima"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"
    DF = "Distrito Federal"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

