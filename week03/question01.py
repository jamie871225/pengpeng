import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)
spdata=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for spot in spdata:
        title=spot["stitle"]
        longitude=spot["longitude"]
        latitude=spot["latitude"]
        images=[]
        images.append(spot["file"])
        img=images[0].split("http://")
        file.write(title+","+longitude+","+latitude+","+"http://"+img[1]+"\n")