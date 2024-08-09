import sqlite3
import pandas as pd
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

### Creating the database in SQLite3

# df = pd.read_csv("data\medfri09.csv", encoding='unicode_escape')

# df.head()

# # connection = sqlite3.connect('demo_test.db')
# # print(connection)

### Creating the table name

# health_data = df.to_sql("us-health", connection, if_exists = 'replace')

# print(health_data)

# connection.close()

# pip install -U langchain langchain-community langchain-openai
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///demo_test.db")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "how many female records avaliable?"})


results = db.run(response)

print(results)