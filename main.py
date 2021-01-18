# Importing

import subprocess
import time
import requests
import os

hw = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() # Grapping HWID

a = requests.get('url here') # Making GET Request

try:
    if hw in a.text: # Checking HWID In URL
        print('[+] HWID Signed In Success')
        pass # If HWID In URL Then Success
    else:
        print('[!] HWID Not Found')
        print(f'HWID: {hw}') 
        time.sleep(5)
        os._exit() # If HWID Not In URL Then Fail + Close os

except:
    print('[?] Failed to connect to database')
    time.sleep(5) 
    os._exit() # Check for Fail Connection
 
os.system('title HWID Authentication') # OS Title
 
print('Hello, World!') # Hello World :)
input()
