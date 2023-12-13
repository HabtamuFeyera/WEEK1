#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine

def load_data_from_postgres(db_params):
    engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')
    sql_query = "SELECT * FROM tellco_data;"
    mydata = pd.read_sql_query(sql_query, engine)
    return mydata


