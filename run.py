import time
import pandas as pd
import gspread
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

import tools
from soccer import Soccer


if __name__ == "__main__":
    dt = datetime.today()
    end = dt + timedelta(days=2)

    print("Test Execution Started")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    driver = [webdriver.Remote(command_executor='http://selenium_ui:4444/wd/hub', options=options) for i in range(5)]

    matches_url_list = tools.get_matches(end, driver)
    soccer_list = [Soccer(i) for i in matches_url_list]
    [soccer_list[i].run(driver[i % 5]) for i in range(len(soccer_list))]
    soccer_stats_full = pd.concat([tools.treat_stats(i) for i in soccer_list])

    gc = gspread.service_account(filename='../Soccer.json')
    sh = gc.open("Soccer")
    worksheet = sh.worksheet('Soccer')

    df_worksheet = pd.DataFrame(worksheet.get_all_records())
    df = update_table(df_old=df_worksheet, df_new=soccer_stats_full)

    worksheet.update([df.columns.values.tolist()] + df.astype(str).values.tolist())

    print(df_worksheet.shape)
    print(soccer_stats_full.shape)
    print(df.shape)
