from enum import Enum

class Clipping_Type(Enum):

    SEM_SERVICO = "Sem Serviço"
    TOSA_TESOURA = "Tosa na Tesoura"
    TOSA_MAQUINA = "Tosa na Máquina"
    TOSA_BEBE = "Tosa Bebê"
    TOSA_RACA = "Tosa de Raça"
    TOSA_VERAO = "Tosa Verão"
    TOSA_HIGIENICA = "Tosa Higiênica"
    TOSA_ESTETICA = "Tosa Estética"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Dyeing_Type(Enum):

    SEM_SERVICO = "Sem Serviço"
    VERMELHO = "Vermelho"
    AMARELO = "Amarelo"
    AZUL = "Azul"
    VERDE = "Verde"
    LARANJA = "Laranja"
    ROXO = "Roxo"
    ROSA = "Rosa"
    BRANCO = "Branco"
    PRETO = "Preto"
    MARROM = "Marrom"
    CINZA = "Cinza"
    DOURADO = "Dourado"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
