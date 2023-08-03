
from distutils.log import error
from multiprocessing import context
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from djapplibreriaEABO.models import Autores
from djapplibreriaEABO.models import Categorias
from djapplibreriaEABO.models import Cliente
from djapplibreriaEABO.models import Libros
from djapplibreriaEABO.models import Libros
from djapplibreriaEABO.models import TblLibroPorAutor
from djapplibreriaEABO.models import PedidoCliente
from djapplibreriaEABO.models import AuthUser
from django.core.files.storage import FileSystemStorage

from django.shortcuts import redirect, render




# Create your views here.


def index (request):
    libros= Libros.objects.all()
    cate= Categorias.objects.all()
    contexto = {'libros':libros,'cate':cate}
   
    return render(request, "djapplibreriaEABO/index.html",contexto)




def index2 (request):
    return render(request, "djapplibreriaEABO/index2.html")

   
   
# AUTORESSSS) 
    

def muestra_frm_aut(request):
    autores = Autores.objects.all()
    contexto = {'autore':autores}
    return render(request, "djapplibreriaEABO/form_autores.html",contexto )

def frm_autores(request):
    if request.user.is_authenticated:   
        
     return render(request, "djapplibreriaEABO/form_autores.html")
    else:
        return render(request, "djapplibreriaEABO/login.html")

def procesar_autor(request):
    
    
    nombres= request.POST ['nombres']
    apellidos = request.POST ['apellidos']
    estado = request.POST ['estado']
    
   
    
 
    
    autor = Autores()
    
    autor.nombres = nombres  
    autor.apellidos = apellidos  
    autor.estado = estado  
    
   
    
    autor.save()
    return redirect(listado_autores)

def eliminar_autor(request, id_autor):
    autor = Autores.objects.get(pk=id_autor)
    autor.delete()
#    return HttpResponse("llegamos aqui con el id" + str(id_aprendiz))
    return redirect(listado_autores)
 
 
def listado_autores(request):
    autor =Autores.objects.all()
    contexto = {'autores': autor}
    if request.user.is_authenticated:  
     return render(request,"djapplibreriaEABO/datos_autor.html",contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")


def update_autore(request, id_autor):
    autor = Autores.objects.filter(pk= id_autor).first()
    contexto = {
    'autor': autor}
    return render(request, "djapplibreriaEABO/editar_autor.html",contexto)

  
def updaterecord_autores(request, id_autor):
    autor = Autores.objects.filter(pk= id_autor).first()
    nombres= request.POST ['nombres']
    apellidos = request.POST ['apellidos']
    estado = request.POST ['estado']
   
    autor.nombres = nombres  
    autor.apellidos = apellidos  
    autor.estado = estado  
    
    autor.save()
    return redirect(listado_autores)


   
    
    
     # CATEGORIASSSSSSSSSSSS) 

      
     
     
def Formulario_datos_categorias(request):
        # return render(request, " edwinapp/Formulario.html")
   cate = ()
   cate.id_categoria = request.POST['id_categoria']
   cate.categoria = request.POST['categoria']
   cate.estado = request.POST['estado']
    
    
   cate.save()
   categorias = Categorias.objects.all()

   contexto = {'categorias': categorias}

    
    # return HttpResponse("llegamos aqui")
   return render(request, "djapplibreriaEABO/datos_categorias.html", contexto)


def Formulario_categorias(request):
    cate = Categorias()
    cate.usuario = request.POST['usuario']
    cate.clave = request.POST['clave']
    id_categoria = int(request.POST['id_categoria'])
    apr=Categorias.objects.get(id_categoria=id_categoria)
    
    cate.correo = request.POST['correo']

    cate.save()

    categorias = Autores.objects.all()

    contexto = {'categorias': categorias}
        #return HttpResponse('ok')
    return render(request, "djapplibreriaEABO/datos_categorias.html", contexto)


def muestra_frm_categ(request):
    categorias = Categorias.objects.all()
    contexto = {'categorias':categorias}
    if request.user.is_authenticated: 
      return render(request, "djapplibreriaEABO/form_categorias.html",contexto )
    else:
            return render(request, "djapplibreriaEABO/login.html")
        
def frm_categorias(request):
    if request.user.is_authenticated:   
       return render(request, "djapplibreriaEABO/form_categorias.html")
    else:
        return render(request, "djapplibreriaEABO/login.html")


def procesar_categoria(request):
    
    # id_categoria= request.POST ['id_categoria']
    categoria= request.POST ['categoria']
    estado = request.POST ['estado']
    
   
    
 
    
    cate = Categorias()
    # cate.id_categoria = id_categoria
    cate.categoria = categoria  
    cate.estado = estado  
    
   
    
    cate.save()
    return redirect(listado_categorias)

def eliminar_categorias(request, id_categoria):
    categoria = Categorias.objects.get(pk=id_categoria)
    categoria.delete()
#    return HttpResponse("llegamos aqui con el id" + str(id_aprendiz))
    return redirect(listado_categorias)
 
 
def listado_categorias(request):
    cate =Categorias.objects.all()
    contexto = {'categorias': cate}
    if request.user.is_authenticated:  
       return render(request,"djapplibreriaEABO/datos_categoria.html",contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")




def update_categorias(request, id_categoria):
    cate = Categorias.objects.filter(pk= id_categoria).first()
    contexto = {
    'cate': cate
    }
    
    return render(request, "djapplibreriaEABO/editar_categorias.html",contexto)
  

def updaterecord_categorias(request, id_categoria):

    cate = Categorias.objects.filter(pk= id_categoria).first()

    cate.categoria = request.POST['categoria']
    cate.estado = request.POST['estado']
    cate.save()

    return redirect(listado_categorias)    
    
   # CLIENTESSSSSSSSSSSSSSS)    
  
     
def Formulario_datos_cliente(request):
        # return render(request, " edwinapp/Formulario.html")
   cliente = ()
   
   cliente. identificacion = request.POST[' identificacion']
   cliente. nombres = request.POST[' nombres']
   cliente.  apellido = request.POST[' apellido']
   cliente. telefono = request.POST[' telefono']
   cliente. direccion = request.POST[' direccion']
   cliente. correo_electronico = request.POST[' correo_electronico']
   cliente.estado = request.POST['estado']
    
    
   cliente.save()
   clientes = Cliente.objects.all()

   contexto = {'clientes': clientes}

    
    # return HttpResponse("llegamos aqui")
   return render(request, "djapplibreriaEABO/datos_clien.html", contexto)



def Formulario_clientes(request):
    cliente = Cliente()
    cliente.usuario = request.POST['usuario']
    cliente.clave = request.POST['clave']
    id_cliente = int(request.POST['id_cliente'])
    apr=Cliente.objects.get(id_cliente=id_cliente)
    
    cliente.correo = request.POST['correo']

    cliente.save()

    clientes = Cliente.objects.all()

    contexto = {'clientes': clientes}
        #return HttpResponse('ok')
    return render(request, "djapplibreriaEABO/datos_clien.html", contexto)


def muestra_frm_cliente(request):
    cliente = Cliente.objects.all()
    contexto = {'cliente':cliente}
    return render(request, "djapplibreriaEABO/form_cliente.html",contexto )

def frm_clientes(request):
    if request.user.is_authenticated:
      return render(request, "djapplibreriaEABO/form_cliente.html")
    else:
            return render(request, "djapplibreriaEABO/login.html")

def procesar_cliente(request):
    
    # id_categoria= request.POST ['id_categoria']
    identificacion= request.POST ['identificacion']
    nombres= request.POST ['nombres']
    apellido= request.POST ['apellido']
    telefono= request.POST ['telefono']
    direccion= request.POST ['direccion']
    correo_electronico= request.POST ['correo_electronico']
    estado = request.POST ['estado']
    
   
    
 
    
    cliente = Cliente()
    # cate.id_categoria = id_categoria
    cliente.identificacion = identificacion 
    cliente.nombres = nombres  
    cliente.apellido = apellido  
    cliente.telefono = telefono  
    cliente.direccion =  direccion  
    cliente.correo_electronico = correo_electronico  
    cliente.estado = estado  
    
   
    
    cliente.save()
    return redirect(listado_cliente)

def eliminar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    cliente.delete()
#    return HttpResponse("llegamos aqui con el id" + str(id_aprendiz))
    return redirect(listado_cliente)
 
 

 
 
def listado_cliente(request):
    cliente =Cliente.objects.all()
    contexto = {'clientes': cliente}
    if request.user.is_authenticated: 
       return render(request,"djapplibreriaEABO/datos_clien.html",contexto)
    else:
          return render(request, "djapplibreriaEABO/login.html")


def update_cliente(request, id_cliente):
    cliente = Cliente.objects.filter(pk= id_cliente).first()
    contexto = {
    'cliente': cliente
    }
    return render(request, "djapplibreriaEABO/editar_cliente.html",contexto)
 
   
def updaterecord_cliente(request, id_cliente):
    cliente = Cliente.objects.filter(pk= id_cliente).first() 
    cliente.identificacion= request.POST ['identificacion']
    cliente.nombres= request.POST ['nombres']
    cliente.apellido= request.POST ['apellido']
    cliente.telefono= request.POST ['telefono']
    cliente.direccion= request.POST ['direccion']
    cliente.correo_electronico= request.POST ['correo_electronico']
    cliente.estado = request.POST ['estado']
    
   
    cliente.save()
    
 
    
    cliente = Cliente.objects.filter(pk= id_cliente).first()
    
    
    return redirect(listado_cliente)


 # LIBROSSSSSSSSSSSSSSSSSSSSSSSS)    
 
def Formulario_datos_libros(request):
        # return render(request, " edwinapp/Formulario.html")
    libro = Libros()
    libro.isbn = request.POST['isbn']
    libro.titulo = request.POST['titulo']
    libro.fecha_publicacion = request.POST['fecha_publicacion']
    libro.categoria = request.POST['categoria']
    libro.precio = request.POST['precio']
    libro.portada = request.POST['portada']
    libro.cantidad_stock = request.POST[' cantidad_stock']
    libro.estado = request.POST['estado']
        
    
        
    libro.save()
    libros = Libros.objects.all()

    contexto = {'libros': libros}

        
        # return HttpResponse("llegamos aqui")
    return render(request, "djapplibreriaEABO/datos_libro.html", contexto)


def Formulario_libros(request):
   

    contexto = {'libros': Libros.objects.all()}
        #return HttpResponse('ok')
    return render(request, "djapplibreriaEABO/form_libros.html", contexto)


def muestra_frm_libros(request):
    libro = Libros.objects.all()
    contexto = {'libro':libro}
    return render(request, "djapplibreriaEABO/form_libros.html",contexto )

def frm_libros(request):
    categorias = Categorias.objects.all()
    contexto = {'categorias':categorias}
    if request.user.is_authenticated: 
      return render(request, "djapplibreriaEABO/form_libros.html",contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")
        
def procesar_libro(request):
    
    # id_categoria= request.POST ['id_categoria']
    isbn= request.POST ['isbn']
    titulo= request.POST ['titulo']
    fecha_publicacion= request.POST ['fecha_publicacion']
    
    categoria=int(request.POST['categoria'])
    categoria = Categorias.objects.get(pk=categoria) 
    
    precio= request.POST ['precio']
   
    try:
        portada = request.FILES['portada']
        nombre_foto = f"media/{portada.name}"
        fs = FileSystemStorage()
        file_name = fs.save(portada.name, portada)
    except: 
        nombre_foto ="media/sinfoto.jpg"
    
    cantidad_stock = request.POST ['cantidad_stock']
    estado = request.POST ['estado']
    
   
    libro = Libros()
    libro.isbn = isbn 
    libro.titulo = titulo  
    libro.fecha_publicacion = fecha_publicacion  
    libro.categoria = categoria 
    libro.precio =  precio  
    libro.portada = nombre_foto
    libro.cantidad_stock = cantidad_stock 
    libro.estado = estado  
    
   
    
    libro.save()
    return redirect(listado_libros)

def eliminar_libro(request, isbn):
    try:
        libro = Libros.objects.get(pk=isbn)
        libro.delete()
    
        return redirect(listado_libros)
    except:
        error="Primero debes de eliminar donde esta la tabla con la llave foranea..."
        libros = Libros.objects.all()
        contexto={'libros': libros,
                  'error':error}
        return render(request, 'djapplibreriaEABO/datos_libro.html',contexto)
 
 
 
def listado_libros(request):
    libros =Libros.objects.all()
    contexto = {'libros': libros}
    if request.user.is_authenticated: 
      return render(request,"djapplibreriaEABO/datos_libro.html",contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")


def update_libros(request, isbn):
    libro = Libros.objects.filter(pk= isbn).first()
    contexto = {
    'libro': libro,
    }
    return render(request, "djapplibreriaEABO/editar_libro.html",contexto)
  
def updaterecord_libros(request, isbn):
   
    libro=Libros.objects.filter(pk= isbn).first()
   
    libro.titulo= request.POST ['titulo']
    libro.fecha_publicacion= request.POST ['fecha_publicacion']
    libro.precio= request.POST ['precio']
    libro.portada = request.POST ['portada']
    libro.cantidad_stock = request.POST ['cantidad_stock']
    libro.estado = request.POST ['estado']
    
    libro.save()
 
    
    return redirect(listado_libros)


  # LIBROSSSSSSSSSS AUTORESSSSSSSSSSSSSS)   
   
def listado_librosautores(request):
   librosautores =TblLibroPorAutor.objects.all()
   contexto = {'librosautores': librosautores}
   if request.user.is_authenticated: 
      return render(request,"djapplibreriaEABO/datos_libro_autor.html",contexto)
   else:
            return render(request, "djapplibreriaEABO/login.html")
   


 # pedidossssssssssssssss  clientessssssssssssssssssssssssss) 
 
def listado_pedido_cliente(request):
    pedidocliente  = PedidoCliente.objects.all()
    contexto ={'pedidosclientes':pedidocliente }
    if request.user.is_authenticated: 
       return render(request, 'djapplibreriaEABO/datos_pedido_cliente.html', contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")
    
def frm_pedido_cliente(request):
    libro=Libros.objects.all()
    cliente=Cliente.objects.all()
    contexto={'libros':libro,"clientes":cliente}
    if request.user.is_authenticated: 
       return render(request, 'djapplibreriaEABO/form_pedido_cliente.html',contexto)
    else:
        return render(request, "djapplibreriaEABO/login.html")
    
    
def procesar_pedido_cliente(request):
    numero_pedido = request.POST['numero_pedido'] 
    id_cliente = int(request.POST['id_cliente'])
    id_cliente = Cliente.objects.get(pk=id_cliente)
    isbn = int(request.POST['isbn'])
    isbn = Libros.objects.get(pk=isbn)
    fecha_pedido = request.POST['fecha_pedido']
    cantidad = request.POST['cantidad']
    subtotal = request.POST['subtotal']
    estado = request.POST['estado']
     
    pedidocliente = PedidoCliente()
    pedidocliente.numero_pedido = numero_pedido
    pedidocliente.id_cliente = id_cliente
    pedidocliente.isbn = isbn
    pedidocliente.fecha_pedido = fecha_pedido
    pedidocliente.cantidad  = cantidad 
    pedidocliente.subtotal = subtotal
    pedidocliente.estado = estado
  

    pedidocliente.save()
    return redirect(listado_pedido_cliente)

    # return HttpResponse('Registro procesado e insertado correctamente...')


def eliminar_Pedido_Cliente(request, id_pedido):
    try:
        pedidocliente= PedidoCliente.objects.get(pk= id_pedido)
        pedidocliente.delete()
        return redirect(listado_pedido_cliente)
        # return HttpResponse("llegamos aqui con el id"+string(id_aprendiz))
    except:
        error=" Primero debes de eliminar donde esta la tabla con la llave foranea..."
        
def actualizar_Pedido_Cliente(request, id_pedido):
  pedidocliente = PedidoCliente.objects.filter(pk= id_pedido).first()
  contexto = {
    'pedidocliente': pedidocliente,
    }
  return render(request, "djapplibreriaEABO/editar_pedido_cliente.html",contexto)
  
def actualizar_Pedido_Cliente2(request, id_pedido):
     
    pedidocliente = PedidoCliente.objects.filter(pk= id_pedido).first()

    pedidocliente.numero_pedido = request.POST['numero_pedido']  
    pedidocliente.fecha_pedido = request.POST['fecha_pedido']
    pedidocliente.cantidad = request.POST['cantidad']
    pedidocliente.subtotal = request.POST['subtotal']
    pedidocliente.estado = request.POST['estado']  


    pedidocliente.save()
    return redirect(listado_pedido_cliente)
    
def Formulario_Pedido_Cliente(request):
    pedidocliente = PedidoCliente()
    pedidocliente.numero_pedido = request.POST['numero_pedido'] 
    pedidocliente.id_cliente = request.POST['id_cliente']
    pedidocliente.isbn = request.POST['isbn']
    pedidocliente.fecha_pedido = request.POST['fecha_pedido']
    pedidocliente.cantidad = request.POST['cantidad']
    pedidocliente.subtotal = request.POST['subtotal']
    pedidocliente.estado = request.POST['estado']
        
    
        
    pedidocliente.save()
    pedidosclientes = PedidoCliente.objects.all()

    contexto = {'pedidosclientes': pedidosclientes}

        
        # return HttpResponse("llegamos aqui")
    return render(request, "djapplibreriaEABO/datos_libro_autor.html", contexto)

def login(request):
    return render(request,'djapplibreriaEABO/login.html')


def validar_usuario(request):
    if request.POST:
        usu = request.POST['usuario']
        clave = request.POST['clave']

        try:
            user = auth.authenticate(username=usu, password=clave)
            auth.login(request, user)

        except (AuthUser.DoesNotExist, AttributeError):
            return HttpResponse("Error al iniciar sesion")
        return redirect(index)

    else:

        return HttpResponse(" no se puede  acceder a esta pagina sin inciar")
    

def logout(request):
    auth.logout(request)
    return redirect(index)