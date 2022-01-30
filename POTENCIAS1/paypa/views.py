from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment,LiveEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from .models import *
#from .models import Video
import sys, json
# Create your views here.

def hola(request):
    #return render(request,template_name='paypa/Base.html')
    print("ENTRO EN EL HOLA")
    return render(request,"paypa/Base.html")  

def hola1(request):
    return render(request,"paypa/Base_1.html")  

def hola2(request):
    return render(request,"paypa/Base_2.html")

def hola3(request):
    return render(request,"paypa/Base_3.html")

def hola4(request):
    return render(request,"paypa/Base_4.html")

def hola5(request):
    return render(request,"paypa/Base_5.html") 

###################################################

def home(request):# aqui voy a colocar el video 
    #video=Video.objects.all()
    return render(request,"paypa/home.html")  

def Historia(request):
    return render(request,"paypa/Historia.html")  

def Contacto(request):
    return render(request,"paypa/Contacto.html")   
        
def Horoscopo(request):
    return render(request,"paypa/Horoscopo.html")    

def Tarot(request):
    return render(request,"paypa/Tarot.html")    

def Quiromancia(request):
    return render(request,"paypa/Quiromancia.html")     

def Membresias(request):
    return render(request,"paypa/Membresias.html")  

def Servicios(request):
    return render(request,"paypa/Servicios.html")

def Pagos(request):
    return render(request,"paypa/Pagos.html")    

##################################################################


def pa(request):

    GOLD = Producto.objects.get(pk=4)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 GOLD",GOLD)

    if detalle_precio==GOLD.price:
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)

def pa1(request):

    BLACK = Producto.objects.get(pk=5)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 black",BLACK)

    if detalle_precio==BLACK.price:
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)

def pa2(request):

    PLATINUM = Producto.objects.get(pk=7)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 PLATINUN",PLATINUM)

    if detalle_precio==PLATINUM.price:
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)

def pa3(request):

    LECTURA = Producto.objects.get(pk=1)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 LECTURA",LECTURA)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 LECTURA 000   ",Producto.objects.get(pk=700))

    if detalle_precio==LECTURA.price:
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)

def pa4(request):

    MANO = Producto.objects.get(pk=8)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 MANO",MANO)
    

    if detalle_precio==float(MANO.price):
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)

def pa5(request):

    ESPECIAL = Producto.objects.get(pk=9)
    data=json.loads(request.body)
    order_id=data['orderID']   

    detalle=GetOrder().get_order(order_id) 
    detalle_precio=float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)
    print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000 ESPECIAL",ESPECIAL)

    if detalle_precio==ESPECIAL.price:
       print("ENTRO COMPAAAAAAAAAAAAAAII 00000000000")
       trx=CaptureOrder().capture_order(order_id, debug=True) 
       pedido = Compra(
            id=trx.result.id,
            estado=trx.result.status,
            codigo_estado=trx.status_code,
            producto =Producto.objects.get(pk=1),
            total_de_la_compra=trx.result.purchase_units[0].payments.captures[0].amount.value,
            nombre_cliente=trx.result.payer.name.given_name,
            apellido_cliente=trx.result.payer.name.surname,
            correo_cliente=trx.result.payer.email_address,
            direccion_cliente=trx.result.purchase_units[0].shipping.address.address_line_1)
       pedido.save()    

       data={
          "id":f"{trx.result.id}",
          "nombre_cliente":f"{trx.result.payer.name.given_name}",
          "mensaje":"Tu compra se realizo =D"
       }
       return JsonResponse(data)
    else: 
       data={
          "mensaje":"Error =("
       }    
       return JsonResponse(data)       



#PARA REALIZAR EL PROCESO DE COMPRA #ID DE CLIENTE #ID SECRETO HIDE
class PayPalClient:
    def __init__(self):
        self.client_id = "ARpDdq2HGLQh_AhAWIYAu2jzFta9XpYyY-2my8s9YCGWNCvXoL5bM8VO5zjjilvVoeQTdu8rZl2DyeRd" 
        self.client_secret = "EI4NjheXhfyJWG55r_wFvDr9UQUSy3RjiWrt3DeIm61X5QWA40x2PPj2gnmTq_5dzMk6cqGQNWQyr7am" 

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result
    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


#OBTENGO LA INFORMAICON DE LA ORDEN DE COMPRA
class GetOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """You can use this function to retrieve an order by passing order ID as an argument"""   
  def get_order(self, order_id):
    """Method to get order"""
    request = OrdersGetRequest(order_id)
    #3. Call PayPal to get the transaction
    response = self.client.execute(request)
    return response
    #4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
    #print ('Status Code: ', response.status_code)
    #print ('Status: ', response.result.status)
    #print ('Order ID: ', response.result.id)
    #print ('Intent: ', response.result.intent)
    #print ('Links:')
    #for link in response.result.links:
    #  print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
    #print ('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
    #                   response.result.purchase_units[0].amount.value))

#"""This driver function invokes the get_order function with
#   order ID to retrieve sample order details. """
#if __name__ == '__main__':
#  GetOrder().get_order('REPLACE-WITH-VALID-ORDER-ID')
  

#CAPTURA DE LA COMPRA
class CaptureOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """this sample function performs payment capture on the order.
  Approved order ID should be passed as an argument to this function"""

  def capture_order(self, order_id, debug=False):
    """Method to capture order using order_id"""
    request = OrdersCaptureRequest(order_id)
    #3. Call PayPal to capture an order
    response = self.client.execute(request)
    #4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
    if debug:
      print ('Status Code: ', response.status_code)
      print ('Status: ', response.result.status)
      print ('Order ID: ', response.result.id)
      print ('Links: ')
      for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
      print ('Capture Ids: ')
      for purchase_unit in response.result.purchase_units:
        for capture in purchase_unit.payments.captures:
          print ('\t', capture.id)
      print ("Buyer:")
      #print ("\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
        #response.result.payer.name.given_name + " " + response.result.payer.name.surname,
        #response.result.payer.phone.phone_number.national_number))
    return response



    