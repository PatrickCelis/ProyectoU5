from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from .models import Services, Payment_user, Expired_payments, User
from rest_framework import viewsets, permissions, status, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .pagination import StandardResultsSetPagination
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer, UserSerializer


# class ServicesViewSet(viewsets.ModelViewSet):
#     queryset = Services.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = ServicesSerializer
#
# class PaymentUserViewSet(viewsets.ModelViewSet):
#     queryset = Payment_user.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = Payment_userSerializer
#
# class ExpiredViewSet(viewsets.ModelViewSet):
#     queryset = Expired_payments.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = Expired_paymentsSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer


# class PaymentView(generics.CreateAPIView):
#     queryset = Payment_user.objects.all()
#     serializer_class = Payment_userSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class AllViewsView(generics.ListAPIView):
#     queryset = Services, Payment_user, Expired_payments, User.objects.all()
#     serializer_class = ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer, UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

'''Modificar registros uno por uno.'''

# class PaymentFilterSet(filters.FilterSet):
#      class Meta:
#          model = Payment_user
#         fields = ['PaymentDate', 'ExpirationDate']

class MyPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100




#Modificar Services uno por uno, es estática asi que solo admitirá GET.
class GetOneServices(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @permission_classes([IsAdminUser|IsAuthenticated])
    #@method_decorator(csrf_exempt, name='dispatch')
    def get(self, request, pk, *args, **kwargs):
        throttle_scope = 'general'
        uno = get_object_or_404(Services, pk=pk)
        serializer = ServicesSerializer(uno)
        return Response({"mensaje": "Petición GET recibida"},serializer.data)

    @permission_classes([IsAdminUser])
    def put(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(Services, pk=pk)
        serializer = ServicesSerializer(uno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAdminUser])
    def delete(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(Services, pk=pk)
        uno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostOneServices(APIView):
    @permission_classes([IsAdminUser])
    def post(self, request, *args, **kwargs):
        # throttle_scope = 'general'
        serializer = ServicesSerializer(data=request.data)
        print('confirmado')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Modificar Payment_user uno por uno.
class OnePaymentUser(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @permission_classes([IsAdminUser|IsAuthenticated])
    def get(self, request, pk):
        uno = get_object_or_404(Payment_user, pk=pk)
        serializer = Payment_userSerializer(uno)
        throttle_scope = 'get'
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def put(self, request, pk):
        uno = get_object_or_404(Payment_user, pk=pk)
        serializer = Payment_userSerializer(uno, data=request.data)
        throttle_scope = 'put'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAdminUser])
    def delete(self, request, pk):
        throttle_scope = 'delete'
        uno = get_object_or_404(Payment_user, pk=pk)
        uno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostOnePayment(APIView):
    @permission_classes([IsAdminUser | IsAuthenticated])
    def post(self, request, *args, **kwargs):
        throttle_scope = 'post'
        serializer = Payment_userSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Modificar uno por uno en Expired_payments, se solicita que solo admita GET y POST.
class OneExpired(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get', 'post']
    pagination_class = MyPagination

    @permission_classes([IsAdminUser|IsAuthenticated])
    def get(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(Expired_payments, pk=pk)
        serializer = Expired_paymentsSerializer(uno)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def put(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(Expired_payments, pk=pk)
        serializer = Expired_paymentsSerializer(uno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAdminUser])
    def delete(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(Expired_payments, pk=pk)
        uno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PostOneExpired(APIView):
    @permission_classes([IsAdminUser])
    def post(self, request, *args, **kwargs):
        throttle_scope = 'general'
        serializer = Expired_paymentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Modificar uno por uno en User.
class OneUser(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @permission_classes([IsAdminUser|IsAuthenticated])
    def get(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(uno)
        return Response(serializer.data)

    @permission_classes([IsAdminUser])
    def put(self, request, pk):
        throttle_scope = 'general'
        person = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAdminUser])
    def delete(self, request, pk):
        throttle_scope = 'general'
        uno = get_object_or_404(User, pk=pk)
        uno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PostOneUser(APIView):
    @permission_classes([IsAdminUser])
    def post(self, request, *args, **kwargs):
        throttle_scope = 'general'
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





