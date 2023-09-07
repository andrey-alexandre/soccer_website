import pandas as pd
from datetime import datetime

def action():
    pd.DataFrame({'Data': [datetime.now()]}).to_csv('/home/app/webapp/teste.csv')

    
if __name__ == '__main__':
    action()