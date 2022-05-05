from ..models import Category, Position
from ..serializers import PositionSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class PositionDetail(APIView):
    def get_product(self, request, pk1, pk2):
        try:
            product = Category.objects.get(id=pk1).positions.get(id=pk2)
        except:
            raise Http404
        return product

    def get(self, request, pk1, pk2):
        product1 = self.get_product(request, pk1, pk2)
        serializer = PositionSerializer(product1)
        return Response(serializer.data)

    def put(self, request, pk1, pk2):
        if request.user.role == 1:
            product = self.get_product(request, pk1, pk2)
            try:
                request.data.pop('category')
            except:
                pass
            serializer = PositionSerializer(instance=product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else: return Response('Permission denied!!')

    def delete(self, request, pk1, pk2):
        if request.user.role == 1:
            product = self.get_product(request, pk1, pk2)
            product.delete()
            return Response({"delete_status": "successful"})
        else: return Response('Permission denied!!')
