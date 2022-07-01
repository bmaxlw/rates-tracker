import datetime
import json
import requests
import time
import pyodbc as db
import pandas as pd
import matplotlib.pyplot as plt


def sql_server_connect(database='Stocks', server='DESKTOP-VU19ML5',
                       driver='{ODBC Driver 17 for SQL Server}',
                       trusted='yes'):
    cursor = db.connect(f'DRIVER={driver};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        f'Trusted_Connection={trusted};').cursor()
    return cursor


def track(tracking_time: int,
          stocks_to_track: str,
          sql):
    stocks_to_track = stocks_to_track.upper().replace(' ', '')
    counter = 0
    src_api = f'https://api.stockdata.org/v1/data/quote?symbols={stocks_to_track}' \
              f'&api_token=mmbGNbEv4MGTB3BQf8FjcXmVMt04bCKkx0w1Gsql'

    while counter < tracking_time:
        counter += 1
        json_data = json.loads(requests.get(src_api).text)
        for item in json_data['data']:
            ticker = item['ticker']
            name = item['name']
            currency = item['currency']
            price = float(item['price'])

            insert_statement = f"INSERT INTO tbl_StocksStreaming" \
                               f"(stock_ticker, stock_name, currency, stock_price) " \
                               f"VALUES('{ticker}', '{name}', '{currency}', '{price}');"

            sql.execute(insert_statement)
            sql.commit()
            print(f'Record #{counter} added at {datetime.datetime.now()}...')

        if counter < tracking_time:
            time.sleep(60)

    with open('log.txt', 'a') as file:
        file.write(f'{datetime.datetime.now()} | {counter} records committed\n')
        file.close()

    sql.close()







