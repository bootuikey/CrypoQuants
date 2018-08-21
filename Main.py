import ccxt
import time
import logging

#
def judgeifchance(threshold = 0.03,*orderbooks):
    maxBid = {'exchangeID':'','maxBid':0,'bidAllCounts':0}
    minAsk = {'exchangeID': '', 'minAsk': 0, 'askAllCounts': 0}
    for orderbook in orderbooks:
        if maxBid['maxBid'] == 0:
            maxBid['exchangeID'] = orderbook['exchangeID']
            maxBid['maxBid'] = orderbook['bids'][4][0]
        elif maxBid['maxBid'] < orderbook['bids'][4][0]:
            maxBid['exchangeID'] = orderbook['exchangeID']
            maxBid['maxBid'] = orderbook['bids'][4][0]
        else:
            pass

    orderbook = {}
    for orderbook in orderbooks:
            if (minAsk['minAsk'] == 0):
                minAsk['exchangeID'] = orderbook['exchangeID']
                minAsk['minAsk'] = orderbook['asks'][4][0]
            elif minAsk['minAsk'] > orderbook['asks'][4][0]:
                minAsk['exchangeID'] = orderbook['exchangeID']
                minAsk['minAsk'] = orderbook['asks'][4][0]
            else:
                pass
    chazhi = (maxBid['maxBid'] - minAsk['minAsk']) / minAsk['minAsk']
    logger.info("愿意出最大价钱的买家是 %s 价格为 %s，最便宜的价格就卖的卖家是 %s 价格为 %s，差价比例为：%s" %(maxBid['exchangeID'], maxBid['maxBid'], minAsk['exchangeID'], minAsk['minAsk'], chazhi))
    if chazhi >= threshold:
        logger.info("机会来啦！交易所 %s 和交易所 %s 出现了利差！" % (minAsk['exchangeID'], maxBid['exchangeID']))
        return True
    else:
        logger.info("机会没出现，等一下吧！！！！" )
        return False


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename='myapp.log', filemode='w')
logger = logging.getLogger(__name__)
coinEX = ccxt.coinex()
zb = ccxt.zb()
okex = ccxt.okex()
bibox = ccxt.bibox({
    'apiKey': 'e115769a73f5e0d26e646da98ced53d5282e2646',
    'secret': '7c0d8b2769d952ed8a5ff5c9fd45721f6fdee76f',
})
while True:
    try:
        orderbookCoinEx = coinEX.fetch_order_book("BTC/USDT", 5)
        orderbookZB = zb.fetch_order_book("BTC/USDT", 5)
        orderbookOkEx = okex.fetch_order_book("BTC/USDT", 5)
        orderbookBibox = bibox.fetch_order_book("BTC/USDT", 5)
        orderbookCoinEx['exchangeID'] = 'CoinEx'
        orderbookZB['exchangeID'] = 'ZB'
        orderbookOkEx['exchangeID'] = 'OkEx'
        orderbookBibox['exchangeID'] = 'BiBox'
        judgeifchance(0.03, orderbookCoinEx, orderbookZB, orderbookOkEx, orderbookBibox)
    except Exception as e:
        logger.error("出现错误：%s" % e)


