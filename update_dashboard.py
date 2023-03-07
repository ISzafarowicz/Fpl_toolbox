import pandas as pd
from Scraping_Module.scraping_fpl_api import FplScraper

scraper = FplScraper()
curr_gw = scraper.load_gameweek()
curr_gw.to_excel('Dashboard_Data/current_gameweek_data.xlsx', index=False)
print('Current Gameweek Data Updated')