from general.serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from connection.script import *
import json
import pdb
from pprint import pprint

class GeneralController:
    def get_general_info_list(self, request):
        try:
            start_exec(['uname -a','who','cat /proc/cpuinfo',
                '/sbin/ifconfig','cat /proc/uptime'])
            general_info = {
                "cpus": get_cpus(),
                "users":get_users(),
                "platform":get_platform(),
                "uptime:":get_uptime(),
                "ipaddressess":get_ipaddress()
            }
            return json.dumps(general_info)
        except Exception as error:
            print(error)
    def get_general_info(self, request, pk):
        try:
            start_exec(['uname -a','who','cat /proc/cpuinfo',
                '/sbin/ifconfig','cat /proc/uptime'])
            general_info = {
                "cpus": get_cpus(),
                "users":get_users(),
                "platform":get_platform(),
                "uptime":get_uptime(),
                "ipaddressess":get_ipaddress()
            }
            pk = pk.replace("_",".")
            specific_info = {} 
            specific_info['cpus'] = general_info['cpus'].get(pk,"Not able to find")
            specific_info['users'] = general_info['users'].get(pk,"Not able to find")
            specific_info['platform'] = general_info['platform'].get(pk,"Not able to find")
            specific_info['uptime'] = general_info['uptime'].get(pk,"Not able to find")   
            specific_info['ipaddressess'] = general_info['ipaddressess'].get(pk,"Not able to find")      
            return json.dumps(specific_info)
        except Exception as error:
            print(error)
