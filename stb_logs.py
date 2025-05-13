#!/usr/local/bin/python3

import os, subprocess
from datetime import datetime


class StbLogs():
    def __init__(self):
        #self.serial=str(input("Type Serial number:  "))
        self.serial = "192.168.2.17"
        self.dict_adb = {'adb_connect': "adb connect ",
                         'adb_devices': "adb devices ",
                         'adb_logcat': "adb logcat -d > ",
                         'adb_install': "adb install -r -f ",
                         'adb_kill': "adb kill-server",
                         'adb_bugreport': "adb bugreport ",
                         'adb_meminfo': "adb shell dumpsys cpuinfo ",                         
                         }

        self.dict_so = {'so_KillAdb': "killall adb"}

        self.dict_menu = {1: "Get Logs",
                          2: "Get Bugreports",
                          3: "Install apk",
                          4: "Check memory-use live Claro APK",
                          5: "connect device",
                          6: "disconnect devices",
                          7: "Exit"}

        self.save_folder = os.path.expanduser("~/Downloads/")
        self.current_time = datetime.now().strftime("date_%d_%m_%Hh_%Mm")
        self.choice_msg = "Select an option: "
        self.apkVersions_path = "/Users/at/Downloads/apk_claroTv_tata/"

    def get_cwd(self):
        subprocess.run(f'cd {self.save_folder}')
        self.local_path_downloads=subprocess.run('pwd')
    


    def crearte_folder(self):
        subprocess.run(f'cd  {self.local_path_downloads}')
        subprocess.run('mkdir chmod 777 apk_claroTv_tata')
        subprocess.run('cd apk_claroTv_tata')
        #self.apkVersions_path=subprocess.run('pwd')
        
        

    def adb_connection(self):
        subprocess.run(self.dict_so['so_KillAdb'], shell=True)
        subprocess.run(self.dict_adb['adb_connect'] + self.serial, shell=True)

    def get_adb_logs(self):
        self.adb_connection()
        print("Getting Logs...please wait.....\n")
        logs_saved_fileName=self.serial + self.current_time
        subprocess.run(self.dict_adb['adb_logcat']  + self.save_folder + logs_saved_fileName + ".txt",shell=True)
        print(f"Logs saved in => {self.save_folder}+{logs_saved_fileName}\n")

    def get_adb_bugreport(self):
        self.adb_connection()
        subprocess.run(self.dict_adb['adb_bugreport'] + self.save_folder , shell=True)
        print(f"Saved bugreport in => {self.save_folder} + folder\n")

    def get_meminfo(self):
        self.adb_connection()
        print(f"Saved meminfo_report in => {self.save_folder}\n")
        subprocess.run(f"while true;do {self.dict_adb['adb_meminfo']} | grep com.amx.launcher | tee -a {self.save_folder}meminfo_{self.current_time}.txt;sleep 1; done", shell=True)

            

    def list_files(self):
        self.apk_list=[]
        files=os.listdir(self.apkVersions_path)
        for file in files:
            if file not in self.apk_list:
                self.apk_list.append(file)
                self.apk_list.sort()
        return self.apk_list

        

        
    def install_adb_apk(self):
        #self.get_cwd()
        #self.crearte_folder()
        self.list_files()
        print('LATEST APK = >  '+ self.apk_list[-1])
        self.adb_connection()
        subprocess.run(self.dict_adb['adb_install']  + self.apkVersions_path+self.apk_list[-1], shell=True)

    def clear_screen(self):
        os.system('clear')

    def adb_kill(self):
        subprocess.run(self.dict_adb['adb_kill'], shell=True)
        print(f"  devices disconnected \n")

    def main(self):
        while True:
            print((self.choice_msg + '\n'))
            for num, ops in self.dict_menu.items():
                print(f"{num}.- {ops} \n")
            
            try:
                choice = int(input('.............................  ====>    '))


                if choice == 1:
                    self.get_adb_logs()


                elif choice == 2:
                    self.get_adb_bugreport()

                elif choice == 3:
                    self.install_adb_apk()

                elif choice == 4:
                    self.get_meminfo()

                elif choice == 5:
                    self.adb_connection()

                elif choice == 6:
                    self.adb_kill()

                elif choice == 7:
                    print("Ending...")
                    break

                else:
                    print("Try again...")
            except :
                print(f"\n Input Error.. select a valid option .... +  \n ")


if __name__ == '__main__':
    stb_logs = StbLogs()
    stb_logs.main()



