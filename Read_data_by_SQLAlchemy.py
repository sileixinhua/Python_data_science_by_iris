#用sqlalchemy 读取数据
import sqlalchemy

engine=sqlalchemy.create_engine("sqlite:///iris.db")

iris_data=pd.read_sql("SELECT * FROM iris",engine)
print(iris_data)