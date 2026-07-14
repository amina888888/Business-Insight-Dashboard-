import pandas as pd
import numpy as np
from db_manager import save_to_db

def generate_and_save(n_users=50):
    data = {
        'user_id': range(1, n_users + 1),
        'session_duration': np.random.uniform(1, 60, n_users),
        'pages_visited': np.random.randint(1, 20, n_users),
        'conversion_rate': np.random.uniform(0, 0.2, n_users),
        'revenue': np.random.randint(10, 1000, n_users)
    }
    df = pd.DataFrame(data)
    save_to_db(df)