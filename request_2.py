import json
import requests

x = requests.get('http://saral.navgurukul.org/api/courses')
data=x.json()
def courses():
    i=0
    for v in data["availableCourses"]:
        print(i+1,v["name"],v["id"])
        i+=1
courses()