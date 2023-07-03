from django.db import models
from django.core.exceptions import ValidationError

# Validación (debe tener 7 dígitos)
def validate_nroregistro(value):
    if len(value) != 7:
        raise ValidationError('El numero de registro del libro debe tener 7 dígitos.')

# Validación cantidad de días de préstamo del libro
def validate_prestamo_days(value):
    if value <= 0:
        raise ValidationError('Los días de préstamo deben ser mayores que 0.')

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    nroregistro = models.CharField(max_length=13, validators=[validate_nroregistro])
    cantidad_paginas = models.PositiveIntegerField()
    cantidad_copias = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    dias_prestamo = models.PositiveIntegerField(validators=[validate_prestamo_days])

    def __str__(self):
        return f"Prestamo del libro '{self.libro}'"

