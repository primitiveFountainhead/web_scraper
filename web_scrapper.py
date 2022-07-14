#taken from geeks for geeks
from tqdm import tqdm
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


DIR = "img"

  
htmldata = urlopen('https://commons.wikimedia.org/w/index.php?search=Telugu+board&title=Special%3AMediaSearch')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

i=0
for item in tqdm(images):
    img_url = item['src']
    f = img_url.split('/')[-1]
    f = DIR+"/"+str(i)+"_" + f
    urlretrieve(img_url, f)
    i += 1
