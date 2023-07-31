from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Geoname(Base):
    __tablename__ = "geonames"
    geonameid: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    asciiname: Mapped[str] = mapped_column(String, nullable=True)
    alternatenames: Mapped[str] = mapped_column(String, nullable=True)
    latitude: Mapped[str] = mapped_column(String, nullable=True)
    longitude: Mapped[str] = mapped_column(String, nullable=True)
    feature_class: Mapped[str] = mapped_column(String, nullable=True)
    feature_code: Mapped[str] = mapped_column(String, nullable=True)
    country_code: Mapped[str] = mapped_column(String, nullable=True)
    cc2: Mapped[str] = mapped_column(String, nullable=True)
    admin1_code: Mapped[str] = mapped_column(String, nullable=True)
    admin2_code: Mapped[str] = mapped_column(String, nullable=True)
    admin3_code: Mapped[str] = mapped_column(String, nullable=True)
    admin4_code: Mapped[str] = mapped_column(String, nullable=True)
    population: Mapped[str] = mapped_column(String, nullable=True)
    elevation: Mapped[str] = mapped_column(String, nullable=True)
    dem: Mapped[str] = mapped_column(String, nullable=True)
    timezone: Mapped[str] = mapped_column(String, nullable=True)
    modification_date: Mapped[str] = mapped_column(String, nullable=True)


