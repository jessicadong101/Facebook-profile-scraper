# Facebook-profile-scraper

 A script that can be used to automate downloading the Facebook profile photos.

### Files

* fb_image_scraper.py: Script used for downloading Facebook profile photos.
* fb_links.csv: CSV file with person's name and facebook profile link separated by a comma. See provided file as a sample.


### Installing

Install the given files. Update the fb_links.csv to match the profile pictures you want downloaded. Make sure to also include a folder titled "pics" in the same directorry as the other files listed above. The pictures will be automatically stored in the "pics" folder. You also need to have ChromeDriver downloaded.

```
python3 fb_image_scraper.py
```


## Rules

* Before starting, change '/Users/jessicadong/Downloads/chromedriver' in line 96 of fb_image_scraper.py to match the location of ChromeDriver on your laptop.

* Once script is running, you will be directed to Facebook's home page. The script will give you 5 seconds to log into your Facebook account. Feel free to edit "time.sleep(5)" in line 103 of fb_image_scraper.py to match how ever long you need to log into your Facebook.

* Let the script run. It will download the profile pictures provide in fb_links.csv and store it as a PDF file in the pics folder.
