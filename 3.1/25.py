#-----------------------------------------------------------------------
# 修改stockquote.py,从https://15tianqi.cn/taiyuan15tian/获取天气，输入城市名，得到当日天气
# weather.py
#-----------------------------------------------------------------------

import sys
import stdio
from instream import InStream

#-----------------------------------------------------------------------

# Return the raw HTML from the website http://finance.yahoo.com

def _readHTML(city):
    WEBSITE = 'https://15tianqi.cn/'
    page = InStream(WEBSITE + city+'15tian')
    html = page.readAll()
    return html

#-----------------------------------------------------------------------

# Extract the current stock price of the stock whose symbol is 
# city from the HTML and return it.
'''
<div class="tianqi15"><ul>  <li class="bold"><p>太原今天天气(02-24)</p> <span><em class="tqclas"></em><em class="tq阴"></em></span>  <b><font class="gray">白天：</font>-3</b><b><font class="gray">夜间：</font>-3</b> <i><font class="blue">0℃</font>～<font class="red">0℃</font><br> </i></li>   <li class="bold"><p>太原明天天气(02-25)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-17℃</font>～<font class="red">3℃</font><br>西风 &lt;3级</i></li>   <li class="bold"><p>太原后天天气(02-26)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-16℃</font>～<font class="red">2℃</font><br>西风 &lt;3级</i></li>   <li> <p>02月27日(<font class="blue">星期六</font>)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-15℃</font>～<font class="red">3℃</font><br>西风 &lt;3级</i></li>   <li> <p>02月28日(<font class="red">星期日</font>)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-19℃</font>～<font class="red">3℃</font><br>西南风 &lt;3级</i></li>   <li> <p>03月01日(星期一)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-19℃</font>～<font class="red">0℃</font><br>南风 &lt;3级</i></li>   <li class="lastd"> <p>03月02日(星期二)</p> <span><em class="tq00 one"></em></span> <b><font class="gray">白天：</font>晴</b><b><font class="gray">夜间：</font>晴</b> <i><font class="blue">-18℃</font>～<font class="red">-1℃</font><br>西南风 &lt;3级</i></li></ul></div>
'''
def priceOf(city):
    html  = _readHTML(city)
    l = []
    trade = html.find('tianqi15', 0)
    #pbeg  = html.find('<p>', trade)
    beg   = html.find('<p>', trade)
    end   = html.find('</p>', beg)
    price = html[beg+3:end]
    l.append(price)
    temp1 = html.find('blue">', end)
    lowtemp = html[temp1+6:temp1+9]
    l.append(lowtemp)
    temp2 = html.find('red">',temp1)
    hightemp = html[temp2+5:temp2+8]
    l.append(hightemp)
    #price = price.replace(',', '')
    return l

#-----------------------------------------------------------------------

# Accept string city as a command-line argument. Write to
# standard output the current stock price for city, as reported
# by the website http://finance.yahoo.com/.

def main():
    lOfStockSymbol = sys.argv[1:]
    for stock in lOfStockSymbol:
        price = priceOf(stock)
        #stdio.writef(price)
        print(price)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python stockquote.py goog
# 540.48

# python stockquote.py adbe
# 83.55

