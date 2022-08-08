from enum import Enum

class Payment_Type(Enum):

    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Débito"
    PIX = "Pix"
    DINHEIRO = "Dinheiro"
    TRANSFERENCIA = "Transferência bancária"   

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

