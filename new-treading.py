    
from concurrent.futures import ThreadPoolExecutor, as_completed
from tnp-news import work2 as INL
from asiaone-list-page import main2 as SNL
import time

count = 0
def count_me(f):
    print(f.__doc__)
    f()

with ThreadPoolExecutor(max_workers=10) as tp:
    start_time = time.time()
    print(start_time)
    future_pool = [tp.submit(count_me, i) for i in [SNL, INL]]
    for f in as_completed(future_pool):
        f.result()
    print("--- %s seconds ---" % (time.time() - start_time))





# import threading 
# import requests
# from tnp-news 

# class Worker(threading.Thread):
# 	def __init__(self):
# 		super(Worker, self).__init__()

# 	def run(self):
# 		for i in range(10):
# 			print(i)


# if __name__ == '__main__':
# 	thread1 = Worker()
# 	thread2 = Worker()
# 	thread1.start()
# 	thread2.start()
