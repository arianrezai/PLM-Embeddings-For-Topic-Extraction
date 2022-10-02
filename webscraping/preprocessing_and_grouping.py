import pandas as pd
import nltk
import os
from utils import *


df = pd.read_csv('polimi_thesis.csv')
df["date"] = df.date.str[-4:].astype(int)
df['department'] = df['department'].replace(department_association)
df['years'] = df.apply(lambda row: group_years(row), axis=1)
df2 = pd.DataFrame(df.groupby(['department','years'])['thesis_title'].count()).reset_index()
os.chdir("..")
external_path = os.path.join(os.path.abspath(os.curdir), "3_latent_space_clustering/datasets")
os.chdir(external_path)
for idx, row in df2.iterrows():
  department = row.department
  years = row.years
  mask = (df.years == years) & (df.department == department)
  thesis_abstract = df.loc[mask, 'thesis_description'].to_list()
  cleaned_sentences_no_verbs = [clean_sentences(elem) for elem in thesis_abstract if len(elem)>16]
  path = os.path.join(external_path, "{}_{}".format(department, years))
  os.mkdir(path)
  os.chdir(path)
  
  with open("texts.txt", 'w') as f:
       for abstract in cleaned_sentences_no_verbs:
              f.write(abstract.replace("\r\n", " "))
              f.write('\n')
  