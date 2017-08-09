from riotwatcher import RiotWatcher
import  pymongo
import time
from requests import HTTPError


keys=['YOU-API-KEY']

host='localhost'
port= 27017

my_region = 'na1'
client=pymongo.MongoClient(host,port)


db= client['db']
sheet0=db['userid_v2']
sheet=db['userinfo_v1']


j=0

watcher = RiotWatcher(keys[0])
for item in sheet0.find():
    accountId=item['accountId']
    if item['flag']==0 and item['task']==0:
        try:
            time.sleep(0.1)
            matchlist = watcher.match.matchlist_by_account(my_region, account_id=accountId, season=9)['matches']
            dic=item
            dic['matchlist']=matchlist
            sheet.insert_one(dic)
            sheet0.update(
                     {'_id':item['_id']},
                    {'$set':{'flag':1}}
                 )
            j+=1
            print(j)
        except:
            print('wrong')
            continue


