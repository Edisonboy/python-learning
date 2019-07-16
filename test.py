import time
import requests

url = 'https://merchant-api-pre.imlaidian.com/merchant-api/es/add/%s/wOFR1UeZk4mTd7PHR5PY'

filename = 'C:\\Users\\ediso\\Desktop\\long_text_2019-06-11-21-13-13.txt'
with open(filename) as file_object:
    contents = file_object.read()
    array = contents.split(',')
    print(len(array))
    for a in array:
        print("==")
        requestUrl = url % a.strip()
        response = requests.get(requestUrl)
        print(requestUrl)
        print(response.json())
        time.sleep(0.5)
