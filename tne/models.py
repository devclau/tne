from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
       db_table = "categorias"

class GLO_COMUNAS(models.Model):
    COMU_COD = models.CharField(primary_key=True, max_length=100)
    COMU_DES = models.CharField(max_length=20)
   

    class Meta:
        db_table = '"DELFOS"."GLO_COMUNAS"'
        verbose_name = 'GLO_COMUNAS'
        verbose_name_plural ='GLO_COMUNAS'

class T_TNE_SOLICITUDES(models.Model):
    FECHA_SOLICITUD = models.CharField(max_length=20)
    RUT = models.CharField(max_length=20)
    PERIODO_SOLICITUD = models.CharField(max_length=20, default=2023)
    INSCRIPCION = models.CharField(max_length=2)
    INSCRIPCION_PERIODO = models.CharField(max_length=5,null=True, blank=True )
    TNE_REVALIDAR = models.CharField(max_length=2)
    TNE_NUEVO = models.CharField(max_length=2)

    class Meta:

        db_table = '"DELFOS"."T$TNE_SOLICITUDES"'
        verbose_name = 'T$TNE_SOLICITUDES'
        verbose_name_plural ='T$TNE_SOLICITUDES'

