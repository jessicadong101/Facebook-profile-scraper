import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from PIL import Image

def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    return img.crop(((img_width - crop_width) // 2,
                    (img_height - crop_height) // 2,
                    (img_width + crop_width) // 2,
                    (img_height + crop_height) // 2))

def crop_max_square(img):
	return crop_center(img, min(img.size), min(img.size))

# get the url and candidate name from csv file
def get_urls(file):
    contents = []
    with open(file,'r') as csvf:
        urls = csv.reader(csvf)
        for url in urls:
            url = [x for x in url if x!='']
            contents.append(url)
    return contents

# download images
def download_image(driver, url, image_class, alt, filename):
    try:
        driver.get(url)
        time.sleep(5)
        try:
            pfp = driver.find_element_by_class_name(image_class)
            pfp.click()
            time.sleep(5)

            url = driver.current_url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            img_tags = soup.find(itemprop="image")["src"]
            with open('pics/' + filename + '.jpg', 'wb') as f:
                response = requests.get(img_tags)
                f.write(response.content)

        except:
            try:
                pfp = driver.find_element_by_class_name(alt)
                pfp.click()
                time.sleep(5)

                url = driver.current_url
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                img_tags = soup.find(itemprop="image")["src"]
                with open('pics/' + filename + '.jpg', 'wb') as f:
                    response = requests.get(img_tags)
                    f.write(response.content)

            except:
                try:
                    url = driver.current_url
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    img_tags = soup.find("img",{"class":"spotlight"})["src"]
                    with open('pics/' + filename + '.jpg', 'wb') as f:
                        response = requests.get(img_tags)
                        f.write(response.content)

                except:
                    try:
                        pfp = driver.find_element_by_xpath("//div[2]/div/div/div/a/img")
                        pfp.click()
                        time.sleep(5)
                        urls = driver.current_url
                        response = requests.get(urls)
                        soup = BeautifulSoup(response.content, "html.parser")
                        img_tags = soup.find(itemprop="image")["src"]
                        with open('pics/' + filename + '.jpg', 'wb') as f:
                            response = requests.get(img_tags)
                            f.write(response.content)

                    except:
                        return [filename, url]
    except:
        pass
    im = Image.open('pics/' + filename + '.jpg')
    im_cropped = crop_max_square(im)
    im_cropped.save('pics/' + filename + '.jpg')
# make csv based off content
def make_csv(arr):
    with open("fb_photo_redo.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(arr)

def main():
    driver = webdriver.Chrome('/Users/jessicadong/Downloads/chromedriver')  # where chromedriver is stored
    URLS = get_urls('candidate_fb_links.csv')
    image_class = '_2dgj'
    alt = '_1nv3 _11kg _1nv5 profilePicThumb'
    error = []
    # login in fb
    driver.get('https://www.facebook.com')
    time.sleep(5)
    for url in URLS:
        name = url[0]
        url = url[1:]
        if len(url) == 1:
            content = download_image(driver, url[0], image_class, alt, name)
            if content != None:
                error += [content]
        else:
            if len(url) == 0:
                error += [[name, '']]
            for i, link in enumerate(url,1):
                content = download_image(driver, link, image_class, alt, name +'_' + str(i))
                # content = download_image(driver, link, image_class, alt, name)
                if content != None:
                    error += [content]
    driver.quit()
    make_csv(error)

main()
