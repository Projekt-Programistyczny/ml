import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, desc 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.links import Link as ModelLink
from models.real_estates import RealEstates as ModelRealEstates

load_dotenv('.env')

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URI"]
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def add_category(url, category):
    with SessionLocal() as db:
        row = db.query(ModelRealEstates).filter_by(url=url).first()
        row.category = category
        db.commit()


def set_link_as_used(url):
    with SessionLocal() as db:
        row = db.query(ModelLink).filter_by(url=url).first()
        row.used = True
        db.commit()
    

def select_unused_and_active_links(city: str):
    with SessionLocal() as db:
        links_details = db.query(ModelLink).filter_by(city_name=city,
                                                      used=False,
                                                      is_active=True).all()
        return links_details
    
def select_used():
    with SessionLocal() as db:
        links_details = db.query(ModelRealEstates).all()
        return links_details

def select_joined_tables():
  with SessionLocal() as db:
    estates = db.query(ModelRealEstates, ModelLink).join(ModelLink, ModelRealEstates.url == ModelLink.url).filter_by(type_of_offer='sprzedaz').all()
    return estates