from bs4 import BeautifulSoup
import emoji
import re
from plyer import notification
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os
import schedule