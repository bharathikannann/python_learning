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


class ExampleModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.linear(x)

# -----------------------Detach the model from the graph-----------------------

example_tensor = torch.rand(10, 10)
example_output = example_model(example_tensor).detach()

