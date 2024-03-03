from homeharvest import scrape_property
from datetime import datetime
from models import *
import numpy as np
import pandas as pd



def scrapeForSale(data: ScrapePropertyParameters):
    #current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #filename = f"HomeHarvest_{current_timestamp}.csv"

    properties = scrape_property(
        location=data.location,
        listing_type="for_sale", 
        past_days=data.past_days, 
        radius=data.radius,
        # proxy="http://user:pass@host:port"  # use a proxy to change your IP address
    )

    properties = properties.replace([np.nan, np.inf, -np.inf], None)

    properties_list = properties.to_dict(orient='records')

    #print(f"Number of properties: {len(properties)}")

    #properties.to_csv(filename, index=False)
    #print(properties.head())

    return properties_list

def scrapeSold(data: ScrapePropertyParameters):
    

    properties = scrape_property(
        location=data.location,
        listing_type="sold", 
        past_days=data.past_days, 
        radius=data.radius,
    )
    
    properties = properties.replace([np.nan, np.inf, -np.inf], None)

    properties_list = properties.to_dict(orient='records')

    print()

    

    return properties_list

def scrapeForRent(data: ScrapePropertyParameters):

    properties = scrape_property(
        location=data.location,
        listing_type="for_rent", 
        past_days=data.past_days, 
        radius=data.radius,
    )

    properties = properties.replace([np.nan, np.inf, -np.inf], None)

    properties_list = properties.to_dict(orient='records')

    
    return properties_list