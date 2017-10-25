#! /usr/bin/python
import urllib.request
response = urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
html = response.read()

lines =len(html.splitlines())
print(lines)
#print('(1) How many total requests were made in the time period represented in the log?')
#print('(2) How many requests were made on each day? per week? per month?')
#print('(3)What percentage of the requests were not successful (any 4xx status code)?')
#print('(4)What percentage of the requests were redirected elsewhere (any 3xx codes)?')
#print('(5)What was the most-requested file?')
#print('(6)What was the least-requested file?')
#print('(7) quit')
#answer = int(input('Choose a question to answer:'))
#print(html)



#def main () :
#		f = open('http_access_log', 'r')
#		count = 0
#		allLine =[]
#		by_weekday = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#		by_month = {}
#
#		for line in f:
#			count += 1
#			allLine.append(line) 
#			split_data = line.split() 
#			    try:
#				    str_date = line.split() [3] (1:].split(':')[0]
#			    except:
#				    pass
#				date = datetime.strptime( str_date, "%d/%b/%Y" ) 
#				by_weekday[date.weekday() ] += 1
#
#				if count > 2000:
#					print by_weekday
#					return 0
#
#	print ("1. How many total request were made in the time period represented in the log?") 
#	print len(allLine)
