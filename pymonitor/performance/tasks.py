from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from connection.script import *
from performance.models import *
import json
from performance.serializers import *
from pprint import pprint

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/2')),
    name="task_performance_poll")
def task_performance_poll():
    """
    Saves latest image from Flickr
    """
    try:
        start_exec(['df -Ph', 'free -tm', 'uptime'])
        performance_info = {
            "disk": get_disk(),
            "memory":get_mem(),
            "load":get_load()
        }
        for server_ip in performance_info['disk']:
            performance = Performance()
            performance.server = server_ip
            if performance_info['disk'][server_ip]["file_Sytem"]!="Unable to find disk details":
                if performance_info['disk'][server_ip]["file_Sytem"].get("/dev/sda3")!=None:
                    performance.file_system = "/dev/sda3"
                    performance.free_space = performance_info['disk'][server_ip]["file_Sytem"]["/dev/sda3"]["Free_space"]
                    performance.total_size = performance_info['disk'][server_ip]["file_Sytem"]["/dev/sda3"]["Total_size"]
                    performance.use_percentage = performance_info['disk'][server_ip]["file_Sytem"]["/dev/sda3"]["use%"]
                    performance.used_space = performance_info['disk'][server_ip]["file_Sytem"]["/dev/sda3"]["used_space"]
                else:
                    performance.file_system = None
                    performance.free_space = None
                    performance.total_size = None
                    performance.use_percentage = None
                    performance.used_space = None
            else:
                performance.file_system = None
                performance.free_space = None
                performance.total_size = None
                performance.use_percentage = None
                performance.used_space = None

            if performance_info['load'][server_ip]['Get_load']!="Unable to find Load details":
                performance.load = performance_info['load'][server_ip]['Get_load']
            else:
                performance.load = None

            if performance_info['memory'][server_ip].get('mem_details')!='Unable to find memory details':
                performance.available_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Available']
                performance.cache_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Buff/cache']
                performance.free_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Free']
                performance.shared_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Shared']
                performance.total_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Total']
                performance.used_memory = performance_info['memory'][server_ip]['mem_details']['Mem:']['Used']
            else:
                performance.available_memory = None
                performance.cache_memory = None
                performance.free_memory = None
                performance.shared_memory = None
                performance.total_memory = None
                performance.used_memory = None

            performance.save()        
        return json.dumps(performance_info)
    except Exception as error:
        print(error)
    logger.info("Hello performance")



# def serialize(data):

#     return json.dumps(data)

# def deserialize(data):

#     return json.loads(data)

# def get_post_data(request, key="data"):
#     data = deserialize(request.POST.get(key, "{}"))
#     return data

# class RegisterView(viewsets.ModelViewSet):

#     @csrf_exempt
#     def register(self, request):
#         print("entering user view")
#         pdb.set_trace()
#         data = get_post_data(request)
#         try:

#             user = User.objects.get(username=data.get("userid"))
#             db_serializer_obj = UserSerializer(user)
#             db_serializer_obj1 = RegisterSerializer(user)

#             data =  {"status": "User ID already Exist"}
#             return HttpResponse(serialize(data))

#         except User.DoesNotExist:
#             user = User.objects.create_user(data.get("userid"),data.get("email"), data.get("passwd"))
#             register = Register()
#         user.first_name= data.get('fname', '')
#         user.last_name = data.get('lname', '')
#         user.is_staff = True
#         user.is_active = True
#         register.user = user
#         register.mobile_no = data.get("mobile")
#         register.hometown = data.get("home")
#         register.save()
#         # user.is_superuser = True
#         user.save()

#         data =  {"status": " Registration success! Please Log In"}
#         return HttpResponse(serialize(data))
