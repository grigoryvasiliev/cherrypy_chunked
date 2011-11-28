import urllib2
import simplejson

url = "http://127.0.0.1:8080/TestStreaming1"
resp = urllib2.urlopen(url)

res = resp.readline()

while res:
	print len( simplejson.loads( res ) )
	res = resp.readline()
	
