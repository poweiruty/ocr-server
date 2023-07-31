from PIL import Image
import pytesseract
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from boards.models import Board
from boards.serializers import BoardSerializer

class OCR(APIView) :
    def get(self, request, pk) :
        board = Board.objects.get(pk=pk)
        serializer = BoardSerializer(board)
        #filename = serializer.data.get('loaded_file')
        #filepath = f"media/{filename}"
        filepath = serializer.data.get('loaded_file')
        print(filepath[1:])
        image = Image.open(filepath[1:])
        lang = "eng"
        result = pytesseract.image_to_string(image, lang=lang)
        return Response({
            'result' : result
        })

def index(request) :
    return render(request, 'index.html')

def login(request) :
    return render(request, 'login_form.html')

def mypage(request) :
    return render(request, 'mypage.html')

def join(request) :
    return render(request, 'join_form.html')

def user_update(request) :
    return render(request, 'user_update_form.html', {'pk' : request.user.pk})

def board(request, pk) :
    return render(request, 'board.html')

def board_update(request, pk) :
    return render(request, 'board_update_form.html')

def board_write(request) :
    return render(request, 'board_form.html')

def boards(request) :
    return render(request, 'board_list.html')