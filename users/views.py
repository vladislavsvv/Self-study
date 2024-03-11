from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import UserIsStaff, UserIsOwnerOrReadOnly
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Разрешить создание и удаление только пользователям со статусом staff
        if self.action in ['create', 'destroy']:
            self.permission_classes = [UserIsStaff]

        # Разрешить чтение и обновление только владельцу объекта или пользователям со статусом staff
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [UserIsOwnerOrReadOnly]

        # Разрешить всем просматривать список пользователей
        elif self.action == 'list':
            self.permission_classes = []

        return super().get_permissions()