from .connection import MySSH
from .server_details import server_details_dict
from threading import Thread
import pdb
import re
from datetime import timedelta
import pprint
#########################
class ApData:
    pass

# Create the SSH connection
ApData.dic = {}
ApData.cmd_out_dic = {}
def _connect(hst_n, hst_d):
    try:
        ApData.dic[str(hst_n)] = MySSH()
        ApData.dic[str(hst_n)].set_verbosity(False)
        ApData.dic[str(hst_n)].connect(hostname=hst_n,
                                        username=hst_d['username'],
                                        password=hst_d['password'],
                                        port=22)
        ApData.dic.update()
        if ApData.dic[str(hst_n)].connected() is False:
            print('ERROR: connection failed for host {}.'.format(
                ApData.dic[str(hst_n)]))
    except Exception as err:
        print("ERROR: {}".format(err))

def _run(con_obj, cmd, *args,**kwrgs):    
    print('=' * 64)
    print('command: %s' % (cmd))
    ApData.cmd_out_dic[con_obj] = {}
    for command in cmd:
        status, output = ApData.dic[con_obj].run(command)
        ApData.cmd_out_dic[con_obj][command] = output
        ApData.cmd_out_dic[con_obj].update()
        ApData.cmd_out_dic.update()
    print('status : %d' % (status))
    print('output : %d bytes' % (len(output)))
    print('=' * 64)
    return ApData.cmd_out_dic
def start_exec(cmd, indata=None):
    '''
    Run a command with optional input.

    @param cmd    The command to execute.
    @param indata The input data.
    @returns The command exit status and output.
             Stdout and stderr are combined.
    '''
    for hst_name,details in server_details_dict.items():
        conn_thread = Thread(target=_connect, args=(hst_name, details))
        conn_thread.start()
        conn_thread.join()
    for conn_obj in ApData.dic:
        print('*' * 64)
        print("For Host: {} ".format(conn_obj))
        print('*' * 64)
        output = _run(conn_obj, cmd)
    return output
        # cmd_thread = Thread(target=_run, args=(conn_obj, cmd))
        # cmd_thread.start()
        # conn_thread.join()
def get_uptime():
    """
    Get uptime
    """
    #start_exec(['cat /proc/uptime'])
    uptime = {}
    try:
        for hst in ApData.cmd_out_dic:
            uptime[str(hst)] = {}
            f = ApData.cmd_out_dic[hst]['cat /proc/uptime']
            uptime_seconds = float(f.split()[0])
            uptime_time = str(timedelta(seconds=uptime_seconds))
            uptime[str(hst)]['up_time'] = uptime_time.split('.', 1)[0]
            idle = float(f.split()[1])
            uptime[str(hst)]['idle_time'] = str(timedelta(seconds=idle))
            uptime[str(hst)].update()
            uptime.update()
    except Exception as err:
        uptime[str(hst)]['data'] = str(err)
        uptime[str(hst)].update()
        uptime.update()
    return uptime

def get_ipaddress():
    """
    Get the IP Address
    """
    ipadrr = {}
    #start_exec(['/sbin/ifconfig'])
    try:
        for hst in ApData.cmd_out_dic:
            ipadrr[str(hst)] = {}
            ad = ApData.cmd_out_dic[hst]['/sbin/ifconfig']
            ad_val = re.findall("(\d+.\d+.\d+.\d+)\s",ad)

            if ad_val!=[]:
                ipadrr[str(hst)]['ip_addr'] = ad_val[0]
                ipadrr[str(hst)].update()
                ipadrr.update()
            else:
                ipadrr[str(hst)]['ip_addr'] = "Not able to find ip address"
                ipadrr[str(hst)].update()
                ipadrr.update()
            mac =  re.findall("(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)",ad)
            if mac!=[]:
                ipadrr[str(hst)]['mac'] = mac[0]
                ipadrr[str(hst)].update()
                ipadrr.update()
            else:
                ipadrr[str(hst)]['mac'] = "Not able to find mac address"
                ipadrr[str(hst)].update()
                ipadrr.update()
    except Exception as err:
        print(err)
    return ipadrr

def get_cpus():
    """
    Get the number of CPUs and model/type
    """
    cpu = {}
    #start_exec(['cat /proc/cpuinfo'])
    try:
        for hst in ApData.cmd_out_dic:
            cpu[str(hst)] = {}
            model = ApData.cmd_out_dic[hst]['cat /proc/cpuinfo']
            cpu_model = re.findall('model\s+name\s+:\s+(.*)',model)
            cpu_cores = re.findall('cpu\s+cores\s+:\s+(.*)',model)
            if cpu_model!=[]:
                cpu[str(hst)]['cpu_model'] = cpu_model[0]
                cpu[str(hst)].update()
                cpu.update()
            else:
                cpu[str(hst)]['cpu_model'] = "Not able to find cpu info"
                cpu[str(hst)].update()
                cpu.update()
            if cpu_cores!=[]:
                cpu[str(hst)]['cpu_cores'] = cpu_cores[0]
                cpu[str(hst)].update()
                cpu.update()
            else:
                cpu[str(hst)]['cpu_cores'] = "Not able to find cpu cores"
                cpu[str(hst)].update()
                cpu.update()

    except Exception as err:
        print(str(err))

    return cpu
##############################
def get_users():
    users = {}
    #start_exec(['who'])

    try:
        for hst in ApData.cmd_out_dic:
            users[str(hst)] = {}
            model = ApData.cmd_out_dic[hst]['who']
            out = re.findall('(\S+)\s+(\S+)\s+(.*)\n',model)
            if out!= []:
                users[str(hst)]['users_list'] = out
            else:
                users[str(hst)]['users'] = "unable to find users"
    except Exception as err:
        print(err)
    return users  
def get_platform():
    #start_exec(['uname -a'])
    load_details = {}
    try:
        for hst in ApData.cmd_out_dic:
            model = ApData.cmd_out_dic[hst]['uname -a']
            load_details[str(hst)] = {}
            load_details[str(hst)]['platform'] = {}
            out = re.findall('\w+\s(\S+)\s+(\S+)\s\S+.*GNU\/(\w*)',model)

            if out!=[]:
                load_details[str(hst)]['platform']={'local_host' : out[0][1],
                'kernal_version' : out[0][1],'OS':out[0][2]}
            else:
                load_details[str(hst)]['platform'] = "Unable to find Platform "
    except Exception as err:
        print(err) 
    return load_details
##########performance##############################
def get_disk():
    rom_details = {}
    start_exec(['df -Ph'])
    try:
        for hst in ApData.cmd_out_dic:
            rom_details[str(hst)] = {}
            model = ApData.cmd_out_dic[hst]['df -Ph']
            rom_details[str(hst)]['file_Sytem'] = {}
            r = re.compile(r'(\S+)\s+(\d+.?\d+?\w?)\s+(\d+.?\d*?\w?)\s+(\d+.?\d*\w?)\s+(\d+%)')
            k = r.findall(model)
            if k!=[]:
                for i in k:
                    j = list(i)[ : ]
                    rom_details[str(hst)]['file_Sytem'][j[0]] ={'Total_size':j[1],
                    'used_space':j[2],'Free_space':j[3],"use%" :j[4]}
            else:
                rom_details[str(hst)]['file_Sytem'] = "Unable to find disk details"
    except Exception as err:
        print(err)
    return rom_details

def get_mem():
    start_exec(['free -tm'])    

    ram_details = {}
    try:
        for hst in ApData.cmd_out_dic:

            ram_details[str(hst)] = {}
            model = ApData.cmd_out_dic[hst]['free -tm']
            ram_details[str(hst)]['mem_details'] = {}
            r = re.compile(r'(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)?\s+(\d+)?\s+(\d+)?')
            k = r.findall(model)
            if k!=[]:
                for i in k:
                    l = list(i)[ : ]
                    ram_details[str(hst)]['mem_details'][l[0]] = {'Total': l[1]+'M',
                    'Used':l[2]+'M','Free':l[3]+'M','Shared' : l[4]+'M','Buff/cache':l[5]+'M',
                    'Available' : l[6]+'M'}
            else:
                ram_details[str(hst)]['mem_details'] = "Unable to find memory details" 
    except Exception as err:
        print(err)       
    return ram_details

def get_load():
    start_exec(['uptime'])
    Load_details = {}
    try:
        for hst in ApData.cmd_out_dic:
            model = ApData.cmd_out_dic[hst]['uptime']
            Load_details[str(hst)] = {}
            Load_details[str(hst)]['Get_load'] = {}
            r = re.compile(r'([a-z]+:(.*?),)')
            k = r.search(model)
            if k!=[] and k!=None:
                Load_details[str(hst)]['Get_load']=  k.group(2)
            else:
                Load_details[str(hst)]['Get_load'] = "Unable to find Load details"
    except Exception as err:
        print(err)
    return Load_details

#tm = get_uptime()
#pprint.pprint(tm)
# addr = get_cpus()
# print(addr)












#run_cmd('sudo ls -ltrh /var/log | tail', sudo_password)  # sudo command