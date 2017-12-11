import numpy as np
import pandas as pd


def index_tenfold(n:int) ->np.ndarray:
    """Produce index array for tenfold CV with dataframe length n."""
    original_indices = np.arange(n)
    tenfold_indices = np.zeros(n)

    div, mod = divmod(n, 10)
    unit_sizes = [div for _ in range(10)]
    for i in range(mod):
        unit_sizes[i] += 1

    for k, unit_size in enumerate(unit_sizes):
        tenfold = np.random.choice(original_indices, unit_size,
                                   replace=False)
        tenfold_indices[tenfold] = k
        original_indices = np.delete(
            original_indices,
            [np.argwhere(original_indices == val) for val in tenfold],
        )
        # print(tenfold, original_indices)
    return tenfold_indices