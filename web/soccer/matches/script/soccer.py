from selenium.webdriver.common.by import By
import pandas as pd


class Soccer:
    def __init__(self, _url):
        self.url = _url
        self.id = _url.split('/')[-1]
        self.date = None
        self.history = None
        self.stats_table = None
        self.home_history = None
        self.away_history = None
            
    
    def change_url(self, _driver):
        _driver.get(self.url)
        
    
    def get_date(self, _driver):    
        date_html = _driver.find_elements(By.XPATH, "//span[@class='analysisRaceTime']")
        self.date = date_text = date_html[0].text
    
    
    def get_history(self, _driver):
        history_table = _driver.find_elements(By.XPATH, "//div[@class='small-12 columns' and .//table]")[-1]
        df = pd.read_html(history_table.get_attribute('outerHTML'))[0]
        df_dropped = df.drop(df.columns[[-4, -1]], axis=1)
        self.history = df_dropped
        
        
    def get_stats_table(self, _driver):
        history_list = _driver.find_elements(By.XPATH, "//div[@id='history_table']")
        if history_list:
            history_table = history_list[0]
            try:
                df = pd.read_html(history_table.get_attribute('outerHTML'))[0]
                self.stats_table = df
            except:
                self.stats_table = None
            
        
    def get_home_history(self, _driver):
        history_list = _driver.find_elements(By.XPATH, "//div[@id='history1']")
        if history_list:
            history_table = history_list[0]
            try:
                df = pd.read_html(history_table.get_attribute('outerHTML'))[0]
                df_dropped = df.drop(df.columns[[-5, -1]], axis=1)
                self.home_history = df_dropped
            except:
                self.home_history = None
        
        
    def get_away_history(self, _driver):
        history_list = _driver.find_elements(By.XPATH, "//div[@id='history2']")
        if history_list:
            history_table = history_list[0]
            try:
                df = pd.read_html(history_table.get_attribute('outerHTML'))[0]
                df_dropped = df.drop(df.columns[[-5, -1]], axis=1)
                self.away_history = df_dropped
            except:
                self.away_history =  None
    
    
    def run(self, _driver):
        try:
            self.change_url(_driver)
            self.get_date(_driver)
            self.get_history(_driver)
            self.get_stats_table(_driver)
            self.get_home_history(_driver)
            self.get_away_history(_driver)
        except:
            print(self.url)