import logging

from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ChatSerializer, ChatCreateSerializer
from .models import Chat
logger = logging.getLogger('log')


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def chatting(request):
    if request.method == 'GET':
        usr = request.user.username
        mess = Chat.objects.filter(to_mes=usr)
        serializer = ChatSerializer(mess, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChatCreateSerializer(data=request.data)
        from_mes = request.user.username
        if serializer.is_valid():
            serializer.save(from_mes=from_mes)
            logger.info(f"{request.user.username} write message")
            logger.warning(f"{request.user.username} write message")
            logger.error(f"{request.user.username} write message")
            logger.critical(f"{request.user.username} write message")
            return Response(serializer.data)
        return Response(serializer.errors)

