#绘制样本图
import pandas as pd
from matplotlib import pyplot as plt

iris_data=pd.read_csv("iris.csv")
for name,symbol in zip(("setosa","versicolor","virginica"),("o","s","*")):
	data=iris_data[iris_data["species"]==name]
plt.plot(data["petal_length"],data["petal_width"],symbol)
plt.show()
