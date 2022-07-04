import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import json

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40),unique=True)

    def __str__(self):
        return f'{self.name = }, {self.id = }'


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40),unique=True)

    def __str__(self):
        return f'Shop: {self.id}, {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40),nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)
    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL,nullable=False)
    date_sale = sq.Column(sq.Date,nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)
    stock = relationship(Stock, backref='sale')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def init_test_data(session):
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale
        }[record.get('model')]
        session.add(model(id=record.get('pk'),**record.get('fields')))
    session.commit()

#Задание 2
# Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

def select_shops_on_publisher(session, publisher_name):
    result = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()
    for i in result:
        print(i)



