#用原生Python读取数据
fp=open("iris.csv","r")
next(fp)
iris_data=[]
for line in fp:
	record = line.strip().split(".")
	iris_data.append(record)
print(iris_data[:5])