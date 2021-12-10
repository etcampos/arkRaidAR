import requests
import json


class XboxServer:
    def __init__(self, ip, mapName, numPlayers, lastUpdated, name, cluster, isPVE):
        self.ip = ip
        self.mapName = mapName
        self.numPlayers = numPlayers
        self.lastUpdated = lastUpdated
        self.name = name
        self.cluster = cluster
        self.isPVE = isPVE

    def __str__(self):
        ipAddr = str(self.ip)
        n = str(self.numPlayers)
        ##TODO: Logic for milisecond conversion
        result = "IP: " + ipAddr + "\nMap Name: " + self.mapName + "\nNumber Players: " + n + "\nServer Name: " + self.name
        return result




##Create json file for servers
f = open("xboxServers.json", "w")
response = requests.get("http://arkdedicated.com/xbox/cache/officialserverlist.json")
f.write(response.text)
f.close()

##read file
f = open("xboxServers.json", )
data = json.load(f)
numOfArray = 1
lst = []

for i in data:
    s = XboxServer(i["IP"], i["MapName"], i["NumPlayers"], i["LastUpdated"], i["Name"], i["ClusterId"], i["SessionIsPve"])
    lst.append(s)
    #print(s)
f.close()

count = 0;
for j in lst:
    if j.mapName == "Aberration_P" and j.isPVE == 0:
        nlst = j.name.split("-")
        region = nlst[0]
        if region == "NA":
            if len(nlst) == 4:
                consoleType = nlst[2]
                serverNum = nlst[3]
                #count = count + 1
                if serverNum == "Aberration773":
                    print("==========================")
                    print("IP:", j.ip, "\nNum Players:", j.numPlayers, "\nConsole:", consoleType, "\nServer:", serverNum)


print("\n\nServer Count:", count)