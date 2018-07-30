import json

import requests


cross_instruments = ['ETHBTC', 'LTCBTC', 'NEOBTC', 'EOSETH', 'SNTETH', 'BNTETH', 'LRCBTC',
                     'LRCETH', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'KNCBTC', 'KNCETH',
                     'FUNBTC', 'FUNETH', 'NEOETH', 'XVGBTC', 'XVGETH', 'EOSBTC', 'SNTBTC',
                     'ETCBTC', 'ZECBTC', 'BNTBTC', 'BTGBTC', 'REQBTC', 'REQETH', 'TRXBTC',
                     'TRXETH', 'XRPBTC', 'RCNBTC', 'RCNETH', 'RDNBTC', 'RDNETH', 'XMRBTC',
                     'BATBTC', 'BATETH', 'XLMBTC', 'XLMETH', 'CNDBTC', 'CNDETH', 'TNBBTC',
                     'TNBETH', 'ELFBTC', 'ELFETH', 'EDOBTC', 'EDOETH', 'RLCBTC', 'RLCETH',
                     'POABTC', 'POAETH', 'ZILBTC', 'ZILETH', 'WPRBTC', 'WPRETH', 'GNTBTC',
                     'GNTETH', 'REPBTC', 'REPETH', 'AGIBTC', 'AGIETH', 'HOTBTC', 'HOTETH']


def get_cross_instruments():
    """
    function for getting a list of cross instruments
    """
    bin_resp = requests.get('https://api.binance.com/api/v3/ticker/price')
    bin_content = json.loads(bin_resp.content)
    symbols_list = [symb['symbol'] for symb in bin_content]
    symbols = 't' + ',t'.join(symbols_list)
    bit_resp = requests.get(f'https://api.bitfinex.com/v2/tickers?symbols={symbols}')
    bit_content = json.loads(bit_resp.content)
    cross_instruments = []
    for cont in bit_content:
        cross_instruments.append(cont[0].replace('t', ''))
    print(len(cross_instruments))
    print(cross_instruments)

get_cross_instruments()
