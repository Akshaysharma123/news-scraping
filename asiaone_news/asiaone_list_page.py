import requests
from bs4 import BeautifulSoup

# def main2():
    
main_url = "https://www.asiaone.com/singapore"
shortUrl = "https://www.asiaone.com"

# col-xs-12

# Getting individual cities url
def getDetails(main_url):
    data = []
    # data['main_source'] = main_url #site-url
    re = requests.get(main_url)
    soup = BeautifulSoup(re.text, "html.parser")

    heading_title = soup.find('h2',{'class':'pane-title'}).text

    data.append({
            'heading':heading_title,
        })
    # print(heading_title)

    ui_cards = soup.find_all('div', {'class':'ui cards'})
    ui_div_card = ui_cards[0].find_all('div', {'class':"card"})
   

    for card in ui_div_card:
        overlay = card.find('div', {'class':'content overlay'})
        image = card.find_all('img')
       
        if overlay is not None:
            href_link = overlay.find('a').get('href')
            href_text = overlay.find('a').text
        else:
            non_overlay = card.find('div', {'class':'content'})
            if non_overlay is not None:
                href_link = non_overlay.find('a').get('href')
                href_text = non_overlay.find('a').text

        img_src = ''
        for i in image:
            img_src = "{0}{1}".format(shortUrl, i['src'])

      
        data.append({
            # 'heading':col_heading,
            'href':href_link,
            'text':href_text,
            'image':img_src,
            # 'heading':href_heading
        })

    return data

details = getDetails(main_url)
for detail in details:
    print(detail)
    if __name__ == "__main__":
            import time
            start_time = time.time()
           
            print("--- %s seconds ---" % (time.time() - start_time))