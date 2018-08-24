import ccxt
import time
import logging

#
def judgeifchance(threshold = 0.03, crypoName="BTC", *orderbooks):
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
    logger.info("愿意出最大价钱买%s的买家是%s价格为%s，最便宜的价格就卖%s的卖家是%s价格为%s，差价比例为:%.2f%%" % (crypoName, maxBid['exchangeID'], maxBid['maxBid'], crypoName, minAsk['exchangeID'], minAsk['minAsk'], chazhi*100))
    if chazhi >= threshold:
        logger.info("机会来啦！交易所%s和交易所%s的%s出现了%.2f%%的利差！" % (minAsk['exchangeID'], maxBid['exchangeID'], crypoName, chazhi*100))
        return True
    else:
        logger.info("%s机会没出现，等一下吧！！！！" % crypoName)
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
        orderbookCoinEx_BCH = coinEX.fetch_order_book("BCH/USDT", 5)
        orderbookZB_BCH = zb.fetch_order_book("BCH/USDT", 5)
        orderbookOkEx_BCH = okex.fetch_order_book("BCH/USDT", 5)
        orderbookBibox_BCH = bibox.fetch_order_book("BCH/USDT", 5)
        orderbookCoinEx_BCH['exchangeID'] = 'CoinEx'
        orderbookZB_BCH['exchangeID'] = 'ZB'
        orderbookOkEx_BCH['exchangeID'] = 'OkEx'
        orderbookBibox_BCH['exchangeID'] = 'BiBox'

        orderbookCoinEx_ETC = coinEX.fetch_order_book("ETC/USDT", 5)
        orderbookZB_ETC = zb.fetch_order_book("ETC/USDT", 5)
        orderbookOkEx_ETC = okex.fetch_order_book("ETC/USDT", 5)
        orderbookBibox_ETC = bibox.fetch_order_book("ETC/USDT", 5)
        orderbookCoinEx_ETC['exchangeID'] = 'CoinEx'
        orderbookZB_ETC['exchangeID'] = 'ZB'
        orderbookOkEx_ETC['exchangeID'] = 'OkEx'
        orderbookBibox_ETC['exchangeID'] = 'BiBox'

        orderbookCoinEx_EOS = coinEX.fetch_order_book("EOS/USDT", 5)
        orderbookZB_EOS = zb.fetch_order_book("EOS/USDT", 5)
        orderbookOkEx_EOS = okex.fetch_order_book("EOS/USDT", 5)
        orderbookBibox_EOS = bibox.fetch_order_book("EOS/USDT", 5)
        orderbookCoinEx_EOS['exchangeID'] = 'CoinEx'
        orderbookZB_EOS['exchangeID'] = 'ZB'
        orderbookOkEx_EOS['exchangeID'] = 'OkEx'
        orderbookBibox_EOS['exchangeID'] = 'BiBox'

        judgeifchance(0.03, "BCH", orderbookCoinEx_BCH, orderbookZB_BCH, orderbookOkEx_BCH, orderbookBibox_BCH)
        judgeifchance(0.03, "ETC", orderbookCoinEx_ETC, orderbookZB_ETC, orderbookOkEx_ETC, orderbookBibox_ETC)
        judgeifchance(0.03, "EOS", orderbookCoinEx_EOS, orderbookZB_EOS, orderbookOkEx_EOS, orderbookBibox_EOS)
    except Exception as e:
        logger.error("出现错误：%s" % e)


