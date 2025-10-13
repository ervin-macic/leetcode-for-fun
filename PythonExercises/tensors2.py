import torch

def weird_transform(x):
    # x: (N, M)
    x = x.clone() # make copy to avoid mutating x
    mean_col = x.mean(dim=0, keepdim=True) # 
    x = x - mean_col
    mask = x < 0
    x[mask] = 0
    x = x / (x.sum(dim=1, keepdim=True) + 1e-6)
    return x

a = torch.tensor([[1.0, 2.0, 3.0],
                  [3.0, 1.0, 2.0]])
b = weird_transform(a)
print(b)
