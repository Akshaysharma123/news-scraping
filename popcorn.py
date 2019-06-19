import requests
from bs4 import BeautifulSoup
import time
import schedule
import sys

start_time = time.time()
def main():
    url = "https://www.popcorn.app/sg/men-in-black-international/movie/9035"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    title = soup.find(text="GV Suntec Gold Class ")
    print(title)
    mainSecond = title.parent.parent.parent
    # main2S = mainSecond.find(text='Platinum')
    class1S = mainSecond.find(text='10:40PM').parent
    print(class1S['class'])
    if 'seat_1' in class1S['class']:
        print("Not Changed")
    else:
        print("Changed in: ", time.time() - start_time)
        sys.exit()

if __name__ == "__main__":
    # main()
    schedule.every(5).seconds.do(main)
    while True:
        schedule.run_pending()