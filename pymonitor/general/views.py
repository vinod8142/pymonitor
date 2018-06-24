
#Django lib
from django.shortcuts import render
from rest_framework import viewsets
from general.serializers import *
from general.controllers import *
from django.http import HttpResponse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class GeneralViewSet(viewsets.ModelViewSet, GeneralController):
    '''
    API endpoint that allows to get general information about Servers.
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = GeneralSerializer

    def list(self, request, *args, **kwargs):
        return HttpResponse(self.get_general_info_list(request))
    def retrieve(self, request, pk=None):
        return HttpResponse(self.get_general_info(request, pk))
    def create(self, request, *args, **kwargs):
        pass
    def update(self, request, *args, **kwargs):
        pass
    def destroy(self, request, pk=None):
        pass




