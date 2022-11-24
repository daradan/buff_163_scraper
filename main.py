import json
import csv
import time
import random
import config
import requests


class BuffParser:
    def __init__(self):
        self.sale = False

    def start(self):
        for url in config.URLS:
            page = 1
            response = self.get_response(url, page)
            products = response['data']['items']
            while page < response['data']['total_page']:
                page += 1
                products.extend(self.get_response(url, page)['data']['items'])
            data_parsed = self.parse_products(products)
            self.export_to_csv(data_parsed)

    def get_response(self, url, page):
        while True:
            params = config.PARAMS
            if 'buying' not in url:
                self.sale = True
                params['use_suggestion'] = '0'
                params['trigger'] = 'undefined_trigger'
            else:
                self.sale = False
            params['page_num'] = page
            response = requests.get(url, params=params, cookies=config.COOKIES, headers=config.HEADERS)
            if response.status_code == 200:
                print(f'Parsing: {response.url}')
                return json.loads(response.text)
            time.sleep(random.randrange(5, 10))

    def parse_products(self, products: list):
        all_data = []
        for product in products:
            temp = []
            temp.append(product['market_hash_name'])
            if self.sale:
                temp.append(f"https://buff.163.com/goods/{product['id']}?from=market#tab=selling")
            else:
                temp.append(f"https://buff.163.com/goods/{product['id']}?from=market#tab=buying")
            all_data.append(temp)
            print(f'Parsed: {temp}')
        return all_data

    def export_to_csv(self, data_parsed):
        csv_header = ['name', 'url']
        name = 'purchase.csv'
        if self.sale:
            name = 'sale.csv'
        with open(name, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_header)
            writer.writerows(data_parsed)


if __name__ == '__main__':
    BuffParser().start()
