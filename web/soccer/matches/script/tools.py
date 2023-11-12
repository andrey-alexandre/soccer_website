from selenium.webdriver.common.by import By
import pandas as pd
import time

from matches.script.soccer import Soccer


def treat_stats(soccer_obj: Soccer):
    if soccer_obj.stats_table is not None:
        df = soccer_obj.stats_table.copy()

        df.loc[:,'GameId'] = soccer_obj.id
        df.loc[:, 'url'] = soccer_obj.url
        df.loc[:, 'Data'] = soccer_obj.date
        df.loc[:, 'JogosCasa'] = soccer_obj.home_history.shape[0] if soccer_obj.home_history is not None else 0
        df.loc[:, 'JogosFora'] = soccer_obj.away_history.shape[0] if soccer_obj.away_history is not None else 0
        df.loc[:, 'Data'] = pd.to_datetime(df.loc[:, 'Data'])-pd.Timedelta(hours=3)

        df_renamed = df.rename({'Average (Half / Full)': 'NomeTime', 'Average (Half / Full).1': 'TipoMetrica'}, axis=1).copy()
        df_renamed_filtered = df_renamed.query("NomeTime != 'Comparison'").copy()

        df_renamed_filtered.loc[:,'NomeTime'] = df_renamed_filtered.loc[:,'NomeTime'].str.replace(r'Last [0-9]', '-', regex=True)
        splitted_team = df_renamed_filtered.loc[:,'NomeTime'].str.split(' - ', expand=True)
        df_renamed_filtered.loc[:,'Time'] = splitted_team.loc[:, 0]
        df_renamed_filtered.loc[:,'Local'] = splitted_team.loc[:, 1]

        splitted_goal = df_renamed_filtered.loc[:,'Goal'].str.split('/', expand=True)
        df_renamed_filtered.loc[:,'Goal_T1'] = splitted_goal.loc[:, 0]
        df_renamed_filtered.loc[:,'Goal_T2'] = splitted_goal.loc[:, 1]

        splitted_goal_over = df_renamed_filtered.loc[:,'Goal Over'].str.replace('%', '').str.split('/', expand=True)
        df_renamed_filtered.loc[:,'GoalOver_T1'] = splitted_goal_over.loc[:, 0]
        df_renamed_filtered.loc[:,'GoalOver_T2'] = splitted_goal_over.loc[:, 1]  

        splitted_corner = df_renamed_filtered.loc[:,'Corner'].str.split('/', expand=True)
        df_renamed_filtered.loc[:,'Corner_T1'] = splitted_corner.loc[:, 0]
        df_renamed_filtered.loc[:,'Corner_T2'] = splitted_corner.loc[:, 1]

        splitted_corner_over = df_renamed_filtered.loc[:,'Corner Over'].str.replace('%', '').str.split('/', expand=True)
        df_renamed_filtered.loc[:,'CornerOver_T1'] = splitted_corner_over.loc[:, 0]
        df_renamed_filtered.loc[:,'CornerOver_T2'] = splitted_corner_over.loc[:, 1]

        splitted_win = df_renamed_filtered.loc[:,'Win'].str.replace('%', '').str.replace('-', '-/-').str.split('/', expand=True)
        df_renamed_filtered.loc[:,'Win_T1'] = splitted_win.loc[:, 0]
        df_renamed_filtered.loc[:,'Win_T2'] = splitted_win.loc[:, 1]

        df_final = df_renamed_filtered.loc[:,['Data', 'GameId', 'Time', 'Local', 'TipoMetrica', 'JogosCasa', 'JogosFora',
                                              'Goal_T1', 'Goal_T2', 'GoalOver_T1', 'GoalOver_T2', 'Corner_T1', 'Corner_T2', 
                                              'CornerOver_T1', 'CornerOver_T2', 'Win_T1', 'Win_T2', 'url']].copy()

        return df_final
    

def get_matches(limit_date, driver_):
    filtered_df = pd.DataFrame()
    matches_urls=[]
    i = 1
    while filtered_df.shape[0] == 0:
        driver_.get(f'https://www.scorebing.com/fixtures/p.{i}')
        time.sleep(2)

        table_html = driver_.find_elements(By.XPATH, "//table[@class='live-list-table diary-table']")
        df_page = pd.read_html(table_html[0].get_attribute('outerHTML'))[0]
        df_page = df_page.rename({'Unnamed: 1': 'Kick-off Time'}, axis=1)
        df_page['Time'] = pd.to_datetime(df_page['Kick-off Time'], format='%y/%m/%d %H:%M')
        filtered_df = df_page.query(f'Time > @limit_date')

        matches_elements = driver_.find_elements(By.XPATH, "//a[.//img[@alt='Analysis']]")
        matches_urls += [i.get_attribute('href').replace('/match/', '/match_history/') for i in matches_elements]
        i += 1
    
    return matches_urls


def update_table(df_old, df_new):
    df_new = df_new.astype({'GameId': 'int'})
    df_old = df_old.astype({'GameId': 'int'})
    
    df_ids = df_new.merge(df_old, on='GameId', how='outer', indicator=True)[['GameId', '_merge']]
    ids_old = df_ids.query('_merge == "right_only"').GameId.tolist()
    ids_new = df_ids.query('_merge != "right_only"').GameId.tolist()

    df_final = pd.concat([df_new.query('GameId in @ids_new'), df_old.query('GameId in @ids_old')])

    return df_final
