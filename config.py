import requests

URL_PURCHASE = 'https://buff.163.com/api/market/goods/buying'
URL_SALE = 'https://buff.163.com/api/market/goods'
URLS = [URL_SALE, URL_PURCHASE]

COOKIES = {
    'Device-Id': 'XXX',
    'Locale-Supported': 'en',
    'game': 'csgo',
    'AQ_HD': '1',
    'YD_SC_SID': 'XXX',
    'NETS_utid': 'XXX',
    'NTES_YD_SESS': 'XXX',
    'S_INFO': 'XXX',
    'P_INFO': 'XXX',
    'remember_me': 'XXX',
    'session': 'XXX',
    'csrf_token': 'XXX',
}

HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://buff.163.com/market/csgo',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0 Safari/537.36 '
                  'OPR/93.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Opera";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

PARAMS = {
    'game': 'csgo',
    'page_num': '1',
}


if __name__ == '__main__':
    response = requests.get(URL_PURCHASE, params=PARAMS, cookies=COOKIES, headers=HEADERS)
    print(response.text)
