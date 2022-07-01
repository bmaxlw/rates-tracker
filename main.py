import datetime
import json
import requests
import time
import pyodbc as db
import stocks

sql = stocks.sql_server_connect()

stocks.track(1, 'CRM', sql=sql)
