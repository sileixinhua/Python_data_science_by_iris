#条状图显示组平均数，可以从图上看出不同的花种类中，他们的属性特点。
import pandas as pd
from matplotlib import pyplot as plt

iris_data=pd.read_csv("iris.csv")
#读取数据
grouped_data=iris_data.groupby("species")
#用不同的花的类别分成不同的组，此数据为三组
group_mean=grouped_data.mean()
#求组平均值
group_mean.plot(kind="bar")
plt.legend(loc="upper center",bbox_to_anchor=(0.5,1.2),ncol=2)
plt.show()
#画图