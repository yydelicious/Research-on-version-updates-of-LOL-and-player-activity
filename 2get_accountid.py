from riotwatcher import RiotWatcher
import  pymongo
import time
from requests import HTTPError

host='localhost'
port= 27017
watcher = RiotWatcher('YOU-API-KEY')
my_region = 'na1'
client=pymongo.MongoClient(host,port)


db= client['db']
sheet0=db['userid_v1']
sheet=db['userid_v2']

j=0

for item in sheet0.find():
    id=item['id']
    if item['flag']==0:
        try:
            time.sleep(0.1)
            accountinfo = watcher.summoner.by_id(my_region, id)['accountId']
            dic=item
            dic['accountId']=accountinfo
            sheet.insert_one(dic)
            sheet0.update(
                     {'_id':item['_id']},
                    {'$set':{'flag':1}}
                 )
            j+=1
            print(j)
        except HTTPError as err:
            if err.response.status_code == 429:
                print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                print('Summoner with that ridiculous name not found.')
            else:
                print('wrong')
            continue




