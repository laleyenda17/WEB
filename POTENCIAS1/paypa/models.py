from django.db import models

# Create your models here.
class Producto(models.Model):
      producto=models.CharField(max_length=200,null=False)
      #title = models.CharField(max_length=200,verbose_name='Titulo')
      price=models.DecimalField(max_digits=8, decimal_places=2)
      #description =models.TextField(verbose_name='Descripcion')
      #image =models.ImageField(verbose_name='Imagen',upload_to="projects")
      #links =models.URLField(null=True,blank=True)
      #created =models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creaciôn')
      #updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de Modificacion')


      #class Meta:
      #      verbose_name="proyecto"
      #      verbose_name_plural= "proyectos"
      #      ordering=["-created"]

      def __str__(self):
          return self.producto

class Compra(models.Model):
      id =models.CharField(primary_key= True,max_length=100)
      estado =models.CharField(max_length=100)         
      codigo_estado =models.CharField(max_length=100)
      producto =models.ForeignKey(to=Producto,on_delete=models.SET_NULL,null= True) 
      total_de_la_compra=models.DecimalField(max_digits=6, decimal_places=2)
      nombre_cliente=models.CharField(max_length=100)
      apellido_cliente=models.CharField(max_length=100)
      correo_cliente=models.EmailField(max_length=100)
      direccion_cliente=models.CharField(max_length=100)

      def __str__(self):
          return self.nombre_cliente 

#class Video(models.Model):
#      caption=models.CharField(max_length=100)
#      video=models.FileField(upload_to="paypa/%y")

#      def __str__(self):
#          return self.caption

      
