from rest_framework.serializers import ModelSerializer
from users.serializers import UserOverviewSerializer
from .models import Board

class BoardSerializer(ModelSerializer) : 
    writer = UserOverviewSerializer(read_only=True)

    class Meta : 
        model = Board

        fields = "__all__"

        # depth = 1 #쓸수는 있지만 보안상 문제로 사용하지 않음

        # fields = [
        #     "title",
        #     "content",
        #     "writer"
        # ]

        # exclude = [
        #     "insert_joined"
        # ]