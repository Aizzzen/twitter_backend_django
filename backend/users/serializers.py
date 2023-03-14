from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    # Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    # и так же что он не может быть прочитан клиентской стороной
    password = serializers.CharField(
        max_length=40,
        min_length=6,
        # write_only=True
    )

    # Клиентская сторона не должна иметь возможность отправлять токен вместе с
    # запросом на регистрацию. Сделаем его доступным только на чтение.
    token = serializers.CharField(max_length=255, read_only=True)

    # fullname = serializers.CharField(max_length=40, default=None)
    # confirmed = serializers.BooleanField(default=False)
    # location = serializers.CharField(max_length=255, default=None)
    # about = serializers.CharField(max_length=255, default=None)
    # website = serializers.CharField(max_length=255, default=None)

    class Meta:
        model = User
        # Перечислить все поля, которые могут быть включены в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = ('id', 'email', 'username', 'password', 'token',
                  # 'fullname', 'confirmed', 'location', 'about', 'website'
                  )

    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return User.objects.create_user(**validated_data)
