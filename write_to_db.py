import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

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
