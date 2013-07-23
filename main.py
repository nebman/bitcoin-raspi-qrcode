import sys
import time
import os

import bitstamp
import fbgraphics

try:
    exchange = bitstamp.BitstampUSD()
    fb = fbgraphics.FbGraphics()
except:
    print "error while init."

try:
    rate = exchange.getrate()
    topay = round(2 / rate, 8)
except Exception, e:
    fb.renderError(e)
    print "error: ", e


fb.renderQR(topay, "test")

time.sleep(300)

