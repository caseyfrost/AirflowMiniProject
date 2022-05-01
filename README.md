# AirflowMiniProject
Create and run a simple dag to download and process stock data.

This basic project uses the sequential executor, SQLite, and stores data in a local directory


## Instructions

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


## Outputs

1. each time the script runs, and there is stock data to download, two csv files, one for APPL and one for TSLA, will be created in a directory named after that day's date.
2. ![Screen Shot 2022-05-01 at 10 23 57 AM](https://user-images.githubusercontent.com/20688436/166157087-36f3a51d-a736-4840-af81-02bb856c5379.png)
3. The CSV will look like this when opened.
4. ![Screen Shot 2022-05-01 at 10 25 29 AM](https://user-images.githubusercontent.com/20688436/166157130-daf2f022-548c-448e-9634-cab1d1bdfca8.png)
5. The Airflow UI will also indicate if a job ran and the status of the job.
6. ![Screen Shot 2022-05-01 at 10 27 41 AM](https://user-images.githubusercontent.com/20688436/166157195-a087c021-2a78-4cac-b275-930148528dca.png)


