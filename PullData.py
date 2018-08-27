import ccxt
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename='myapp.log', filemode='w')
logger = logging.getLogger(__name__)
huobipro = ccxt.huobipro()
binance = ccxt.binance()
out_hbproETC = open('HuobiPro_Ticker_ETC.CSV', 'a', newline='')
csv_write_hbproETC = csv.writer(out_hbproETC, dialect='excel')
out_hbproEOS = open('HuobiPro_Ticker_EOS.CSV', 'a', newline='')
csv_write_hbproEOS = csv.writer(out_hbproEOS, dialect='excel')
out_hbproBCH = open('HuobiPro_Ticker_BCH.CSV', 'a', newline='')
csv_write_hbproBCH = csv.writer(out_hbproBCH, dialect='excel')

while True:
    try:
        tickerHuobiPro_ETC = huobipro.fetch_ticker("ETC/USDT")
        line = [tickerHuobiPro_ETC['symbol'], tickerHuobiPro_ETC['datetime'], tickerHuobiPro_ETC['bid'],
                           tickerHuobiPro_ETC['bidVolume'], tickerHuobiPro_ETC['ask'], tickerHuobiPro_ETC['askVolume'],
                           tickerHuobiPro_ETC['high'], tickerHuobiPro_ETC['low'], tickerHuobiPro_ETC['open'],
                           tickerHuobiPro_ETC['close']]
        csv_write_hbproETC.writerow(line)
        ###################################################################################################
        tickerHuobiPro_EOS = huobipro.fetch_ticker("EOS/USDT")
        line = [tickerHuobiPro_EOS['symbol'], tickerHuobiPro_EOS['datetime'], tickerHuobiPro_EOS['bid'],
                tickerHuobiPro_EOS['bidVolume'], tickerHuobiPro_EOS['ask'], tickerHuobiPro_EOS['askVolume'],
                tickerHuobiPro_EOS['high'], tickerHuobiPro_EOS['low'], tickerHuobiPro_EOS['open'],
                tickerHuobiPro_EOS['close']]
        csv_write_hbproEOS.writerow(line)
        ##################################################################################################
        tickerHuobiPro_BCH = huobipro.fetch_ticker("BCH/USDT")
        line = [tickerHuobiPro_BCH['symbol'], tickerHuobiPro_BCH['datetime'], tickerHuobiPro_BCH['bid'],
                tickerHuobiPro_BCH['bidVolume'], tickerHuobiPro_BCH['ask'], tickerHuobiPro_BCH['askVolume'],
                tickerHuobiPro_BCH['high'], tickerHuobiPro_BCH['low'], tickerHuobiPro_BCH['open'],
                tickerHuobiPro_BCH['close']]
        csv_write_hbproBCH.writerow(line)
    except Exception as e:
        logger.error("出现错误：%s" % e)

# tickerbinance_ETC = binance.fetch_ticker("ETC/USDT")
# tickerbinance_EOS = binance.fetch_ticker("EOS/USDT")
# tickerbinance_BCH = binance.fetch_ticker("BCH/USDT")
