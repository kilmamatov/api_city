from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///geonames.db', echo=True)

Base: DeclarativeMeta = declarative_base()




