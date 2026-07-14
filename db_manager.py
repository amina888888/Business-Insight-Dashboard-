import sqlite3
import pandas as pd
from logger_config import logger

DB_NAME = "business_metrics.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Таблица для бизнес-метрик
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_behavior (
            user_id INTEGER,
            session_duration REAL,
            pages_visited INTEGER,
            conversion_rate REAL,
            revenue REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(df):
    conn = get_connection()
    try:
        df.to_sql('user_behavior', conn, if_exists='append', index=False)
        logger.info(f"Сохранено {len(df)} записей поведения пользователей.")
    except Exception as e:
        logger.error(f"Ошибка БД: {e}")
    finally:
        conn.close()