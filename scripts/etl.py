
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

ROOT = Path(__file__).parents[1]
DATA_RAW = ROOT / 'data' / 'raw'
DB_PATH = ROOT / 'data' / 'sales.db'

def run_etl():
    engine = create_engine("sqlite:///" + DB_PATH.as_posix())
    customers = pd.read_csv(DATA_RAW / 'customers.csv', parse_dates=['signup_date'])
    products = pd.read_csv(DATA_RAW / 'products.csv')
    orders = pd.read_csv(DATA_RAW / 'orders.csv', parse_dates=['order_date'])
    customers.to_sql('customers', engine, if_exists='replace', index=False)
    products.to_sql('products', engine, if_exists='replace', index=False)
    orders.to_sql('orders', engine, if_exists='replace', index=False)
    print("ETL completed: tables written to", DB_PATH)

if __name__ == "__main__":
    run_etl()
