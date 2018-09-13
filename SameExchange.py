import ccxt
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename='sameExchange.log', filemode='w')
logger = logging.getLogger(__name__)
def sameExchangseAlg(exchange):
    ft_usdt_askOne = exchange.fetch_ticker("FT/USDT")['ask']
    ###################################################################
    ft_eth_bidOne = exchange.fetch_ticker("FT/ETH")['bid']
    eth_usdt_bidOne = exchange.fetch_ticker("ETH/USDT")['bid']
    ###################################################################
    ft_btc_bidOne = exchange.fetch_ticker("FT/BTC")['bid']
    btc_usdt_bidOne = exchange.fetch_ticker("BTC/USDT")['bid']
    if ft_usdt_askOne >= 1.01*ft_eth_bidOne*eth_usdt_bidOne:
        logger.info("eth机会来了 %s %s" %(ft_usdt_askOne, 1.01*ft_eth_bidOne*eth_usdt_bidOne))
        trade(exchange, 'ETH/USDT', eth_usdt_bidOne, ft_eth_bidOne, ft_usdt_askOne)
    else:
        logger.info("%s %s" %(ft_usdt_askOne, 1.01*ft_eth_bidOne*eth_usdt_bidOne))
    if ft_usdt_askOne >= 1.01*ft_btc_bidOne*btc_usdt_bidOne:
        logger.info("btc机会来了 %s %s" %(ft_usdt_askOne, 1.01*ft_btc_bidOne*btc_usdt_bidOne))
        trade(exchange, 'BTC/USDT', btc_usdt_bidOne, ft_btc_bidOne, ft_usdt_askOne)
    else:
        logger.info("%s %s" %(ft_usdt_askOne, 1.01*ft_btc_bidOne*btc_usdt_bidOne))
def trade(exchange,symbol, bidOne, bidTwo, askOne):
    # firstly buy btc or eth using usdt,
    freeAmount = exchange.fetch_balance()['USDT']['free']
    tradeAmount = min(min(bidOne, bidTwo, askOne), freeAmount)
    order = exchange.create_market_buy_order('BTC/USDT', tradeAmount)
    count = 0
    orderStatus = ''
    while count < 5:
        orderStatus = fcoin.fetch_order(order['id'], 'BTC/USDT')['status']
        if orderStatus != 'closed':
            time.sleep(50)
            count += 1
        else:
            break
    if count == 5:
        print('order can not be closed, exceed max retry count')


fcoin = ccxt.fcoin({'apiKey': '40', 'secret': 'b9'})
print(fcoin.fetch_balance()['USDT']['free'])
sameExchangseAlg(fcoin)


