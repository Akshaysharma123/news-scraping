    
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from asia-one-news.asiaone-list-page import main2 as INL
# from tnp-news.tnp-news import main2 as SNL
# import time

# count = 0
# def count_me(f):
#     print(f.__doc__)
#     f()

# with ThreadPoolExecutor(max_workers=10) as tp:
#     start_time = time.time()
#     print(start_time)
#     future_pool = [tp.submit(count_me, i) for i in [SNL, INL]]
#     for f in as_completed(future_pool):
#         f.result()
#     print("--- %s seconds ---" % (time.time() - start_time))
