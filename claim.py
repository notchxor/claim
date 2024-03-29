import os
import sys
import time
import subprocess
import logging
import json
import configparser

def run(cmd):
    cmdout = subprocess.run(cmd,encoding='utf-8',stdout=subprocess.PIPE)
    print(cmdout.stdout)


config = configparser.ConfigParser()
config.read("config.ini")
chains=json.loads(config.get("chains","chains"))
password = config.get("config","wallet_pass")
sleep=int(config.get("config","wait_s"))
logging.basicConfig(filename=config.get("config","logfile"),level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


run(['cleos', 'wallet', 'unlock', '-n', config.get("config","wallet_name"), '--password' ,password])
for chain in chains:
    key=config.get(chain,"key")
    print("importing key: ",key)
    run(['cleos', 'wallet','import', '-n', 'claim', '--private-key',key])

while True:
    time.sleep(sleep)
    run(['cleos', 'wallet', 'unlock', '-n', config.get("config","wallet_name"), '--password' ,password])
    for chain in chains:
        try:
            json_owner="{\"owner\":\""+config.get(chain,"owner")+"\"}"
            authority=config.get(chain,"owner")+"@"+config.get(chain,"permission")
            cmd=['cleos','-u',config.get(chain,"api"),'push','action','eosio','claimrewards',json_owner,'-p',authority]
            run(cmd)
        
        except subprocess.CalledProcessError as err:
            logging.info(err)
            pass
        except Exception as err:
            logging.info(err)
            pass

