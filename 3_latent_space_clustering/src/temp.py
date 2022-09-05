#import nltk
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('universal_tagset')
"""import os
os.system['CUDA_LAUNCH_BLOCKING=1']
import torch 
import gc
gc.collect()
torch.cuda.empty_cache()"""
"""
from GPUtil import showUtilization as gpu_usage
gpu_usage()"""
from numba import cuda

gpus = cuda.gpus.lst

for gpu in gpus:
    with gpu:
        meminfo = cuda.current_context().get_memory_info()
        print("{} %, free_memory / total in bytes".format(meminfo[0]/meminfo[1]))

