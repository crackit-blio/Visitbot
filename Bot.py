import random
from time import sleep
import requests
from fake_useragent import UserAgent

# List of proxies you obtained
# ... (your existing proxy list)

url = "https://www.toprevenuegate.com/icj1hrt7pd?key=40e6de77327dfa02813c429680adef2f"
num_visits = 1000
visit_count = {}

# Initialize UserAgent
ua = UserAgent()

for i in range(num_visits):
    random.shuffle(proxies)
    for proxy in proxies:
        try:
            headers = {'User-Agent': ua.random}
            response = requests.get(url, proxies={"http": proxy}, headers=headers, timeout=5)
            if response.status_code == 200:
                visit_count[proxy] = visit_count.get(proxy, 0) + 1
                print(f"Visited {url} ({visit_count[proxy]}) from {proxy}")
                sleep(1)
                break
            else:
                print(f"Failure {response.status_code} from {proxy}")
                
        except requests.RequestException as e:
            print(f"Error during request from {proxy}: {str(e)}")
        sleep(9)

    else:
        print("All proxies exhausted, end of try.")
        break
