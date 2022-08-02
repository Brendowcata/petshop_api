from django.db import models
from customer.models import CustomerModel
import uuid


class AnimalModel(models.Model):

    SIZES = (
        ('Pequeno', 'Pequeno'),
        ('Medio', 'Médio'),
        ('Grande', 'Grande')
    )

    BREEDS = (
        ('Akita', 'Akita'),
        ('American Bully', 'American Bully'),
        ('American staffordshire terrier', 'American staffordshire terrier'),
        ('Basenji', 'Basenji'),
        ('Basset hound', 'Basset hound'),
        ('Beagle', 'Beagle'),
        ('Bernese', 'Bernese'),
        ('Bichon frise', 'Bichon frisé'),
        ('Boiadeiro australiano', 'Boiadeiro australiano'),
        ('Border collie', 'Border collie'),
        ('Borzoi', 'Borzoi'),
        ('Boston terrier', 'Boston terrier'),
        ('Boxer', 'Boxer'),
        ('Buldogue frances', 'Buldogue francês'),
        ('Bull terrier', 'Bull terrier'),
        ('Cane corso', 'Cane corso'),
        ('Cavalier king charles spaniel', 'Cavalier king charles spaniel'),
        ('Chihuahua', 'Chihuahua'),
        ('Chow chow', 'Chow chow'),
        ('Cocker spaniel ingles', 'Cocker spaniel inglês'),
        ('Corgi', 'Corgi'),
        ('Dachshund', 'Dachshund'),
        ('Dalmata', 'Dálmata'),
        ('Doberman', 'Doberman'),
        ('Dogo argentino', 'Dogo argentino'),
        ('Dogue alemao', 'Dogue alemao'),
        ('Dogue de Bordeaux', 'Dogue de Bordeaux'),
        ('Fila brasileiro', 'Fila brasileiro'),
        ('Fox paulistinha', 'Fox paulistinha'),
        ('Galguinho italiano', 'Galguinho italiano'),
        ('Golden retriever', 'Golden retriever'),
        ('Greyhound ou Galgo ingles', 'Greyhound ou Galgo inglês'),
        ('Husky siberiano', 'Husky siberiano'),
        ('Jack russel terrier', 'Jack russel terrier'),
        ('Labradoodle', 'Labradoodle'),
        ('Labrador retriever', 'Labrador retriever'),
        ('Lhasa apso', 'Lhasa apso'),
        ('Lulu da Pomerania', 'Lulu da Pomerânia'),
        ('Malamute do alasca', 'Malamute do alasca'),
        ('Maltês ou Bichon Maltes', 'Maltês ou Bichon Maltês'),
        ('Mastiff ingles', 'Mastiff inglês'),
        ('Mastim Napolitano', 'Mastim Napolitano'),
        ('Mastim tibetano', 'Mastim tibetano'),
        ('Papillon', 'Papillon'),
        ('Pastor alemao', 'Pastor alemão'),
        ('Pastor alemao', 'Pastor australiano'),
        ('Pastor Belga', 'Pastor Belga'),
        ('Pastor de Shetland', 'Pastor de Shetland'),
        ('Pastor do Caucaso', 'Pastor do Cáucaso'),
        ('Pastor Maremano Abruzes', 'Pastor Maremano Abruzes'),
        ('Pastor Suiço', 'Pastor Suiço'),
        ('Pequines', 'Pequinês'),
        ('Pinscher miniatura', 'Pinscher miniatura'),
        ('Pit bull', 'Pit bull'),
        ('Pointer Ingles', 'Pointer Inglês'),
        ('Poodle', 'Poodle'),
        ('Poodle Toy', 'Poodle Toy'),
        ('Pug', 'Pug'),
        ('Rottweiler', 'Rottweiler'),
        ('Rough Collie', 'Rough Collie'),
        ('Samoieda', 'Samoieda'),
        ('Sao bernardo', 'São bernardo'),
        ('Schnauzer', 'Schnauzer'),
        ('Setter Irlandes', 'Setter Irlandês'),
        ('Shar-pei', 'Shar-pei'),
        ('Shiba', 'Shiba'),
        ('Shih tzu', 'Shih tzu'),
        ('Spitz Japones', 'Spitz Japonês'),
        ('Staffordshire bull terrier', 'Staffordshire bull terrier'),
        ('Terra nova', 'Terra nova'),
        ('Vira-lata', 'Vira-lata'),
        ('Weimaraner', 'Weimaraner'),
        ('West Highland White Terrier', 'West Highland White Terrier'),
        ('Whippet', 'Whippet'),
        ('Yorkshire Terrier', 'Yorkshire Terrier')
    )

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    name = models.CharField(
        max_length=100, 
        db_column="NAME"
        ) #Nome

    breed = models.CharField(
        max_length=30,
        choices=BREEDS, 
        blank=False, 
        null=False, 
        db_column="BREED",
        ) #Raça

    size = models.CharField(
        max_length=7,
        choices=SIZES, 
        blank=False, 
        null=False, 
        db_column="SIZE"
        ) #Tamanho

    color = models.CharField(
        max_length=20,
        db_column="COLOR"
        ) #Cor

    observation = models.TextField(
        blank=True,
        db_column="OBSERVATION"
        ) #Observação

    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE, 
        null=False
        ) #Cliente
    
    class Meta:
        db_table = "ANIMAL"
        verbose_name = "animal"
        verbose_name_plural = "animals"


    def __str__(self) -> str:
        return f"{self.name}, {self.customer}"