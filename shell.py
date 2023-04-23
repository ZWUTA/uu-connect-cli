import subprocess
import time
from tools import ConfigToolsbox
from config.config import *

def getTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
def timeLogMsg(str_in:str):
    return f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {str_in}"

config = ConfigToolsbox.cfgmgr("./config", "vpn.json")
config.cache_init()

if(config.cache["core-type"] == "zju"):
    init_command:str = (
        f"{config.cache['core']}"
        f" -username {config.cache['username']}"
        f" -password {config.cache['password']}"
        f" -server {config.cache['server']}"
        f" -port {config.cache['port']}"
        f" -socks-bind {config.cache['socks-bind']}"
        f" {(lambda ka,:'' if ka else '-disable-keep-alive')(config.cache['KeepAlive'])}"
        )
else:
    init_command:str = (
        f"{config.cache['core']}"
        f" -username {config.cache['username']}"
        f" -password {config.cache['password']}"
        f" -server {config.cache['server']}"
        f" -port {config.cache['port']}"
        f" -socks-bind {config.cache['socks-bind']}"
        )
# print(init_command)

first_run:bool = True
while config.cache["KeepAlive"]:
    if first_run:
        first_run = False
    else:
        print(timeLogMsg(tag_keep_alive))
    uu_connect = subprocess.Popen(init_command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    while True:
        if(uu_connect.poll() == 0):
            break
        line = uu_connect.stdout.readline()
        if not line:
            break
        #print(getTime(),end="")
        print(tag_core_out,line.decode("utf-8"),end="")
    print(timeLogMsg(tag_core_end))
    time.sleep(config_time_sleep)
print(timeLogMsg(tag_daemon_end))