import requests
import json

api_url_base ='https://od-api.oxforddictionaries.com/api/v1'
print(api_url_base)
headers={
  "Accept": "application/json",
  "app_id": "**********",
  "api_key":'***************************'
   }
n=input('enter the word that you wnat to know the meaning')
s='{0}/entries/en/'+n
print(s)
api_url = s.format(api_url_base)
print(api_url)
response=requests.get(api_url,headers=headers)
if response.status_code ==200:
   data=json.loads(response.content.decode('utf-8'))
   #print(json.dumps(data,indent=4))
   #print('now starts from here\n\n\n\n')
   #print(json.dumps(data['results'][0],indent=4))
   #print('second para starts from here')
   print(json.dumps(data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'],indent=4))
#['senses'][0]['subsenses'][0]['definitions'][0]
else:
   print('cant')

