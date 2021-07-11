from rest_framework import status
from rest_framework.response import Response

from customersapi.models import Customers
from customersapi.api.serializer import CustomersSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, ListAPIView

from customersapi.api.custompagination import CustomPagination
from customersapi.api.permission import IsAdminUserOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
class CustomersCrateAPIViews(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request):
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            print(Customers.objects.filter(TC=request.data['TC']))
            if Customers.objects.filter(TC=request.data['TC']).exists():
                return Response({"Message": "Customer already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomersDetailAPIViews(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self, pk):
        customers_instance = get_object_or_404(Customers, pk=pk)
        return customers_instance

    def get(self, request, pk):
        customers = self.get_object(pk=pk)
        serializer = CustomersSerializer(customers)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        customers = self.get_object(pk=pk)

        serializer = CustomersSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customers = self.get_object(pk=pk)
        customers.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class CustomersListView(ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['City', 'Town']