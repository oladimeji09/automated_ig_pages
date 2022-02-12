from datetime import datetime
import sys, python_helper as ph, google_helper as gh

default_args = {
    'owner': 'airflow',
    'start_date':datetime(2022, 2, 7),
                }

def timecheck():
    with open(ph.root_fp+'top-10-billionaires/heartbeat.csv', 'a+') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')

def gmail_check():
    with open(ph.root_fp+'top-10-billionaires/gmail_heartbeat.csv', 'a+') as f:
        print('LEVEL 1')
        try:
            if gh.main('gmail'):
                print('LEVEL 2')
                f.write('Gmail Active \t'+ datetime.now().strftime("%Y-%m-%d %H:%M")+'\n')
        except:
                f.write('Gmail Inactive \t'+ datetime.now().strftime("%Y-%m-%d %H:%M") +'\n')
                print('LEVEL 3')

timecheck()
gmail_check()
