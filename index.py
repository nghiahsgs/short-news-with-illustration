import os
from selenium import webdriver
import cv2

class ShortNews():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        
        self.file_path_screen_shot = "screenshot.png"
        self.start_x, self.start_y, self.end_x, self.end_y = (
            15, 15, 600+15, 600+15)

    def converHTML2png(self):
        file_path_html = '%s\index.html' % os.getcwd()
        self.driver.get(file_path_html)
        self.driver.get_screenshot_as_file(self.file_path_screen_shot)
        
    
    def cropImage(self):
        img_0 = cv2.imread(self.file_path_screen_shot)
        img_crop = img_0[self.start_y:self.end_y, self.start_x:self.end_x]
        cv2.imwrite(self.file_path_screen_shot, img_crop)

bot=ShortNews()
bot.converHTML2png()
bot.cropImage()
