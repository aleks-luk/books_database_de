from user_api import UserAPI
from books_scrapper import BookScraper
import csv_data_transformation
import upload_csv_to_s3
import etl_s3_to_rds

def main():
    # Run user_api_data.py
    user_api = UserAPI()
    users = user_api.fetch_users_from_api()
    user_api.save_to_file(users, 'raw_data/users_api_data.json')

    # Run books_scrapper.py
    base_url = 'https://libra.ibuk.pl/ksiazki'
    landing_page = 'https://libra.ibuk.pl'
    scraper = BookScraper(base_url, landing_page)
    scraper.scrape()
    scraper.save_to_csv('raw_data/scrapped_book_data.csv')

    # Run csv_data_transformation.py
    csv_data_transformation.transform_books()
    csv_data_transformation.transform_users()
    csv_data_transformation.transform_ratings()
    csv_data_transformation.transform_user_api_data()
    csv_data_transformation.transform_scrapped_books_data()

    # Run upload_csv_to_s3.py
    upload_csv_to_s3.upload_all_files()

    # Run etl_s3_to_rds.py
    etl_s3_to_rds.load_data_from_s3_to_rds()

if __name__ == '__main__':
    main()

