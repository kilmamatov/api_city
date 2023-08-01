import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Geoname


SQLALCHEMY_DATABASE_URL = "sqlite:///geonames.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


def fill_database():
    with open('RU.txt', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for new_list in reader:
            data = Geoname(
                geonameid=new_list[0],
                name=new_list[1],
                asciiname=new_list[2],
                alternatenames=new_list[3],
                latitude=new_list[4],
                longitude=new_list[5],
                feature_class=new_list[6],
                feature_code=new_list[7],
                country_code=new_list[8],
                cc2=new_list[9],
                admin1_code=new_list[10],
                admin2_code=new_list[11],
                admin3_code=new_list[12],
                admin4_code=new_list[13],
                population=new_list[14],
                elevation=new_list[15],
                dem=new_list[16],
                timezone=new_list[17],
                modification_date=new_list[18],
            )
            session.add(data)
        session.commit()


session.close()

