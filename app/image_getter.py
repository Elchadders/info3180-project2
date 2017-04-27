import requests
from bs4 import BeautifulSoup
import urlparse

def return_unique(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]

def get_images(url):
	# url = "https://www.walmart.com/ip/54649026"
	images = []	
	result = requests.get(url)
	soup = BeautifulSoup(result.text, "html.parser")

	# This will look for a meta tag with the og:image property
	og_image = (soup.find('meta', property='og:image') or
	                    soup.find('meta', attrs={'name': 'og:image'}))
	if og_image and og_image['content']:
	    images += [str(og_image['content'])]

	# This will look for a link tag with a rel attribute set to 'image_src'
	thumbnail_spec = soup.find('link', rel='image_src')
	if thumbnail_spec and thumbnail_spec['href']:
	    images += [str(thumbnail_spec['href'])]

	image = """<img src="%s"><br />"""
	for img in soup.findAll("img", src=True):
	   images += [str(urlparse.urljoin(url, img["src"]))]
	
	return return_unique(images)
