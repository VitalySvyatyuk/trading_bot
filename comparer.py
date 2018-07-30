import json

import requests

CROSS_INSTRUMENTS = ['ETHBTC', 'LTCBTC', 'NEOBTC', 'EOSETH', 'SNTETH', 'LRCBTC',
                     'LRCETH', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'KNCBTC', 'KNCETH',
                     'FUNBTC', 'FUNETH', 'NEOETH', 'XVGBTC', 'XVGETH', 'EOSBTC', 'SNTBTC',
                     'ETCBTC', 'ZECBTC', 'BNTBTC', 'BTGBTC', 'REQBTC', 'REQETH', 'TRXBTC',
                     'TRXETH', 'XRPBTC', 'RCNBTC', 'RCNETH', 'RDNBTC', 'RDNETH', 'XMRBTC',
                     'BATBTC', 'BATETH', 'XLMBTC', 'XLMETH', 'CNDBTC', 'CNDETH', 'TNBBTC',
                     'TNBETH', 'ELFBTC', 'ELFETH', 'EDOBTC', 'EDOETH', 'RLCBTC', 'RLCETH',
                     'POABTC', 'POAETH', 'ZILBTC', 'ZILETH', 'WPRBTC', 'WPRETH', 'GNTBTC',
                     'GNTETH', 'REPBTC', 'REPETH', 'AGIBTC', 'AGIETH']

INTERESTING = [
    'LRCETH',  # 1   %13.00
    'KNCETH',  # 9   %2.30, 1.60
    'FUNBTC',  # 1   %1.00, 0.65
    'FUNETH',  # 5   %1.80, 1.28
    'RCNETH',  # 1   %11.41
    'BATBTC',  # 2   %0.31
    'BATETH',  # 16  %0.58
    'CNDETH',  # 1   %5.90, 7.14
    'EDOETH',  # 2   %0.95
    'RLCETH',  # 2   %5.05
    'GNTBTC',  # 3   %1.00

    'ZRXBTC',  # 6   %0.49
    'ZRXETH',  # 28  %0.58, 0.37
    'XVGBTC',  # 2   %0.67
    'XVGETH',  # 26  %0.97, 0.85
    'BATBTC',  # 2   %0.73, 0.32
    'BATETH',  # 16  %0.64, 0.58
    'XLMBTC',  # 3   %0.55, 0.24
    'XLMETH',  # 5   %0.60, 0.56
    'ELFBTC',  # 2   %0.26
    'ELFETH',  # 286 %0.67, 0.57
    'GNTBTC',  # 3   %0.78, 1.00
    'GNTETH',  # 144 %0.51
    'REPETH',  # 2   %1.82, 1.28
]

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


# get_cross_instruments()
