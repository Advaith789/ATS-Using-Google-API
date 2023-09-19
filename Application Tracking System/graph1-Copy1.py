#!/usr/bin/env python
# coding: utf-8

# In[3]:


import psycopg2
import json
from decimal import Decimal

def convert_to_float(data):
    if isinstance(data, dict):
        return {convert_to_float(key): convert_to_float(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_float(element) for element in data]
    elif isinstance(data, Decimal):
        return float(data)  # Convert Decimal to float
    return data

def get_data1():
    conn = psycopg2.connect(
        database="Candidate_List",
        user="postgres",
        password="Adduvaith789",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM list WHERE marital_status = 'Married';")
    rows1 = cursor.fetchone()
    married_count = rows1[0]

    cursor.execute("SELECT count(*) FROM list WHERE marital_status = 'Single';")
    rows2 = cursor.fetchone()
    single_count = rows2[0]

    cursor.close()
    conn.close()

    cols = [
        {"id": "", "label": "Marital Status", "pattern": "", "type": "string"},
        {"id": "", "label": "Married vs Unmarried", "pattern": "", "type": "number"}
    ]
    rows = [
        {"c": [{"v": "Married", "f": None}, {"v": married_count, "f": None}]},
        {"c": [{"v": "Single", "f": None}, {"v": single_count, "f": None}]}
    ]

    data = {
        "cols": cols,
        "rows": rows
    }

    return convert_to_float(data)

if __name__ == '__main__':
    data = get_data1()
    json_data = json.dumps(data)
    print(json_data)


# In[ ]:




