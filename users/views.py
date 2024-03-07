from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import UserIsStaff, UserIsOwnerOrReadOnly
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Разрешить создание и удаление только пользователям со статусом staff
    permission_classes_by_action = {
        'create': [UserIsStaff],
        'destroy': [UserIsStaff],
    }

    # Разрешить чтение и обновление только владельцу объекта или пользователям со статусом staff
    permission_classes = [UserIsOwnerOrReadOnly]
