#from utils import TopClusUtils
import torch
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import argparse


def k_means(emb_path ,seed=42,n_clusters=3):
        embs = torch.load(emb_path)
        pca = PCA(2)
        transformed_embs = pca.fit_transform(embs.numpy())
        kmeans = KMeans(n_clusters=n_clusters, random_state=seed)
        label  = kmeans.fit_predict(transformed_embs)
        for idx, l in enumerate(label):
            print("Document {}: Topic {}".format(idx+1, l))
        u_labels = np.unique(label)
        for i in u_labels:
            plt.scatter(transformed_embs[label == i , 0] , transformed_embs[label == i , 1] , label = i)
        plt.savefig("mygraph.png")
        return 
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--emb_path')
    parser.add_argument('--n_clusters',type=int)
    args = parser.parse_args()
    k_means(emb_path = args.emb_path, n_clusters = args.n_clusters)