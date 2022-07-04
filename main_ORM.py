import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models_ORM import create_tables,init_test_data,select_shops_on_publisher, Publisher, Book, Shop, Sale, Stock


DSN = "postgresql://postgres:ENot3112@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN,echo=True)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()
init_test_data(session)
select_shops_on_publisher(session,'Microsoft Press')




session.close()





