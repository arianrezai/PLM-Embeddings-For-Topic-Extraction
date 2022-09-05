import gc

model.cpu()
gc.collect()
torch.cuda.empty_cache()
