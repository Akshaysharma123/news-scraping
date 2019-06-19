import mysql.connector
import requests
from bs4 import BeautifulSoup


my_database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'sea',
)
my_cursor = my_database.cursor()
