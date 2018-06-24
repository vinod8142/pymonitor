#from performance.models import *
from performance.serializers import *
from performance.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from connection.script import *
import json
import pdb
from pprint import pprint

class PerformanceController:
    def get_performance_info_list(self, request):
        try:
            start_exec(['df -Ph', 'free -tm', 'uptime'])
            general_info = {
                "disk": get_disk(),
                "memory":get_mem(),
                "load":get_load()
            }
            return json.dumps(general_info)
             
        except Exception as error:
            print(error)

    def get_performance_info(self, request, pk):
        try:
            start_exec(['df -Ph', 'free -tm', 'uptime'])
            general_info = {
                "disk": get_disk(),
                "memory":get_mem(),
                "load":get_load()
            }
            pk = pk.replace("_",".")
            specific_info = {} 
            specific_info['disk'] = general_info['disk'].get(pk,"Not able to find")
            specific_info['memory'] = general_info['memory'].get(pk,"Not able to find")
            specific_info['load'] = general_info['load'].get(pk,"Not able to find")
            return json.dumps(specific_info)
        except Exception as error:
            print(error)
