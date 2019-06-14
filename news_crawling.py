from bs4 import BeautifulSoup
import requests
import schedule
import time
from time import gmtime, strftime

# default url - 1
url = "https://stomp.straitstimes.com/singapore-seen"
shortUrl = "https://stomp.straitstimes.com"


def getList(url, shortUrl):
    collection = {}
    # bigDetails = {}
    details = {}
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # big headline news
    bigContent = soup.find('div', {'class': ['col-xs-12', 'col-sm-8', 'col-md-9', 'col-lg-9', 'main-card']})
    headLine = bigContent.find('h2', {'class': 'story-headline'})
    details['bigHeading'] = headLine.text.strip()    #   heading
    bigPara = bigContent.find('span', class_='story-blurb')
    details['bigPara'] = bigPara.text.strip()     #   paragraph
    # print(details['bigPara'])
    bigLink = bigContent.find('a', class_='ss_row1')
    details['bigLink'] = shortUrl + bigLink['href'].strip()    #   big head line next link
    bigPicture = bigContent.find('img', {'class': ['img-responsive', 'lazyloaded']})
    details['bigImgSource'] = bigPicture['src'].strip()    #   image source
    collection['bigKey1'] = {'heading': details['bigHeading']}
    collection['bigKey2'] = {'para': details['bigPara']}
    collection['bigKey3'] = {'link': details['bigLink']}
    collection['bigKey4'] = {'imgSource': details['bigImgSource']}

    # news section
    section = soup.find_all('div', {'class': ['views-row', 'views-row-1', 'views-row-odd', 'views-row-first', 'col-xs-12', 'col-sm-6', 'col-md-6', 'regular-box']})
    i = 1
    current = ""
    for news in section:
        link = news.find('a')
        if link != None:
            source = link['href']
            if source.find('bit.ly') == -1 and source.find('#') == -1 and source.find('www') == -1 and source.find(bigLink['href']) == -1 and source != str("/") and source.find('stomp') == -1:
                if current != source:
                    current = source
                    heading = news.find('h3', class_='story-headline')
                    img = news.find('img', {'class': ['img-responsive', 'lazyloaded']})
                    details['heading'] = heading.text.strip()   #   heading
                    details['link'] = source.strip()    #   source next link
                    details['imgSource'] = img['src'].strip()   #   image source
                    j = 1
                    while(j < 4):
                        key = "key" + str(i) + str(j)
                        collection[key]= {'heading': details['heading']}

                        j+=1
                        key = "key" + str(i) + str(j)
                        collection[key] = {'link': details['link']}

                        j+=1
                        key = "key" + str(i) + str(j)
                        collection[key] = {'imgSource': details['imgSource']}
                        j+=1
                    i+=1
    return collection

def display():
    details = getList(url, shortUrl)
    print("_____________________Time: {}_____________________". format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    print(details)
    print(len(details))

def main():
    # schedule.every(10).hours.do(print)
    display()
    # while(True):
    #     schedule.run_pending()
    #     time.sleep(0)
    if __name__ == "__main__":
             main()