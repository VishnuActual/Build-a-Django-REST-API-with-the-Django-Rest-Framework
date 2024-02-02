from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.decorators import api_view 


from django.shortcuts import get_object_or_404

from .models import Product 
from .serializers import ProductSerializer 




class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if not content:
            content = title 
        serializer.save(content = content) 

product_create_view = ProductListCreateAPIView.as_view()




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 

product_detail_view = ProductDetailAPIView.as_view() 


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
# note that first i am getting all the product data and then serializing that and returning 


product_list_view = ProductListAPIView.as_view() 



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    lookup_field = 'pk' 

    def perform_update(self, serializer):
        instance = serializer.save() 

        if not instance.content:
            instance.content = instance.title 

product_update_view = ProductUpdateAPIView.as_view() 
''' here first same as previous then lookup field is set according the url and get that
    creating an instance then saving that '''
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    lookup_field = 'pk' 

    def perform_destroy(self, instance):
        super().perform_destroy(instance)  

        

product_delete_view = ProductDestroyAPIView.as_view() 



def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 

    if method=='GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk) 
            data = ProductSerializer(obj, many=True) 
            return Response(data) 
        queryset = Product.objects.filter(pk=pk)  
        data = ProductSerializer(queryset, many=True).data 
        return Response(data) 
        # urls args 
        # get request -> detail view 
        # List View 
    elif method=='POST':
        
        #create an item 
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) :
            instance = serializer.save() 


    