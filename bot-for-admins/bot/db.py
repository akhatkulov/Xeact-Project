from sqlalchemy import create_engine,Integer,Text,func,Column
from sqlalchemy.orm import declarative_base,sessionmaker
from pprint import pprint
engine = create_engine("postgresql://postgres:1945@localhost/postgres")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
class Kino(Base):
    __tablename__ = 'kino_xeact'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(Text,nullable=False)
    about = Column(Text,nullable=False)
    pic_link = Column(Text,nullable=False)
    down_link = Column(Text,nullable=False)
Base.metadata.create_all(engine)
def mk_vd(name,about,pic_link,down_code):
    x = Kino(name=name,about=about,pic_link=pic_link,down_link=down_code)
    session.add(x)
    session.commit()

def cnt_vd() -> int:
    x = session.query(func.count(Kino.id)).first()
    print(x[0])
    return x[0]
cnt_vd()

def get_data(page):
    res = page*10
    x = []

    for i in range(page-1,res):
        l = session.query(Kino).filter_by(id=i+1).one_or_none()
        x.append({"id":i+1, "name":l.name, "description":l.about, "down_link":l.down_link, "photo_link":l.pic_link})
        pprint(x)
    return x
get_data(1)