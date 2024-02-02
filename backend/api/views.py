# from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json 
from django.forms.models import model_to_dict 


from products.models import Product 
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view



@csrf_exempt
@api_view(['GET','POST'])
def api_home(request, *arg, **kwargs):
    # instance = Product.objects.all().order_by("?").first() 
    # data = {} 

    serializer = ProductSerializer(data = request.data)  
    if serializer.is_valid() :
        # data = model_to_dict(instance, fields=['id','title','price', 'sale_price'])

        instance = serializer.save() 
        return Response(serializer.data) 