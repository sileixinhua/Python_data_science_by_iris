#用pandas读取数据
import pandas as pd

iris_data=pd.read_csv("iris.csv")
print(iris_data.head(5))