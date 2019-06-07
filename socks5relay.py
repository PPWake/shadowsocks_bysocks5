import socks
import socket
import os
import json
import logging

# {"default":["106.111.110.142", 2081]}
# TODO:1. if the socks5 addr changed, rebuild the connect to remote.
SOCKS_CONTENT = None

def get_socks5_addr(remote_addr, config_path):
    global SOCKS_CONTENT
    if not os.path.exists(config_path):
        return None
    try:
        if not SOCKS_CONTENT:
            with open(config_path) as file:
                content = file.read()
                content = json.loads(content)
                SOCKS_CONTENT = content
        
        if "default" in SOCKS_CONTENT:
            addr:str = SOCKS_CONTENT["default"]
            if type(addr) != str:
                logging.info("socks5 config content formatter invalid %s!" % addr)
                return None
            
            ipports = addr.split(":")
            if len(ipports) != 2:
                logging.info("socks5 config content formatter invalid %s!" % ipports)
                return None
            # print("choise %s -> %s:%s" % (remote_addr, ipports[0], ipports[1]))
            logging.info("choise %s -> %s:%s" % (remote_addr, ipports[0], ipports[1]))
            return ipports[0], int(ipports[1])
    except Exception as e:
        print(e)
    return None