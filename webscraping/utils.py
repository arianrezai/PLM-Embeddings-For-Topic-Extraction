import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def clean_sentences(sentence):
    cleaned_sentence = ''
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    for elem in tagged:
      if elem[1] in ('NN','NNS','NNP','NNPS','FW','JJ','JJR','JJS'):
          cleaned_sentence += elem[0]
          cleaned_sentence += ' '
    return cleaned_sentence

def group_years(row):
   if row['date'] == 2012 or row['date'] == 2013 or row['date'] == 2014 or row['date'] == 2015:
      return '12-15'
   if row['date'] == 2016 or row['date'] == 2017 or row['date'] == 2018 or row['date'] == 2019:
      return '16-19'
   if row['date'] == 2020 or row['date'] == 2021 or row['date'] == 2022:
      return '20-22'

      
department_association = {"DIPARTIMENTO DI ARCHITETTURA E PIANIFICAZIONE": "Architecture",
       "DIPARTIMENTO DI ARCHITETTURA E STUDI URBANI": "Architecture",
       "DIPARTIMENTO DI BIOINGEGNERIA" : "Electronic_Information_Bioengineering",
       "DIPARTIMENTO DI ARCHITETTURA, INGEGNERIA DELLE COSTRUZIONI E AMBIENTE COSTRUITO": "Architecture",
       'DIPARTIMENTO DI CHIMICA, MATERIALI E INGEGNERIA CHIMICA "GIULIO NATTA"': "Chemistry",
       "DIPARTIMENTO DI CHIMICA, MATERIALI E INGEGNERIA CHIMICA GIULIO NATTA": "Chemistry",
       "DIPARTIMENTO DI DESIGN" : "Design",
       "DIPARTIMENTO DI ELETTRONICA, INFORMAZIONE E BIOINGEGNERIA" : "Electronic_Information_Bioengineering",
       "DIPARTIMENTO DI ELETTRONICA E INFORMAZIONE" : "Electronic_Information_Bioengineering",
       "DIPARTIMENTO DI ELETTROTECNICA" : "Electronic_Information_Bioengineering",
       "DIPARTIMENTO DI ENERGIA" : "Physics",
       "DIPARTIMENTO DI FISICA" : "Physics",
       "DIPARTIMENTO DI INDUSTRIAL DESIGN, DELLE ARTI, DELLA COMUNICAZIONE E DELLA MODA" : "Design",
       "DIPARTIMENTO DI INGEGNERIA AEROSPAZIALE" : "Aerospatial_Sciences",
       "DIPARTIMENTO DI INGEGNERIA CIVILE E AMBIENTALE" : "Civil_Engineering",
       "DIPARTIMENTO DI INGEGNERIA GESTIONALE" : "Management_Engineering",
       "DIPARTIMENTO DI INGEGNERIA IDRAULICA, AMBIENTALE, INFRASTRUTTURE VIARIE, RILEVAMENTO" : "Civil_Engineering",
       "DIPARTIMENTO DI INGEGNERIA STRUTTURALE" : "Civil_Engineering",
       "DIPARTIMENTO DI MATEMATICA" : "Mathematics",
       "DIPARTIMENTO DI MATEMATICA FRANCESCO BRIOSCHI" : "Mathematics",
       "DIPARTIMENTO DI MECCANICA" : "Mechanics",
       "DIPARTIMENTO DI PROGETTAZIONE DELL'ARCHITETTURA" : "Architecture",
       "DIPARTIMENTO DI SCIENZA E TECNOLOGIE DELL'AMBIENTE COSTRUITO" : "Architecture",
       "DIPARTIMENTO DI SCIENZE E TECNOLOGIE AEROSPAZIALI" : "Aerospatial_Sciences"
       
}
