#四种属性特征的平均值 条状图
import pandas as pd
from matplotlib import pyplot as plt

iris_data=pd.read_csv("iris.csv")
iris_mean=iris_data.mean()
iris_mean.plot(kind="bar",rot=45)
plt.show()