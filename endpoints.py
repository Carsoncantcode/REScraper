from fastapi import APIRouter
from models import *
from harvester import * 

router = APIRouter()

@router.post('/for_sale')
async def forSaleListings(data: ScrapePropertyParameters):
    listings = scrapeForSale(data)
    return listings

@router.post('/sold')
async def soldListings(data: ScrapePropertyParameters):
    listings = scrapeForSale(data)
    return listings

@router.post('/for_rent')
async def forRentListings(data: ScrapePropertyParameters):
    listings = scrapeForSale(data)
    return listings
