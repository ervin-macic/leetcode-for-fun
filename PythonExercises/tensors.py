import torch

def mystery(t):
    t = t.clone()
    t[t < 0] = 0
    t = t / (t.sum(dim=1, keepdim=True) + 1e-8)
    return t

x = torch.tensor([[1.0, -2.0, 3.0],
                  [-1.0, 0.0, 2.0]])
y = mystery(x)
print(y)
