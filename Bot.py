import requests
import random
from time import sleep

# List of proxies you obtained
proxies = ['163.158.216.152:80',
    '58.176.46.248:80',
    '218.191.247.51:8380',
    '122.96.59.102:80',
    '122.96.59.102:81',
    '220.136.198.198:8080',
    '202.171.253.72:80',
    '122.96.59.99:81',
    '113.252.236.96:8080',
    '122.96.59.99:843',
    '122.193.14.106:81',
    '111.7.160.20:80',
    '124.88.67.23:843',
    '168.63.20.19:8134',
    '82.176.161.89:80',
    '122.193.14.102:80',
    '111.1.23.169:80',
    '124.88.67.17:83',
    '122.96.59.107:843',
    '124.88.67.17:80',
    '122.193.14.108:82',
    '124.88.67.54:843',
    '122.96.59.107:83',
    '124.88.67.17:82',
    '118.151.209.114:80',
    '201.241.88.63:80',
    '124.88.67.24:81',
    '122.193.14.108:80',
    '94.209.99.35:80',
    '124.88.67.24:843',
    '137.135.166.225:8132',
    '122.96.59.98:81',
    '168.63.20.19:8119',
    '124.88.67.32:843',
    '178.166.41.225:80',
    '124.88.67.31:843',
    '137.135.166.225:8142',
    '118.141.41.84:80',
    '201.55.46.6:80',
    '80.112.143.63:80',
    '78.21.187.112:80',
    '168.63.24.174:8138',
    '111.1.23.146:80',
    '122.96.59.102:82',
    '168.63.20.19:8132',
    '217.23.90.10:8080',
    '122.96.59.99:83',
    '112.214.73.253:80',
    '122.193.14.106:80',
    '80.112.170.75:80',
    '122.193.14.106:83',
    '46.101.22.124:8118',
    '122.96.59.107:80',
    '137.135.166.225:8134',
    '122.96.59.98:80',
    '122.96.59.107:82',
    '82.139.108.47:80',
    '122.96.59.102:83',
    '84.52.93.202:3128',
    '111.1.23.181:80',
    '122.193.14.106:82',
    '218.205.80.2:81',
    '218.205.80.12:80',
    '122.96.59.106:80',
    '46.101.22.159:8118',
    '181.36.5.138:3128',
    '111.1.23.141:80',
    '168.63.20.19:8127',
    '122.96.59.107:81',
    '124.88.67.23:81',
    '111.1.23.213:8080',
    '185.23.142.89:80',
    '122.193.14.104:83',
    '218.191.247.51:80',
    '210.51.2.203:8089',
    '195.138.173.87:3128',
    '111.1.23.213:80',
    '122.96.59.99:80',
    '137.135.166.225:8144',
    '122.96.59.99:82',
    '124.88.67.20:843',
    '209.249.157.73:8080',
    '218.205.80.13:80',
    '111.1.23.213:8088',
    '137.135.166.225:8139',
    '137.135.166.225:8135',
    '218.205.80.8:80',
    '122.193.14.104:80']
url = "https://www.toprevenuegate.com/icj1hrt7pd?key=40e6de77327dfa02813c429680adef2f"
num_visits = 1000
visit_count = {}

for i in range(num_visits):
    random.shuffle(proxies)
    for proxy in proxies:
        try:
            response = requests.get(url, proxies={"http": proxy}, timeout=5)  # Setting a timeout
            if response.status_code == 200:
                visit_count[proxy] = visit_count.get(proxy, 0) + 1
                print(f"Visited {url} ({visit_count[proxy]}) from {proxy}")
                sleep(1)
                break  # Break the inner loop if the request is successful
            else:
                print(f"Failure {response.status_code} from {proxy}")
                
        except requests.RequestException as e:
            print(f"Error during request from {proxy}: {str(e)}")
        sleep(5)

    else:
        print("All proxies exhausted, end of try.")
        break  # If all proxies are tried and none worked

