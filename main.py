import subprocess
import time
import request
import os
hw = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
a = requests.get('url here')
 
try:
    if hw in a.text:
        print('[+] HWID Signed In Success')
        pass
    else:
        print('[!] HWID Not Found')
        print(f'HWID: {hw}') 
        time.sleep(5)
        os._exit()
except:
    print('[?] Failed to connect to database')
    time.sleep(5) 
    os._exit() 
 
os.system('title HWID Authentication')
 
print('Hello, World!')
input()
