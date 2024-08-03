import subprocess
import time


#opening app
app_name = 'firefox'
app_loc = f"C:\\Program Files\\Mozilla Firefox\\{app_name}.exe"




subprocess.Popen(app_loc)

time.sleep(5)

def return_list():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id,Path'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)    
    for line in proc.stdout:
        if not line.decode()[0].isspace():
            list_app = line.decode().rstrip()
            print(list_app)
            
print('\n')
return_list()
print('\n')

time.sleep(2)
        
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)    

if app_name in a:
    subprocess.call("TASKKILL /F /IM firefox.exe", shell=True)

time.sleep(3)

print('\n')
return_list()




