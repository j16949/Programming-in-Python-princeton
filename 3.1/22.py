#-----------------------------------------------------------------------
# 修改stockquote.py，yahoo金融已换界面，改为https://finance.yahoo.com/quote/adbe
# stockquote.py
#-----------------------------------------------------------------------

import sys
import stdio
from instream import InStream

#-----------------------------------------------------------------------

# Return the raw HTML from the website http://finance.yahoo.com

def _readHTML(stockSymbol):
    WEBSITE = 'https://finance.yahoo.com/quote/'
    page = InStream(WEBSITE + stockSymbol)
    html = page.readAll()
    return html

#-----------------------------------------------------------------------

# Extract the current stock price of the stock whose symbol is 
# stockSymbol from the HTML and return it.

def priceOf(stockSymbol):
    html  = _readHTML(stockSymbol)
    trade = html.find('PREV_CLOSE-value', 0)
    pbeg  = html.find('>', trade)
    beg   = html.find('>', pbeg+1)
    end   = html.find('</span>', beg)
    price = html[beg+1:end]
    price = price.replace(',', '')
    return float(price)

#-----------------------------------------------------------------------

# Accept string stockSymbol as a command-line argument. Write to
# standard output the current stock price for stockSymbol, as reported
# by the website http://finance.yahoo.com/.

def main():
    lOfStockSymbol = sys.argv[1:]
    for stock in lOfStockSymbol:
        price = priceOf(stock)
        stdio.writef('%.2f\n', price)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python stockquote.py goog
# 540.48

# python stockquote.py adbe
# 83.55

