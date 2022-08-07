import json
import requests

x = requests.get('http://saral.navgurukul.org/api/courses')
with open("requst_part1.json","w") as part:
    dic=json.loads(x.text)
    json.dump(dic,part,indent=4)
print("save")




