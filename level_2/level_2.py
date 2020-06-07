#!/usr/bin/python3
import requests


header = {"Content-Type": "application/X-www-form-urlencoded",
          "Refer": "http://158.69.76.135/level2.php",
          "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}

URL = "http://158.69.76.135/level2.php"
payload = {"idi": "1406", "holdthedoor": "Submit+Query", "key": ""}
cookies = {"HoldTheDoor": ""}

req = requests.get(URL)
while "1406   </td>\n   <td>\n1024" not in req.text:
    cookies["holdthedoor"] = req.cookies["HoldTheDoor"]
    req = requests.put(URL, data=payload, headers=header, cookies=cookies)
    if req.status_code == 200:
        print("The request has succeeded.")
    else:
        print("The request has failed.")
        break
