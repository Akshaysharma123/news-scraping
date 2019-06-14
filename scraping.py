from bs4 import BeautifulSoup
import requests

# only stomp urls

# test url

url = "https://stomp.straitstimes.com/singapore-seen/man-who-got-tasered-and-pinned-down-by-officers-at-everton-park-arrested-for-multiple"


def getDetails(url):
    details = {}
    details['source'] = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())
    for data in soup.find_all('section', {'id': 'block-system-main'}):
        h1 = data.find("h1", {'class': 'headline'})
        heading = h1.text.strip()
        details['heading'] = heading # news heading
        
        div2 = data.find('div', class_='photoswipe-gallery')
        img = div2.find('img', class_='img-responsive')
        imgSource = img['src'].strip()
        details['imgSource'] =  imgSource # image source

        dt = data.find('div', class_='submitted').text
        subdt = dt.index("|")
        pubDate = dt[:subdt].strip()
        details['pubDate'] = pubDate # published date

        # attrs={"data-foo": "value"}
        paraDiv1 = soup.find('div', attrs={'property': 'content:encoded'})
        para = paraDiv1.find('p')
        paraData = para.text.strip()
        details['paraData'] = paraData # paragraph

        auth = data.find('div', class_='taxonomy-term-description')
        if auth.find('a') != None:
            author = auth.find('a').text.strip()
            details['author'] = author # if author available, then author
        else:
            details['author'] = "No author information"
    return details


# test here
details = getDetails(url)
print(details["source"])
print(details["pubDate"])
print(details["heading"])
print(details["imgSource"])
print(details["paraData"])
print(details["author"])
          