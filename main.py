from fastapi import FastAPI
import LivePriceScraper as LPS
import TodayPriceScraper as TPS
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Welcome To Nepse Live Data API'}

@app.get('/liveprice')
async def liveprice():
    return LPS.LivePrice

@app.get('/todayprice')
async def todayprice():
    return TPS.todayprice