#from performance.models import *
from users.serializers import *
from users.models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from connection.script import *
import json
import pdb
from pprint import pprint


def serialize(data):
    return json.dumps(data)

def deserialize(request, key="data"):
    pdb.set_trace()
    data = json.loads(request.POST.get(key, "{}"))
    return data


class UserController:
    def get_user_info_list(self, request):
        
        if request.user.is_superuser:
            try:
                obj = UserRegister.objects.all()
                serializer_user = UserRegisterSerializer(obj,many=True)
                data = json.loads(json.dumps(serializer_user.data))
                #result = {"status": "HTTP_200_OK","data":data}
                return data            
            except Exception as error:
                print(error)
        else:
            return "You dont have credentials to see all data" 
    def get_user_info(self, request, pk):
        if pk==request.user.username:
            try:
                obj = UserRegister.objects.get(user_id=request.user.id)
                serializer_user = UserRegisterSerializer(obj)
                data = serializer_user.data
                data = json.dumps(serializer_user.data)
                return data            
            except Exception as error:
                print(error)
        else:
            return "Please provide your valid username"

    def register(self, request):
        #data = deserialize(request)
        data = request.data
        try:
            user = User.objects.get(username=data.get("username"))
            data =  {"status": "User ID already Exist"}
            return serialize(data)

        except User.DoesNotExist:
            user = User.objects.create_user(data.get("username"),data.get("email"), data.get("password"))
            register = UserRegister()
        user.first_name= data.get('fname', '')
        user.last_name = data.get('lname', '')
        user.is_staff = True
        user.is_active = True
        register.user = user
        register.mobile_no = data.get("mobile", '')
        register.hometown = data.get("hometown", '')
        register.save()
        # user.is_superuser = True
        user.save()

        data =  {"status": " Registration success! Please Log In"}
        return serialize(data)

    def user_update(self, request):
        pdb.set_trace()
        data = request.data
        if data.get("username")==request.user.username:
            try:
                user = User.objects.get(username=data.get("username"))
                user.set_password = data.get('password', '')
                user.email = data.get('email', '')
                user.last_name = data.get('lname', '')
                user.first_name= data.get('fname', '')
                user.last_name = data.get('lname', '')
                register = UserRegister.objects.get(user_id=request.user.id)
                register.mobile_no = data.get("mobile", '')
                register.hometown = data.get("hometown", '')
                register.save()
                user.save()
                data =  {"status": "Update success!"}
                return data
            except Exception as error:
                print(error)
        else:
            return "Please provide your valid username.\nNote: Username can't be changed" 
                
    def user_delete(self, request, pk):
        pdb.set_trace()
        data = request.data
        if pk==request.user.username:
            try:
                user = User.objects.get(username=request.user.username)
                register = UserRegister.objects.get(user_id=request.user.id)
                register.delete()
                user.delete()
                return "Deleted Success!"
            except Exception as error:
                print(error)
        else:
            return "Please provide your valid username.\nNote: Username can't be changed" 