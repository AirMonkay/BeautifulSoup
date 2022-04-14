import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1g0it2o1ut5eb800; INDEED_CSRF_TOKEN=D8wIgRyZqdOKHr5eEPTZrpD6cc599zyC; JSESSIONID=3511F5BE47F5AD62E10ECA3D3CB6FD10; PREF="TM=1649901920330:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1649901920355"; UD="LA=1649901920:CV=1649901920:TS=1649901920:SG=4247bfd008a1489adc73549b4cb81c01"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
