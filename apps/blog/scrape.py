import requests
from bs4 import BeautifulSoup
from apps.blog.models import Blog



def scrape_news():
    url = 'http://kun.uz/'
    response = requests.get(url) 
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    blog_list = soup.find_all('div', {"class" : "container mb-50"}) 
    small_items = soup.find_all('div', {"class": "small-news"})
    recent_news = soup.find_all('div', {"class": "news-lenta"})

    blogs = {
        "blog": [],
        "small_items": [],
        "recent_news": [],
    }
    
    for blog in blog_list:
        title = blog.find("span", {'class': 'big-news__title'}).text.strip()
        description = blog.find("span", {'class': 'big-news__description'}).text.strip()
        image = blog.find("img", {'class': 'big-news__img'})

        if image:
            image_url = image["src"]
        else:
            image_url = "https://kun.uz/default-image.jpg"

        blogs["blog"].append({
            'title' : title,
            'description' : description,
            'image' : image_url,
        })

    for small_item in small_items:
        title = small_item.find("div", {"class" : "small-news__content"}).text.strip()
        image = small_item.find("img", {"src" : "small-news__img"})

        if image:
            image_url = image["src"]
        else:
            image_url = "https://kun.uz/default-image.jpg"

        blogs["small_items"].append({
            "title": title,
            "image": image_url
        })

    for recent_new in recent_news:
        time = recent_new.find("div", {"class" : "news-meta"}).text.strip()
        title = recent_new.find("div", {"class" : "news-lenta__title"}).text.strip()
        print(title)
        blogs["recent_news"].append({
            "time":time,
            "title":title,
        })

    return blogs

