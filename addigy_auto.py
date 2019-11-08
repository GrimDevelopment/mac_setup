import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
subprocess.call(["safaridriver", "--enable"])
safari = webdriver.Safari()

safari.get("http://prod.addigy.com")