# Description:  Hooks in PyTorch
# Hooks are a way to access the internal state of a module during forward and backward passes.
# Useful links: https://youtu.be/syLFCVYua6Q?t=650

import torch

a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)

c = a * b


def c_hook(grad):
    print("c_hook: ", grad)
    return grad + 2

h = c.register_hook(c_hook)
c.register_hook(lambda grad: print("c_hook2: ", grad))
c.retain_grad()

d = torch.tensor(4.0, requires_grad=True )

d.register_hook(lambda grad: print("d_hook: ", grad))
d.register_hook(lambda grad: grad * 2)

e = c * d 

e.retain_grad()
e.register_hook(lambda grad: grad *2)

# This will remove the hook
h.remove()

e.backward()

