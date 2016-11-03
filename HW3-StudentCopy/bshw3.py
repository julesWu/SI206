#name: Julia Wu
#UMID: 38632603
#Unique name: shuyue
#References: 

import re
import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

f = open('webpage.html', 'w')

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'

html_doc = urllib.request.urlopen(base_url).read()

soup_1 = BeautifulSoup(html_doc, 'html.parser')

filename = '/Users/jules.wu/Desktop/Project.3/HW3-StudentCopy/media/logo.png'

visible_text = (soup_1.prettify())
#print (visible_text)

im_str = visible_text.replace('/sites/default/themes/umsi/imgs/logo.png',filename)

text = im_str.replace('students', 'AMAZING student')

#images = re.findall('^/sites/default/themes/umsi/img\S+', text)
#print (images)

f.write(text)
f.close()

#filename = '/Users/jules.wu/Desktop/Project.3/HW3-StudentCopy/webpage.html'
#webbrowser.open_new_tab(filename)

###
#Find the picture and change img source (specific pic) and replace it with your picture
#replace logo picture (use regular expressions to do this)
