#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Management3.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# import add module
import subprocess
import threading
import re
import psycopg2
import yaml
import psutil
from speedtest import Speedtest
import speedtest
import pexpect

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
management3_spec = ["implementation_id", "Management3", 
         "type_name",         "Management3", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Management3
# @brief ModuleDescription
# 
# 
# </rtc-template>
class Management3(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_in = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._inIn = OpenRTM_aist.InPort("in", self._d_in)
        self._d_out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._outOut = OpenRTM_aist.OutPort("out", self._d_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("in",self._inIn)
		
        # Set OutPort buffers
        self.addOutPort("out",self._outOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        ManagementClass()
    
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK

class ManagementClass:
    def __init__(self):
        with open('ipsetting.yaml', 'r') as file:
            serverip_data = yaml.load(file, Loader=yaml.FullLoader)
            self.serverip=serverip_data.get('serverip')
            print(self.serverip)
        self.connection = psycopg2.connect(
            host=self.serverip,
            database="testdb",
            user="rsdlab",
            password="rsdlab"
        )
        '''
        self.arg=sys.argv[1]
        self.connection = psycopg2.connect(
            host=self.arg,
            database="testdb",
            user="rsdlab",
            password="rsdlab"
        )
        '''
        '''
        self.connection = psycopg2.connect(
            host="192.168.0.151",
            database="testdb",
            user="rsdlab",
            password="rsdlab"
        )
        '''
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        thread_ip = threading.Thread(target=self.handle_ip)
        thread_ip.start()
        thread_ip.join()
        
        thread_hard = threading.Thread(target=self.handle_hard)
        thread_hard.start()
        thread_battery = threading.Thread(target=self.handle_battery)
        thread_battery.start()
        thread_cpu = threading.Thread(target=self.handle_cpu)
        thread_cpu.start()
        thread_memory = threading.Thread(target=self.handle_memory)
        thread_memory.start()
        thread_gpu = threading.Thread(target=self.handle_gpu)
        thread_gpu.start()
        thread_speedupload = threading.Thread(target=self.handle_speedupload)
        thread_speedupload.start()
        thread_speeddownload = threading.Thread(target=self.handle_speeddownload)
        thread_speeddownload.start()
        thread_latency = threading.Thread(target=self.handle_latency)
        thread_latency.start()
        thread_checkRTC = threading.Thread(target=self.handle_checkRTC)
        thread_checkRTC.start()
    def handle_ip(self):
        output = subprocess.check_output(["ifconfig"])
        match = re.search(r"wlp2s0:.*?inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output.decode("utf-8"), re.DOTALL)
        self.ip_address = match.group(1)
        print(self.ip_address)
    def handle_hard(self):
        while True:
            try:
                lsusb_output = subprocess.check_output(["lsusb"]).decode("utf-8")
                #正規表現を使用してデバイスの後の数字が001、002、003以外のもののIDを抽出
                pattern = re.compile(r"Bus \d+ Device (\d+): ID (\w+):(\w+)")
                matches = pattern.findall(lsusb_output)
                #フィルタリングして結果を表示
                for device_number, id_part1, id_part2 in matches:
                    if int(device_number) not in [1, 2, 3]:
                        self.cursor.execute(f"update manage set hardvendor='{id_part1}' where ip='{self.ip_address}';")
                        self.cursor.execute(f"update manage set hardproduct='{id_part2}' where ip='{self.ip_address}';")
                        print(f"Device {device_number} ID's Parts: {id_part1}, {id_part2}")
            except subprocess.CalledProcessError as e:
                print(f"Error:{e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(3)
            #self.cursor.execute(f"update manage set hard='{result_battery.stdout}' where ip='{self.ip_address}';")

    def handle_battery(self):
        print("battery")
        while True:
            try:
                CMD='cat /sys/class/power_supply/BAT1/capacity'
                result_battery=subprocess.run(CMD,shell=True, text=True, capture_output=True, check=True)
                print("battery:",result_battery.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error:{e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(3)
            self.cursor.execute(f"update manage set battery='{result_battery.stdout}' where ip='{self.ip_address}';")
    
    def handle_cpu(self):
        print("cpu")
        while True:
            try:
                CMD = 'vmstat'
                result_cpu = subprocess.run(CMD, shell=True, text=True, capture_output=True, check=True)
                #result_memory2 = result_memory.stdout  # 文字列なのでdecode不要
                cpu_idle_match = re.search(r'\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s(\d+)', result_cpu.stdout)
                if cpu_idle_match:
                    cpu_idle_percentage = int(cpu_idle_match.group(1))
                    #print(f'CPU Idle Percentage: {cpu_idle_percentage}%')
                    cpu_rate=100-cpu_idle_percentage
                    print("cpu: ",cpu_rate)
                
            except subprocess.CalledProcessError as e:
                print(f"Error:{e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(3)
            self.cursor.execute(f"update manage set cpu='{cpu_rate}' where ip='{self.ip_address}';")

    def handle_memory(self):
        print("memory")
        while True:
            try:
                CMD = 'free -m'
                result_memory = subprocess.run(CMD, shell=True, text=True, capture_output=True, check=True)
                #result_memory2 = result_memory.stdout  # 文字列なのでdecode不要
                total_match = re.search(r'Mem:\s+(\d+)', result_memory.stdout)
                free_match = re.search(r'Mem:\s+\d+\s+\d+\s+(\d+)', result_memory.stdout)
                if total_match and free_match:
                    total_memory = str(total_match.group(1))
                    free_memory = str(free_match.group(1))
                    #print(f'Total Memory: {total_memory} MB')
                    #print(f'Free Memory: {free_memory} MB')
                    memory_rate = (int(total_memory) - int(free_memory)) / int(total_memory) * 100
                    print("memory:", int(memory_rate))
                
            except subprocess.CalledProcessError as e:
                print(f"Error:{e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(3)
            self.cursor.execute(f"update manage set memory='{int(memory_rate)}' where ip='{self.ip_address}';")
    def handle_gpu(self):
        print("gpu")
        while True:
            password = "rsdlab"  #パスワード
            #sudo intel-gpu-topを実行し、パスワードを自動で入力する
            child = pexpect.spawn("sudo intel_gpu_top -o gpuoutput.txt", encoding='utf-8')  # encodingを指定
            # パスワードを入力
            child.expect(r'\[sudo\] rsdlab のパスワード: ')
            child.sendline(password)
            # 一定時間intel-gpu-top`を実行
            time.sleep(3)
            # `Ctrl+C`で`intel-gpu-top`を停止
            child.sendcontrol('c')

            # ファイルパス
            file_path = "gpuoutput.txt"
            # テキストファイルを開いて中身を読み込む
            with open(file_path, "r") as file:
                data = file.read()
            #正規表現パターン
            pattern = r'\b\d+\.\d{2}\b'  #2桁の小数点以下を持つ数値のパターン
            # 正規表現パターンに一致する数字を抽出
            matches = re.findall(pattern, data)
            rcs1=matches[6]
            rcs2=matches[11]
            rcs=(float(rcs1)+float(rcs2))/2
            rcs_cut=round(rcs,2)
            bcs1=matches[7]
            bcs2=matches[12]
            bcs=(float(bcs1)+float(bcs2))/2
            bcs_cut=round(bcs,2)
            vcs1=matches[8]
            vcs2=matches[13]
            vcs=(float(vcs1)+float(vcs2))/2
            vcs_cut=round(vcs,2)
            vecs1=matches[9]
            vecs2=matches[14]
            vecs=(float(vecs1)+float(vecs2))/2
            vecs_cut=round(vecs,2)

            gpu=rcs_cut+bcs_cut+vcs_cut+vecs_cut
            print(gpu)
            self.cursor.execute(f"update manage set gpu='{gpu}' where ip='{self.ip_address}';")

    
    def handle_disk(self):
        print("disk")
        while True:
            disk_space = psutil.disk_usage('/').percent
            print("disk=")
            print(disk_space)
            time.sleep(3)
            self.cursor.execute(f"update manage set disk='{int(disk_space)}' where ip='{self.ip_address}';")

    def handle_speeddownload(self):
        print("speed")
        while True:
            speed = Speedtest()
            download_speed = speed.download() / 1_000_000  # Convert to Mbps
            print("Dspeed=")
            print(download_speed)
            #time.sleep(3)
            self.cursor.execute(f"update manage set speed_download='{download_speed}' where ip='{self.ip_address}';")
            #time.sleep(1)

    def handle_speedupload(self):
        print("Uspeed")
        while True:
            speed = Speedtest()
            upload_speed = speed.upload() / 1_000_000  # Convert to Mbps
            print("speed=")
            print(upload_speed)
            #time.sleep(3)
            self.cursor.execute(f"update manage set speed_upload='{upload_speed}' where ip='{self.ip_address}';")
    
    def handle_latency(self):
        print("latency")
        while True:
            st = speedtest.Speedtest()
            server_info = st.get_best_server()
            latency = server_info['latency']
            print(latency)
            self.cursor.execute(f"update manage set latency='{latency}' where ip='{self.ip_address}';")

    def handle_checkRTC(self): #エラーが起きたらデータベースに書き込み
        print("checkRTC")
        while True:
            try:
                CMD = 'rtls -l /localhost/rsdlab.host_cxt'
                result_RTC = subprocess.run(CMD, shell=True, text=True, capture_output=True, check=True)
                for line in result_RTC.stdout.splitlines():
                    last_item=line.split()[-1]
                    first_item=line.split()[0]
                    print(last_item)
                    print(first_item)
                
            except subprocess.CalledProcessError as e:
                print(f"Error:{e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(3)
            #self.cursor.execute(f"update manage set battery='{result_battery.stdout}' where ip='{self.ip_address}';")
	



def Management3Init(manager):
    profile = OpenRTM_aist.Properties(defaults_str=management3_spec)
    manager.registerFactory(profile,
                            Management3,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Management3Init(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("Management3" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

