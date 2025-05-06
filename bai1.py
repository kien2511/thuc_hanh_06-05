import requests

page_id = '1062586164506537'
message = 'Hello from my script!'
access_token = 'EAAI2mS8ZC03oBO33aDK18jOu7YxSGTTvtwsE0vdohIQEDuHwGaKkasRVyKBOT2AjZCAcuVZCEAsdzU7YUIyvHaS1h4e8KDd2UbVwEDeXLZBWf31MA1syZAB0ZBAG37r91RhckrxhouYSD7DAfrs0Yb9aLGWlCFtxQpi9fJNh0kZBr8y3nVbD3dSn3h9IuKgxk998ZBoaK2VEDxEPJc2hNiMgECOh'

url = f'https://graph.facebook.com/{660042233852836}/feed'
payload = {
    'message': message,
    'access_token': access_token
}

r = requests.post(url, data=payload)
print(r.status_code)
print(r.text)
