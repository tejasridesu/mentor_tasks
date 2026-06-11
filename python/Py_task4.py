import time
from threading import Thread
def call_api(url):
    print(f"calling {url}")
    time.sleep(2)
    print(f"finished {url}")
urls=["users/1","users/2","users/3"]
t1=Thread(target=call_api,args=("users/1",))
t2=Thread(target=call_api,args=("users/2",))
t3=Thread(target=call_api,args=("users/3",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("All API calls completed")

#high level
#from concurrent.futures import ThreadPoolExecutor
#with ThreadPoolExecutor(max_workers=3) as executor:
#  executor.map(call_api, urls)

# thiscreates threads,executes,waiting for completion means instead of Thread(),start(),join() only one line
