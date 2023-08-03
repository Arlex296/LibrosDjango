from django.urls import path
from djapplibreriaEABO import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('formulario_usu/',views.formulario_usu, name='formulario_usu'),



 path('muestra_frm_aut',views.muestra_frm_aut,name='muestra_frm_aut'),
 path('frm_autores',views.frm_autores,name='frm_autores'),
 path('procesar_autor',views.procesar_autor,name='procesar_autor'),

 path('eliminar_autor/<int:id_autor>',views.eliminar_autor,name='eliminar_autor'),
 path('listado_autores',views.listado_autores,name='listado_autores'),
 path('update_autore/<int:id_autor>',views.update_autore,name='update_autore'),
 path('update_autore/updaterecord_autores/<int:id_autor>',views.updaterecord_autores,name='updaterecord_autores'),
 
 
 path('Formulario_datos_categorias',views.Formulario_datos_categorias,name='Formulario_datos_categorias'),
 path('Formulario_categorias',views.Formulario_categorias,name='Formulario_categorias'),
 path('muestra_frm_categ',views.muestra_frm_categ,name='muestra_frm_categ'),
 path('frm_categorias',views.frm_categorias,name='frm_categorias'),
 path('procesar_categoria',views.procesar_categoria,name='procesar_categoria'),
 path('eliminar_categorias/<int:id_categoria>',views.eliminar_categorias,name='eliminar_categorias'),
 path('listado_categorias',views.listado_categorias,name='listado_categorias'),
 path('update_categorias/<int:id_categoria>',views.update_categorias,name='update_categorias'),
 path('update_categorias/updaterecord_categorias/<int:id_categoria>',views.updaterecord_categorias,name='updaterecord_categorias'),
 
 path('Formulario_datos_cliente',views.Formulario_datos_cliente,name='Formulario_datos_cliente'),
 path('Formulario_clientes',views.Formulario_clientes,name='Formulario_clientes'),
 path('muestra_frm_cliente',views.muestra_frm_cliente,name='muestra_frm_cliente'),
 path('frm_clientes',views.frm_clientes,name='frm_clientes'),
 path('procesar_cliente',views.procesar_cliente,name='procesar_cliente'),
 path('eliminar_cliente/<int:id_cliente>',views.eliminar_cliente,name='eliminar_cliente'),
 path('listado_cliente',views.listado_cliente,name='listado_cliente'),
 path('update_cliente/<int:id_cliente>',views.update_cliente,name='update_cliente'),
 path('update_cliente/updaterecord_cliente/<int:id_cliente>',views.updaterecord_cliente,name='updaterecord_cliente'),
 
 path('Formulario_datos_libros',views.Formulario_datos_libros,name='Formulario_datos_libros'),
 path('Formulario_libros',views.Formulario_libros,name='Formulario_libros'),
 path('muestra_frm_libros',views.muestra_frm_libros,name='muestra_frm_libros'),
 path('frm_libros',views.frm_libros,name='frm_libros'),
 path('procesar_libro',views.procesar_libro,name='procesar_libro'),
 path('eliminar_libro/<int:isbn>',views.eliminar_libro,name='eliminar_libro'),
 path('listado_libros',views.listado_libros,name='listado_libros'),
 path('update_libros/<int:isbn>',views.update_libros,name='update_libros'),
 path('update_libros/updaterecord_libros/<int:isbn>',views.updaterecord_libros,name='updaterecord_libros'),
 
 path('listado_librosautores',views.listado_librosautores,name='listado_librosautores'),


 path('frm_pedido_cliente/',views.frm_pedido_cliente,name='frm_pedido_cliente'),
 path('procesar_pedido_cliente/',views.procesar_pedido_cliente,name='procesar_pedido_cliente'),
 path('listado_pedido_cliente/',views.listado_pedido_cliente,name='listado_pedido_cliente'),
 path('eliminar_Pedido_Cliente/<int:id_pedido>',views.eliminar_Pedido_Cliente, name='eliminar_Pedido_Cliente'),
 path('actualizar_Pedido_Cliente/<int:id_pedido>', views.actualizar_Pedido_Cliente, name='actualizar_Pedido_Cliente'),
 path('actualizar_Pedido_Cliente/actualizar_Pedido_Cliente2/<int:id_pedido>', views.actualizar_Pedido_Cliente2, name='actualizar_Pedido_Cliente2'),


 path('cerrar_sesion/',views.logout,name='logout'),
 path('index2',views.index2,name='index2'),

 path('validar',views.validar_usuario,name='validar_usuario'),
 path('iniciar_sesion/',views.login,name='login'),
]