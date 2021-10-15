from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_questionnaires(request):
    questionnaires = Questionnaire.objects.all()
    serializer = QuestionnaireSerializer(questionnaires, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_style(request):
    if request.method == 'POST':
        serializer = QuestionnaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        questionnaires = Questionnaire.objects.filter(user_id=request.user.id)
        serializer = QuestionnaireSerializer(questionnaires, many=True)
        return Response(serializer.data)
