"""Import Libraries"""

from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import FewShotPromptTemplate
from dotenv import load_dotenv
import os
from few_shots import few_shots

load_dotenv()


def get_llm_chain():
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ["GOOGLE_API_KEY"], temprature=0, verbose=True)
    #llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temprature=0)

    user = "root"
    password = "0000"
    host = "localhost"
    port = 3306
    database = "zarasales"

    db = SQLDatabase.from_uri(f'mysql+pymysql://{user}:{password}@{host}/{database}', sample_rows_in_table_info=5)

   # db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vector_data = [" ".join(example.values()) for example in few_shots]
    vector_store = Chroma.from_texts(vector_data, embedding=embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vector_store,
        k=2,
    )

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery:{SQLQuery}\nSQLResult:{SQLResult}\nAnswer:{Answer}",
    )

    system_prefix = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
"""

    system_suffix = """Only use the following tables:\n{table_info}\n\nQuestion: {input}"""

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=system_prefix,
        suffix=system_suffix,
        input_variables=["input","table_info","top_k"],

    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose = True ,prompt=few_shot_prompt)

    return chain


if __name__ == '__main__':
    chain = get_llm_chain()
    chain.invoke("Find total seasonal products of Mens positions at aisle")['result']