import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contatos_df = pd.read_excel('Contatos.xlsx')
print(contatos_df)