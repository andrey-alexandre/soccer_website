import pandas as pd
from datetime import datetime
from .run import run

def action():
    pd.DataFrame({'Data': [datetime.now()]}).to_csv('/home/app/webapp/teste.csv')

    
if __name__ == '__main__':
    action()