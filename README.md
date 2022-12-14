# PLM Embeddings for Unsupervised Topic Extraction from Scientific Abstracts



The source code used for my Master's Thesis in Data Science and Business Analytics at [**Bocconi University**](https://www.unibocconi.eu/wps/wcm/connect/bocconi/sitopubblico_en/navigation+tree/home/programs/master+of+science/data+science+and+business+analytics) entitled *"Pre-trained Language Model Embeddings: A case of Unsupervised Topic Extraction from Scientific Abstracts"* published in December 2022.

## Requirements

At least one GPU is required to run the code.

Before running, the required packages need to be installed by typing following commands (Using a virtual environment is recommended):

```
pip3 install -r requirements.txt
```

The following resources also need to be downloaded in NLTK:
```
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
```

## Overview

A prominent line of research in Topic Extraction is represented by Topic Models. nevertheless, such line of research presents significant shortcomings due to its foundation on probabilistic generative models.


A new approach to Topic Extraction is explored by Meng et al. through [**TopClus**](https://arxiv.org/abs/2202.04582), a model based on the clustering of embeddings obtained from Pre-trained language models - which is chosen as framework of reference for this research.


Among the potential application fields, the chosen one for this research is that of Academic Abstracts. In particular, the datasetonsists of the Abstracts of the published papers of PhD candidates at Politecnico di Milano.

For this reason, this body of research is not analysing Topic Extraction as a whole, but rather focusing on its potential to extract value from a specific type of Dataset that presents a small-scope and technical vocabulary. 

For this reason, the Thesis is aiming to answer to two main Research Questions:

1. Is it possible to fine-tune topic extraction methods for smaller and technical datasets?
2. Can extracted topics be used to recognize patterns and evolution in the corpus?

With regards to the evaluation of the results, both Qualitative and Quantitative metrics are defined. 

Concerning the first Research Question, the selected method - PLM Embeddings Clustering - is able to over-perform benchmark models on the Dataset.
With regards to the second Research Question, the experiment designed in this Thesis proves the model to be able to reflect a trend present in the original dataset, that of Academic Cross-Fertilization.

## Running PLM Embeddings Clustering

The entry script is [`3_latent_space_clustering/main.py`](3_latent_space_clustering/main.py) and the command line arguments are be displayed upon typing
```
python src/trainer.py -h
```
The topic discovery results are written to `results_${dataset}`.

The code provided in [`webscraping/`](webscraping/) allows to replicate the extraction of the same Abstracts corpora used in the Thesis.

Expected results, highlighting Cross-Fertilization, should look like the following:
```
Physics Department:
Topic 10: Magnetic,Ferromagnet,Metal,Surface,Formulation
Topic 14: Radio,Antenna,Distribution,TRanfer,Optimization
Topic 17: Component-Failure,Threat,Security,Criteria,Frequency
Topic 30: Forecasting,Data,Machine-Learning,Neural-Network,Data
Topic 45: Batteries,Green,Turbine,Wind,Environment
```


