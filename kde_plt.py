#画kde图
import pandas as pd
from matplotlib import pyplot as plt

iris_data=pd.read_csv("iris.csv")
iris_data.plot(kind="kde",subplots=True,figsize=(10,6))
plt.show()