from app import app, db
from models import Paint, Colour, Brand
import sqlalchemy as sa
from helpers import apology
from app import db
from helpers import hex_to_rgb

def add_colour(brand="", name="", colour={}):
    #must have run sanitise_colour_input first
    #convert rgb to hsl
    #TODO

    #check if brand already exists
    #TODO add brand

    #check if colour already exists
    #TODO
        #return message and show colour
        #TODO

    #if not, add to database
    #TODO still need to add brand
    colour=Colour( R=colour['r'], G= colour['g'], B=colour['b'], H=0, S=0, L=0)
    db.session.add(colour)
    db.session.commit()
    paint=Paint(name = name, brand_id=1, colour_id=colour.id)
    db.session.add(paint)
    db.session.commit()

    return True
