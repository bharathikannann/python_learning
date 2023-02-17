# Best practices for pytorch
# 1. Deleting the model from GPU memory, and also from cache

# -----------------Importing libraries -----------------
import gc
import torch


# ----------------- Deleting the model from GPU memory, and also from cache -----------------
example_model = torch.nn.Linear(10, 10)

# Delete the model from GPU memory, and also from cache
del example_model
gc.collect()
torch.cuda.empty_cache()