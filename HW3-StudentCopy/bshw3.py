#name: Julia Wu
#UMID: 38632603
#Unique name: shuyue
#References: Colleen Office Hours

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

#opens the html file and prepares the file for writing
f = open('webpage.html', 'w')

#the url that we are using
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'

#makes a request to the base_url, opens, and reads the webpage
html_doc = urllib.request.urlopen(base_url).read()

#use Beautiful soup to parse the webpage
soup_1 = BeautifulSoup(html_doc, 'html.parser')

#Path of the logo picture Collen wanted us to use.
filename = 'media/logo.png'

#Path of the picture of ourselves that we were supposed to use
my_pic = 'media/Pic.png'

#makes the code of the base_url page pretty (readable)
visible_text = (soup_1.prettify())

#looks through visible text and replaces the missing logos with our version of the logo
im_str = visible_text.replace('logo2.png',filename)

#looks through im_str to replace the big picture with a picture of myself
im_str3 = im_str.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', my_pic)

#looks through im_str3, and replaces any occurance of 'students' with 'AMAZING students'
text = im_str3.replace('students', 'AMAZING students')

#writes the text to the html file
f.write(text)

#closes the file
f.close()


