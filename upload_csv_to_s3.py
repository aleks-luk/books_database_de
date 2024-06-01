import boto3
import logging
import os
# from fork
# Konfiguracja logowania
logging.basicConfig(filename='upload_csv_to_s3.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Konfiguracja AWS S3
s3_bucket_name = 'your-s3-bucket-name'
csv_files = [
    'books_data_transformation_v1.csv',
    'users_data_transformation_v1.csv',
    'ratings_data_transformation_v1.csv',
    'user_api_data_transformation_v1.csv',
    'scrapped_books_data_transformation_v1.csv'
]
csv_files_path = 'files_to_load/'

# Tworzenie klienta S3
s3_client = boto3.client('s3')


def upload_csv_to_s3(file_path, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        logging.info(f'Uploading {file_path} to S3 bucket {bucket}')
        s3_client.upload_file(file_path, bucket, object_name)
        logging.info(f'Successfully uploaded {file_path} to S3 bucket {bucket}')
    except Exception as e:
        logging.error(f'Error uploading {file_path} to S3 bucket {bucket}: {e}')


def upload_all_files():
    for csv_file in csv_files:
        upload_csv_to_s3(os.path.join(csv_files_path, csv_file), s3_bucket_name)


if __name__ == '__main__':
    upload_all_files()