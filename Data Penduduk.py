import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({
        "Nama": ["Amalaia","Riko","Rio","Bui","Ucok"],
        "Umur": [17, 18, 17, 3, 19],
        "Gender":["P","L","L","L","L"]
})
print(data)

cd = data.info()
print(cd)
dc = pd.DataFrame(data=data)
print=(dc)