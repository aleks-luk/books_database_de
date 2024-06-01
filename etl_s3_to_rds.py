import boto3
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
import logging

# Logging configuration
logging.basicConfig(filename='etl_s3_to_rds.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# AWS and RDS configuration
s3_bucket_name = '*'
s3_files = [
    'books_data_transformation_v1.csv',
    'users_data_transformation_v1.csv',
    'ratings_data_transformation_v1.csv',
    'user_api_data_transformation_v1.csv',
    'scrapped_books_data_transformation_v1.csv'
]
rds_host = '*'
rds_port = '*'
rds_dbname = '*'
rds_user = '*'
rds_password = '*'

# S3 client
s3_client = boto3.client('s3')

# Create SQLAlchemy engine
engine = create_engine(f'mysql://{rds_user}:{rds_password}@{rds_host}:{rds_port}/{rds_dbname}')

def load_csv_to_rds(s3_bucket, s3_key, table_name, column_mapping):
    try:
        # Fetching file from S3
        logging.info(f'Fetching {s3_key} from S3 bucket {s3_bucket}')
        s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
        body = s3_object['Body']
        csv_string = body.read().decode('utf-8')

        # Convert CSV string to DataFrame
        data = StringIO(csv_string)
        df = pd.read_csv(data, sep=';')

        # Column mapping
        df = df.rename(columns=column_mapping)

        # Inserting data into RDS
        logging.info(f'Inserting data into {table_name} table in RDS')
        df.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info(f'Successfully inserted data into {table_name} table in RDS')
    except Exception as e:
        logging.error(f'Error inserting data into {table_name} table in RDS: {e}')

def load_data_from_s3_to_rds():
    # Map column for books table
    books_column_mapping = {
        'book_isbn': 'book_isbn',
        'book_title': 'title',
        'book_author': 'author',
        'year_published': 'year',
        'publisher': 'publisher',
        'book_image_url': 'book_image_url'
    }
    load_csv_to_rds(s3_bucket_name, 'books_data_transformation_v1.csv', 'books', books_column_mapping)

    # Map column for users table
    users_column_mapping = {
        'user_city': 'city',
        'user_country': 'country',
        'user_age': 'age'
    }
    load_csv_to_rds(s3_bucket_name, 'users_data_transformation_v1.csv', 'users', users_column_mapping)

    # Map column for ratings table
    ratings_column_mapping = {
        'r_user_id': 'r_user_id',
        'r_book_isbn': 'r_book_isbn',
        'r_book_rating': 'rating'
    }
    load_csv_to_rds(s3_bucket_name, 'ratings_data_transformation_v1.csv', 'ratings', ratings_column_mapping)

    # Load user API data to users table
    load_csv_to_rds(s3_bucket_name, 'user_api_data_transformation_v1.csv', 'users', users_column_mapping)

    # Map column for scrapped books table
    scrapped_books_column_mapping = {
        'book_isbn': 'book_isbn',
        'book_title': 'title',
        'book_author': 'author',
        'year_published': 'year',
        'publisher': 'publisher'
    }
    load_csv_to_rds(s3_bucket_name, 'scrapped_books_data_transformation_v1.csv', 'books', scrapped_books_column_mapping)

if __name__ == '__main__':
    load_data_from_s3_to_rds()
