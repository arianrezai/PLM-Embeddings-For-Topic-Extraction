from bs4 import BeautifulSoup
import requests
import pandas as pd

# Thesis are numbered and reach number 3200
search_num = range(100,3200,100) 
politesi_url_list = []
politesi_url_list.append('https://www.politesi.polimi.it/handle/10589/32801/simple-search?location=10589%2F32801&query=&rpp=100&sort_by=score&order=ASC&submit_search=Aggiorna')
for idx in range(len(search_num)):
  new_url = 'https://www.politesi.polimi.it/handle/10589/32801/simple-search?query=&sort_by=score&order=asc&rpp=100&etal=0&start={}'.format(search_num[idx])
  politesi_url_list.append(new_url)


thesis_link_list = []
link_start = 'https://www.politesi.polimi.it/'

for url in politesi_url_list:
  response = requests.get(url)
  soup= BeautifulSoup(response.text, "lxml")
  table = soup.find(class_="table table-striped table-hover")
  for a in table.find_all('a', href=True):
    thesis_link_list.append(link_start+a['href']+'?mode=complete')

thesis_link_list = list(set(thesis_link_list))




thesis_description = []
date = []
department = []
course = []
thesis_title = []
key_words = []
language= []
for url in thesis_link_list:
  response = requests.get(url)
  soup= BeautifulSoup(response.text, "lxml")
  thesis_description.append(soup.find(class_="metadataFieldValue dc_description_abstracteng").em.text)
  date.append(soup.find(class_="metadataFieldValue dc_date_issued").em.text)
  department.append(soup.find(class_="metadataFieldValue dc_description_researchstructure").em.text)
  if soup.find(class_="metadataFieldValue dc_relation_course") is not None:
    course.append(soup.find(class_="metadataFieldValue dc_relation_course").em.text)
  else:
    course.append(None)
  thesis_title.append(soup.find(class_="metadataFieldValue dc_title").a.text)
  key_words.append(soup.find(class_="metadataFieldValue dc_subject_keywordseng").em.text)
  language.append(soup.find(class_="metadataFieldValue dc_language_iso").em.text)




  #Create a DB


polimi_thesis = pd.DataFrame({"department" :department,
                              "course": course,
                              "date" : date,
                              "thesis_title":thesis_title,
                              "thesis_description":thesis_description,
                              "key_words":key_words,
                              "language":language})
polimi_thesis.to_csv()

"""
#Create a .txt file

with open('webscraping/texts.txt', 'w') as f:
  for abstract in thesis_description:
    f.write(abstract.replace("\r\n", " "))
    f.write('\n')
    f.close()
"""