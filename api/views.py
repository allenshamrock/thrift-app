from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication.models import Customer,Order
from .serializers import CustomerSerializer,OrderSerializer


@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer =CustomerSerializer(customers, many=True)
    return Response(serializer.data)

api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getOrders(request):
    customers = Order.objects.all()
    serializer = OrderSerializer(customers, many=True)
    return Response(serializer.data)


api_view(['POST'])


def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

