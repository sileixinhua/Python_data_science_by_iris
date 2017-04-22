#用sklearn的交叉验证 KNN 逻辑蒂斯回归 三种方式 训练数据集 并对比
import pandas as pd
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

x=pd.read_csv("iris.csv")
y=x.pop("species")
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x.values,y.values,test_size=0.1)

models={
	"knn":KNeighborsClassifier(6),
	"gnb":GaussianNB(),
	"lr":LogisticRegression(multi_class="multinomial",solver="lbfgs")
}

for name,model in models.items():
	score=cross_validation.cross_val_score(model,x,y,cv=5).mean()
	print(name,score)