from enum import Enum


class Breed_Type(Enum):

    AKITA = "Akita"
    AMERICAN_BULLY = "American Bully"
    AMERICAN_STAFFORDSHIRE_TERRIER = "American staffordshire terrier"
    BASENJI = "Basenji"
    BASSET_HOUND = "Basset hound"
    BEAGLE = "Beagle"
    BERNESE = "Bernese"
    BICHON_FRISE = "Bichon frise"
    BOIADEIRO_AUSTRALIANO = "Boiadeiro australiano"
    BORDER_COLLIE = "Border collie"
    BORZOI = "Borzoi"
    BOSTON_TERRIER = "Boston terrier"
    BOXER = "Boxer"
    BULDOGUE_FRANCES = "Buldogue francês"
    BULL_TERRIER = "Bull terrier"
    CANE_CORSO = "Cane corso"
    CAVALIER_KING_CHARLES_SPANIEL = "Cavalier king charles spaniel"
    CHIHUAHUA = "Chihuahua"
    CHOW_CHOW = "Chow chow"
    COCKER_SPANIEL_INGLES = "Cocker spaniel inglês"
    CORGI = "Corgi"
    DACHSHUND = "Dachshund"
    DALMATA = "Dálmata"
    DOBERMAN = "Doberman"
    DOGO_ARGENTINO = "Dogo argentino"
    DOGUE_ALEMAO = "Dogue alemão"
    DOGUE_DE_BORDEAUX = "Dogue de Bordeaux"
    FILA_BRASILEIRO = "Fila brasileiro"
    FOX_PAULISTINHA = "Fox paulistinha"
    GALGUINHO_ITALIANO = "Galguinho italiano"
    GOLDEN_RETRIEVER = "Golden retriever"
    GREYHOUND_OU_GALGO_INGLES = "Greyhound ou Galgo inglês"
    HUSKY_SIBERIANO = "Husky siberiano"
    JACK_RUSSEL_TERRIER = "Jack russel terrier"
    LABRADOODLE = "Labradoodle"
    LABRADOR_RETRIEVER = "Labrador retriever"
    LHASA_APSO = "Lhasa apso"
    LULU_DA_POMERANIA = "Lulu da Pomerânia"
    MALAMUTE_DO_ALASCA = "Malamute do alasca"
    MALTES_OU_BICHON_MALTES = "Maltês ou Bichon Maltês"
    MASTIFF_INGLES = "Mastiff inglês"
    MASTIM_NAPOLITANO = "Mastim Napolitano"
    MASTIM_TIBETANO = "Mastim tibetano"
    PAPILLON = "Papillon"
    PASTOR_ALEMAO = "Pastor alemão"
    PASTOR_AUSTRALIANO = "Pastor australiano"
    PASTOR_BELGA = "Pastor Belga"
    PASTOR_DE_SHETLAND = "Pastor de Shetland"
    PASTOR_DE_CAUCASO = "Pastor de Cáucaso"
    PASTOR_MAREMANO_ABRUZES = "Pastor Maremano Abruzes"
    PASTOR_SUICO = "Pastor Suiço"
    PEQUINES = "Pequinês"
    PINSCHER_MINIATURA = "Pinscher miniatura"
    PIT_BULL = "Pit bull"
    POINTER_INGLES = "Pointer Inglês"
    POODLE = "Poodle"
    POODLE_TOY = "Poodle Toy"
    PUG = "Pug"
    ROTTWEILER = "Rottweiler"
    ROUGH_COLLIE = "Rough Collie"
    SAMOIEDA = "Samoieda"
    SAO_BERNARDO = "São bernardo"
    SCHNAUZER = "Schnauzer"
    SETTER_IRLANDES = "Setter Irlandês"
    SHAR_PEI = "Shar-pei"
    SHIBA = "Shiba"
    SHIH_TZU = "Shih tzu"
    SPITZ_JAPONES = "Spitz Japonês"
    STAFFORDSHIRE_BULL_TERRIER = "Staffordshire bull terrier"
    TERRA_NOVA = "Terra nova"
    VIRA_LATA = "Vira-lata"
    WEIMARANER = "Weimaraner"
    WEST_HIGHLAND_WHITE_TERRIER = "West Highland White Terrier"
    WHIPPET = "Whippet"
    YORKSHIRE_TERRIER = "Yorkshire Terrier"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Size_Type(Enum):

    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class Gender_Type(Enum):

    M = "Masculino"
    F = "Feminino"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Color_Type(Enum):

    ALBINO = "Albino"
    AMARELO = "Amarelo"
    AZUL = "Azul"
    BRANCO = "Branco"
    CINZA = "Cinza"
    DOURADO = "Dourado"
    PRETO = "Preto"
    MARROM = "Marrom"
    VERMELHO = "Vermelho"
    PRETO_BRANCO = "Preto/Branco"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
