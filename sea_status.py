from concurrent.futures import ThreadPoolExecutor, as_completed
from theater import my_cursor
import re
import requests
import json
import time

def getStatus():
    my_cursor.execute("SELECT id FROM theatres WHERE websites_id = 11")
    urls = []
    soldPercents = {}
    wtIDs = my_cursor.fetchall()
    for id in wtIDs:   
        id = id[0]
        sql1 = "SELECT showtimeurl FROM showtimes WHERE t_id = " + str(id)
        my_cursor.execute(sql1)
        urls = my_cursor.fetchall()
        for url in urls:
            uri = str(url[0]).strip()
            hitCode = gethitCode(uri)
            soldPercents[uri] = getJSON(hitCode)
    return soldPercents

def getJSON(hitCode):
    payload = {"filmCode": str(hitCode)}
    postTo = "https://www.gv.com.sg/.gv-api/sessionforfilm"
    header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36", "x_developer": "ENOVAX",}
    page = requests.post(postTo, json.dumps(payload), headers=header)
    dataList = page.json()['data']['locations']
    for i in dataList:
        # print(i['dates'][0]['times'][0]['soldPercent'])
        return i['dates'][0]['times'][0]['soldPercent']
                                                      
def gethitCode(uri):
    m = re.search('filmCode/(.+?)/showDate', uri)
    return m.group(1)

def main():
    executor = ThreadPoolExecutor(max_workers=100)
    uri = executor.submit(getStatus())
    col = uri.result()
    for i in col:
        print(i)

if __name__ == "__main__":
    start_time = time.time()
    main()
    exeTime = time.time()
    print("---Execution time: %s seconds --- Execution time")