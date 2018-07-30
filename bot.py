import json
import time
from decimal import Decimal

import requests

from comparer import CROSS_INSTRUMENTS, INTERESTING


while True:
    bin_resp = requests.get('https://api.binance.com/api/v3/ticker/price')
    symbols = 't' + ',t'.join(CROSS_INSTRUMENTS)
    bit_resp = requests.get(f'https://api.bitfinex.com/v2/tickers?symbols={symbols}')
    if bin_resp.status_code != 200 or bit_resp.status_code != 200:
        print(bin_resp.status_code, bit_resp.status_code)
        raise ValueError
    bin_content = json.loads(bin_resp.content)
    bit_content = json.loads(bit_resp.content)

    print_list = []
    for instrument in INTERESTING:
        for bin in bin_content:
            if bin['symbol'] == instrument:
                bin_price = round(Decimal(bin['price']), 8)
                break
        for bit in bit_content:
            if bit[0] == 't' + instrument:
                bit_price = round(Decimal(bit[1]), 8)
                break
        diff = format(bin_price - bit_price, '.15f')
        diff_percent = abs(round(Decimal(diff)/bin_price * 100, 3))
        print_list.append(diff_percent)
    print(print_list)

    time.sleep(2)
