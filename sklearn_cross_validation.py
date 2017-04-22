#用sklearn的交叉验证 训练数据集
import pandas as pd
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier

x=pd.read_csv("iris.csv")
y=x.pop("species")
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x.values,y.values,test_size=0.1)

scores=cross_validation.cross_val_score(KNeighborsClassifier(3),x,y,cv=5)
mean_score=scores.mean()
print(mean_score)