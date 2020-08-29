import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():

    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

news_title = soup.find("div", class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text

print(news_title)
print("--------------------------------------------------------")
print(news_p)


# In[9]:


#JPL Mars Space Images - Featured Image


# In[10]:


jpl_url = "https://www.jpl.nasa.gov"
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)

html = browser.html
image_soup = BeautifulSoup(html, "html.parser")

image_path = image_soup.find_all("img")[3]["src"]
featured_image_url = jpl_url + image_path
print(featured_image_url)


# In[37]:


#Mars Weather


# In[31]:


mars_weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather_url)

html = browser.html 
weather_soup = BeautifulSoup(html, "html.parser")

mars_weather = weather_soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
print(mars_weather)


# In[13]:


#Mars Facts


# In[14]:


mars_facts_df = pd.read_html("https://space-facts.com/mars/")[1]
mars_facts_df


# In[15]:


mars_html = mars_facts_df.to_html()
print(mars_html)


# In[24]:


#Mars Hemispheres


# In[23]:


#Cerberus Hemisphere
url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

cerberus_url = soup.find('div', class_='downloads')
link = cerberus_url.find('a')
href_cerberus = link['href']

print(href_cerberus)


# In[25]:


#Schiaparelli Hemisphere
url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

schiaparelli_url = soup.find('div', class_='downloads')
link = schiaparelli_url.find('a')
href_schiaparelli = link['href']

print(href_schiaparelli)


# In[26]:


#Syrtis Hemisphere
url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

syrtis_url = soup.find('div', class_='downloads')
link = syrtis_url.find('a')
href_syrtis = link['href']

print(href_syrtis)


# In[27]:


#Valles Hemisphere
url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

valles_url = soup.find('div', class_='downloads')
link = valles_url.find('a')
href_valles = link['href']

print(href_valles)


# In[30]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": href_cerberus},
    {"title": "Schiaparelli Hemisphere", "img_url": href_schiaparelli},
    {"title": "Syrtis Major Hemisphere", "img_url": href_syrtis},
    {"title": "Valles Marineris Hemisphere", "img_url": href_valles}
]
print(hemisphere_image_urls)


# In[ ]:




