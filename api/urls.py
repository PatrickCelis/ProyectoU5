from rest_framework import routers
from . import views
from .api import GetOneServices, PostOneServices, OnePaymentUser, OneExpired, OneUser, PostOnePayment, PostOneExpired, PostOneUser
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('users', views.GetUsers)

# router.register('api/services', ServicesViewSet, 'services')
# router.register('api/payments', PaymentUserViewSet, 'payments')
# router.register('api/expired', ExpiredViewSet, 'expired')
# router.register('api/user', UserViewSet, 'user')


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v2/services/', GetAllServices.as_view(), name = 'fullViewServices'),
    path('api/', views.MyAPIView.as_view(), name='api'),


    path('api/v2/services/<pk>', GetOneServices.as_view(), name='services'),
    path('api/v2/services/', PostOneServices.as_view(), name='postservices'),

    path('api/v2/payments/<pk>', OnePaymentUser.as_view(), name='payments'),
    path('api/v2/payments/', PostOnePayment.as_view(), name='postpayments'),


    path('api/v2/expired/<pk>', OneExpired.as_view(), name='expired'),
    path('api/v2/expired/', PostOneExpired.as_view(), name='postexpireds'),

    path('api/v2/user/<pk>', OneUser.as_view(), name='users'),
    path('api/v2/user/', PostOneUser.as_view(), name='postsusers'),

    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),




]