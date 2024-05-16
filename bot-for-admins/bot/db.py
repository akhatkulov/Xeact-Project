from sqlalchemy import create_engine,Integer,Text,func,Column
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("postgresql://postgres:1945@localhost/postgres")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
class Kino():
    __tablename__ = 'kino_xeact'
    id = Column(Integer,primary_key=True,autoincriment=True)
    name = Column(Text,nullable=False)
    about = Column(Text,nullable=False)
    pic_link = Column(Text,nullable=False)
    down_link = Column(Text,nullable=False)

def mk_vd(name,about,pic_link,down_code):
    x = Kino(name,about,pic_link,down_code)
    session.add(x)
    session.commit()

def cnt_vd() -> int:
    x = session.query(func.count(Kino)).all()
    print(x)
    return x

def get_vd():
    x = session.query(Kino).all()
    print(x)
    return x

def get_data(page):
    res = page*10
    x = []
    for i in range(page-1,res):
        x.append({"id":i+1,"name":get_vd()[i][0],"description":get_vd()[i][1],"down_link":get_vd()[i][3],"photo_link":get_vd()[i][2]})
        print(x)
    return x