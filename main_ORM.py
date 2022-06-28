import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models_ORM import create_tables,init_test_data, Publisher, Book, Shop, Sale, Stock


DSN = "postgresql://postgres:ENot3112@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()
init_test_data(session)
session.close()

#Задание 2
# Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.
# Напишите Python скрипт, который:
# Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
# Импортирует необходимые модели данных.
# Выводит издателя (publisher), имя или идентификатор которого принимается через input().
publisher_name = input('Введите имя издателя: ')
print(publisher_name)
print(publisher_name.id)




