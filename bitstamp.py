import json
import urllib2

class BitstampUSD:
    def getrate(self):
        data = json.load(urllib2.urlopen("https://www.bitstamp.net/api/ticker/"))
        rate = float(data["last"])
        print "bitstamp last="+str(rate)
        return rate
