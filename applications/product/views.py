from rest_framework import generics


from applications.product.selializers import ProductSerializer

from applications.product.models import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
