#用sklearn的逻辑斯蒂回归 训练数据集
import pandas as pd
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

x=pd.read_csv("iris.csv")
y=x.pop("species")
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x.values,y.values,test_size=0.1)

lr=LogisticRegression(multi_class="multinomial",solver="lbfgs").fit(x_train,y_train)
print(lr.predict_proba(x_test))