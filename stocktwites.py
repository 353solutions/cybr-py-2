import json
from urllib.request import urlopen, Request


def parse_reply(fp):
    # unique -> set
    reply = json.load(fp)

    symbols = {}  # symbol -> count
    for message in reply['messages']:
        for symbol in message['symbols']:
            ticker = symbol['symbol']
            # symbols.add(ticker)
            if ticker == 'AAPL':
                continue

            symbols[ticker] = symbols.get(ticker, 0) + 1
    return symbols


def related_stocks(symbol: str) -> dict[str, int]:
    """Return stocks mentioned next to symbol in stocktwits."""
    url = f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json'
    request = Request(
        url=url,
        headers={
            'User-Agent': 'curl',
        },
    )
    with urlopen(request) as fp:
        return parse_reply(fp)


# Testing

from pprint import pprint

# In order not to hit the API (rate limit)
# with open('data/AAPL.json') as fp:
#    pprint(parse_reply(fp))

pprint(related_stocks('AAPL'))
