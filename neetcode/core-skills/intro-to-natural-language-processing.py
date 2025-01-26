import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        max_len = 0
        token_set = set()
        for enc in [positive, negative]:
            for s in enc:
                split = s.split()
                max_len = max(max_len, len(split))
                token_set.update(split)
        token_list = sorted(list(token_set))
        token_dict = {token: i + 1 for i, token in enumerate(token_list)}

        res = torch.zeros((2 * len(positive), max_len))
        idx = 0
        for enc in [positive, negative]:
            for s in enc:
                for i, t in enumerate(s.split()):
                    res[idx, i] = token_dict[t]
                idx += 1
        
        return res