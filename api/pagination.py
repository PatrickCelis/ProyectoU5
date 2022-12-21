from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Services, Payment_user, Expired_payments, User
from api.serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer, UserSerializer


class MyAPIView(APIView):
    def get(self, request):
        # Realizar consulta a base de datos aquí
        results = Services, Payment_user, Expired_payments, User.objects.all()

        # Crear una instancia de PageNumberPagination y especificar el número de resultados por página
        paginator = PageNumberPagination()
        paginator.page_size = 100
        page_results = paginator.paginate_queryset(results, request)

        # Serializar los resultados y devolver la respuesta
        serializer = ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer, UserSerializer(page_results, many=True)
        return Response(serializer.data)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000