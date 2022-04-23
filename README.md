# AirflowMiniProject
Create and run a simple dag to download and process stock data.

This basic project uses the sequential executor, SQLite, and stores data in a local directory
<br/>
## Instructions

--------------
1. Create a virtual python environment
2. Activate your environment
3. Pip install Airflow
4. Pip instsall yfinance
5. Create your "dags" directory within your Airflow directory - usr/Airflow.
6. Start the Airflow web server
7. Start the Airflow scheduler
8. Move the stock_dag.py file into the dags directory
9. Open a browser to localhost:8080
10. Set up your username and password in the command line
11. Turn on the marketvol dag
12. To test the dag you can trigger it
