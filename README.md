# Building-a-Cricket-Statistics-Pipeline-with-Google-Cloud-Services

***Designing a Scalable Cricket Data Pipeline with Google Cloud***
In today’s data-driven world, transforming raw sports data into actionable insights requires a well-orchestrated pipeline. This project showcases the complete journey of building a cricket statistics pipeline using the robust suite of Google Cloud services. From fetching real-time data through the Cricbuzz API to presenting it on an interactive Looker Studio dashboard, every stage — from extraction to visualization — is carefully designed to ensure smooth and efficient data flow. It’s a hands-on demonstration of how cloud-native tools can power modern data engineering solutions in the field of sports analytics.


***ARCHITECTURE***
![Untitled Diagram drawio](https://github.com/user-attachments/assets/1c8b118d-ad8a-4781-9501-861040a86668)

***🔍 Data Extraction with Python and the Cricbuzz API***
The journey kicks off by tapping into the Cricbuzz API using Python to extract real-time cricket statistics. Python's robust API integration capabilities help automate and streamline the data collection process, ensuring a consistent flow of fresh data.

***☁️ Data Storage in Google Cloud Storage (GCS)***
Once retrieved, the raw cricket data is formatted as CSV and stored securely in Google Cloud Storage. This step ensures the data is easily accessible, scalable, and ready for downstream processing in a cloud-native environment.

***⚙️ Triggering Workflows with Cloud Functions***
To automate the pipeline, a Cloud Function is configured to trigger on every new file upload to GCS. This event-driven approach ensures the pipeline responds instantly to incoming data without manual intervention.

***🚀 Orchestrating Data Processing with Cloud Composer (Airflow)***
The Cloud Function launches a scheduled Airflow DAG in Cloud Composer, orchestrating the flow from GCS to BigQuery. Tasks are defined and managed efficiently, ensuring reliable execution and error handling across the workflow.

***🔄 ETL with Dataflow into BigQuery***
A Dataflow job, triggered by the orchestration layer, transforms and loads the data into BigQuery. The job is configured to handle batch processing for accurate and optimized data ingestion, enabling real-time analytics.

***📊 Building an Interactive Dashboard with Looker Studio***
With the processed data now in BigQuery, Looker Studio is used to create an engaging and insightful dashboard. The final product enables dynamic visualization of cricket statistics, turning raw data into decision-ready insights.

***DASHBOARD***

![image](https://github.com/user-attachments/assets/7aa05e96-2825-4452-81d4-32f7786be12f)


