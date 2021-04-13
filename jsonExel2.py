import requests
"""In this method we are using json_exel_converter module which will convert json data directly to exel file
To install pip install json-excel-converter"""
from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer

results = requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog')
r = results.status_code
# t = results.text

data = results.json()
conv = Converter()
conv.convert(data, Writer(file='testdata.xlsx'))
