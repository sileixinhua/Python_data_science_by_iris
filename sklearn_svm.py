import pandas as pd 
from sklearn import svm,metrics,cross_validation

iris_data=pd.read_csv("iris.csv")

x=iris_data[["sepal_length","sepal_width","petal_length","petal_width"]]
y=iris_data["species"]

x_train,x_test,y_train,y_test=cross_validation.train_test_split(x.values,y.values,test_size=0.1)
clf=svm.SVC()
clf.fit(x_train,y_train)
pre=clf.predict(x_test)

score=metrics.accuracy_score(y_test,pre)
print(score)
