import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():

    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

mars_info = {}

#NASA Mars News
def scrape_news():

    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text

    mars_info["news_title"] = news_title
    mars_info["news_p"] = news_p

    return mars_info

    browser.quit()


#JPL Mars Space Images - Featured Image

def scrape_image():

    browser = init_browser()

    jpl_url = "https://www.jpl.nasa.gov"
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")

    image_path = image_soup.find_all("img")[3]["src"]
    featured_image_url = jpl_url + image_path

    mars_info["featured_image_url"] = featured_image_url

    return mars_info

    browser.quit()


#Mars Weather



#Mars Facts

def scrape_facts():

    browser = init_browser()

    mars_facts_df = pd.read_html("https://space-facts.com/mars/")[1]
    mars_facts_df


    mars_html = mars_facts_df.to_html()

    mars_info["mars_facts_df"] = mars_html

    return mars_info

    browser.quit()

#Mars Hemispheres

#Cerberus Hemisphere

def scrape_cerberus():

    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    cerberus_url = soup.find('div', class_='downloads')
    link = cerberus_url.find('a')
    href_cerberus = link['href']

    mars_info["href_cerberus"] = href_cerberus

    return mars_info

    browser.quit()


#Schiaparelli Hemisphere

def scrape_schiaprelli():

    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    schiaparelli_url = soup.find('div', class_='downloads')
    link = schiaparelli_url.find('a')
    href_schiaparelli = link['href']

    mars_info["href_schiaparelli"] = href_schiaparelli

    return mars_info

    browser.quit()

#Syrtis Hemisphere

def scrape_syrtis():

    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    syrtis_url = soup.find('div', class_='downloads')
    link = syrtis_url.find('a')
    href_syrtis = link['href']

    mars_info["href_syrtis"] = href_syrtis

    return mars_info

    browser.quit()


#Valles Hemisphere

def scrape_valles():

    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    valles_url = soup.find('div', class_='downloads')
    link = valles_url.find('a')
    href_valles = link['href']

    mars_info["href_valles"] = href_valles

    return mars_info

    browser.quit()