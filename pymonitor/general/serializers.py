from rest_framework import serializers
from general.models import *

class GeneralSerializer(serializers.Serializer):
    # os_info = DictField(child=CharField())
    # uptime = DictField(child=CharField())
    #import pdb;pdb.set_trace()
    cpu_model=serializers.CharField(source='*')
    #cpu_model = serializers.DictField(child=serializers.CharField())
