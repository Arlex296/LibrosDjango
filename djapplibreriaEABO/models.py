# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from multiprocessing import context
from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'autores'


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40)
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'categorias'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=11)
    nombres = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cliente'


class Libros(models.Model):
    isbn = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=125)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categoria')
    precio = models.IntegerField()
    portada = models.CharField(max_length=100)
    cantidad_stock = models.IntegerField()
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'libros'


class PedidoCliente(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    numero_pedido = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    isbn = models.ForeignKey(Libros, models.DO_NOTHING, db_column='isbn')
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'pedido_cliente'
    
    def __str__(self):
        contexto=[self.isbn, self.id_cliente]
        return str(contexto)


class TblLibroPorAutor(models.Model):
    id_autor = models.IntegerField(primary_key=True)
    isbn = models.IntegerField()
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_libro_por_autor'
        unique_together = (('id_autor', 'isbn'),)



class Usuarios(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    id_cliente = models.IntegerField()
    correo = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'usuarios'
