from rest_framework import serializers
from .models import Services, Payment_user, Expired_payments, User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class Payment_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = ['id', 'User_id', 'Service_id', 'Amount', 'PaymentDate', 'ExpirationDate']

class Expired_paymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = ['id', 'Pay_user_id', 'Penalty_fee_amount']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']




class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("El email ya ha sido usado")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)

        return user


class GetUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]