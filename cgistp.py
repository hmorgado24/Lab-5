from urllib.request import urlopen
from urllib.parse import urlencode

import json
import cgi
import cgitb

cgitb.enable()

data = cgi.Fieldstorage()

angle = data.getvalue('angleinput')
zangle = data.getvalue('zangle')
s1 = data.getvalue('slider1')

stats = {'angleinput':angle, 'zangle':zangle, 'slider1':s1}
with open('jsonstor.txt', 'w') as f:
  json.dump(stats, f)


print('Content-type: text/html\n\n')
print('<html>')
print('<meta http-equiv="refresh" content="30">')
print('<form action="/cgi-bin/cgistp.py" method="POST">')
print('<input type="range" name="slider1" min ="0" max="360" value ="0"> <br>')
print('<input type="submit" name="angleinput" value="Angle Input"> <br> <br>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1556346/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs+Time&type=line&xaxis=Time&yaxis=Motor+Angle"></iframe>')
print(' <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1556346/widgets/375975"></iframe>')
print('<input type="submit" name="zangle" value="Zero Angle">')
print('</form>')
print('</html>')
