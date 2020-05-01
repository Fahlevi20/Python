import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
                    columns=["A","B","C"])
print(data)
cek = pd.DataFrame(data = data,dtype=np.int32)
print(cek)
cek2 = pd.DataFrame.INDEX
print= (cek2)