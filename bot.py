import json
import time
import datetime

import requests
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

"""
I am a trading bot, hehe
"""

# https://www.binance.com/
# https://www.bitfinex.com/

while True:
    bin_resp = requests.get('https://api.binance.com/api/v3/ticker/price')
    bit_resp = requests.get('https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD,tLTCUSD')
    if bin_resp.status_code != 200 or bit_resp.status_code != 200:
        print(bin_resp.status_code, bit_resp.status_code)
        raise ValueError
    bin_content = json.loads(bin_resp.content)
    bin_BTCUSDT = round(float(bin_content[11]['price']), 1)
    bin_LTCUSDT = round(float(bin_content[187]['price']), 3)
    bit_content = json.loads(bit_resp.content)
    bit_BTCUSDT = bit_content[0][1]
    bit_LTCUSDT = bit_content[1][1]
    print(bin_BTCUSDT, bit_BTCUSDT)

    db = create_engine(settings.DB_STRING)
    base = declarative_base()
    class Price(base):
        __tablename__ = 'prices'

        id = Column(Integer, primary_key=True)
        binance_BTCUSDT = Column(Float)
        diff_BTCUSDT = Column(Float)
        diff_BTCUSDT_percent = Column(Float)
        bitfinex_BTCUSDT = Column(Float)
        binance_LTCUSDT = Column(Float)
        diff_LTCUSDT = Column(Float)
        diff_LTCUSDT_percent = Column(Float)
        bitfinex_LTCUSDT = Column(Float)

        datetime = Column(DateTime)

    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)
    diff_BTCUSDT = round(bin_BTCUSDT - bit_BTCUSDT, 1)
    diff_LTCUSDT = round(bin_LTCUSDT - bit_LTCUSDT, 1)

    new_record = Price(binance_BTCUSDT=bin_BTCUSDT,
                       bitfinex_BTCUSDT=bit_BTCUSDT,
                       diff_BTCUSDT=diff_BTCUSDT,
                       diff_BTCUSDT_percent=abs(round(diff_BTCUSDT/bin_BTCUSDT * 100, 3)),
                       binance_LTCUSDT=bin_LTCUSDT,
                       bitfinex_LTCUSDT=bit_LTCUSDT,
                       diff_LTCUSDT=diff_LTCUSDT,
                       diff_LTCUSDT_percent=abs(round(diff_LTCUSDT / bin_LTCUSDT * 100, 3)),
                       datetime=datetime.datetime.now())
    session.add(new_record)
    session.commit()

    #time.sleep(5)
