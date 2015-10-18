import subprocess, json, urllib2

if __name__ == '__main__': 
	
	channels=['eternalenvyy', 'nl_kripp',
		  'sing_sing', 'arteezy']

	switch=False
	i=1
	print('')

	for channel in channels:
		response = urllib2.urlopen('https://api.twitch.tv/kraken/streams/'+channel)
		data = json.load(response)

		if not data['stream']:
			print(str(i) + ' ' + channel + ' OFFLINE')

		else:
			print(str(i) + ' ' + channel + ' ONLINE')
			switch=True
					
		i+=1

	print('')

	if switch:	
		auswahl = int(input('Auswahl: '))
		subprocess.call(["livestreamer",'twitch.tv/'+channels[auswahl-1], "high"])


