from riotwatcher import RiotWatcher
import  pymongo
import time

host='localhost'
port= 27017
watcher = RiotWatcher('YOU-API-KEY')
my_region = 'na1'
client=pymongo.MongoClient(host,port)


db= client['LOL']
sheet0=db['userid_base']
sheet1=db['userid_V1']

j=0

me = watcher.summoner.by_name(my_region, 'chizzoyang')


for item in sheet0.find():
     id=item['id']
     if item['flage']==0:
         try:
             time.sleep(0.5)
             playerlist = watcher.league.by_summoner(my_region, summoner_id=id)[0]
             for player in playerlist['entries']:
                 playerinfo = player
                 playerinfo['tier'] = playerlist['tier']
                 playerinfo['areaname'] = playerlist['name']
                 playerinfo['flag']=0
                 sheet.insert_one(playerinfo)
             j+=1
             print('{}/{}'.format(j,lens))
             sheet0.update(
                      {'_id':item['_id']},
                     {'$set':{'flage':1}}
                  )
         except:
             continue









