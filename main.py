from logger_config import logger
from db_manager import init_db
from data_gen import generate_and_save
import pandas as pd
import sqlite3

def run_analysis():
    init_db()
    generate_and_save(50)
    
    conn = sqlite3.connect("business_metrics.db")
    df = pd.read_sql_query("SELECT * FROM user_behavior", conn)
    conn.close()
    
    # Бизнес-логика: индекс вовлеченности
    df['engagement_score'] = (df['session_duration'] * 0.5) + (df['pages_visited'] * 2)
    # Потенциал потери (Churn Risk)
    df['churn_risk'] = (1 - df['conversion_rate']) * df['revenue']
    
    logger.info("Бизнес-анализ выполнен.")
    print(df.sort_values(by='churn_risk', ascending=False).head())

if __name__ == "__main__":
    run_analysis()