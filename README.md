# Books and Users Data Pipeline Project

This project demonstrates building a data pipeline that extracts, transforms, and loads (ETL) data from various sources into a relational database. The pipeline involves scraping book data, fetching user data from an API, transforming the raw data, uploading the transformed data to an AWS S3 bucket, and finally loading it into an AWS RDS MySQL database.

## Overview
This project shows data extraction, transformation, and loading using various tools and technologies, including Python, AWS S3, and AWS RDS. The project pipeline involves:

Extracting book data from a website and user data from an API.
Transforming the raw data into a structured format suitable for database storage.
Uploading the transformed data to an AWS S3 bucket.
Loading the data from the S3 bucket into an AWS RDS MySQL database.

## Project Structure

**1. Data Extraction**

* user_api_data.py - Fetches user data from an external API and saves it as a JSON file.
* books_scrapper.py - Scrapes book data from a website and saves it as a CSV file.
  
**2. Data Transformaion**

* csv_data_transformation.py - Transforms raw CSV files into a format suitable for loading into the database.

**3. Data Loading**

* upload_csv_to_s3.py -  Uploads the transformed CSV files to an AWS S3 bucket.
* etl_s3_to_rds.py - Loads the CSV files from the S3 bucket into an AWS RDS MySQL database.
* main.py -  Main script that orchestrates the entire ETL process.

## Future Enhancements
To be continued.
