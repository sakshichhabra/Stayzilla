from django.db import connection
from collections import namedtuple
from search.database import dbqueries
from listing.models import Listing


class DBManager:

    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod
    def search_score_filtered_listing(searchquery, score):
        print("Price in db quer score")
        cursor = connection.cursor()
        try:
            destination = searchquery.get('destination')
            print(destination)
            from_date = searchquery.get('from_date')
            print(from_date)
            to_date = searchquery.get('to_date')
            print(to_date)
            num_guests = searchquery.get('num_guests')
            cursor.execute(dbqueries.search_score_filtered_listing,
                           [from_date, from_date, to_date, destination, num_guests, score])
            results = DBManager.named_tuple_fetchall(cursor)
            if len(results) == 0:
                print("None")
                return None
            else:
                valid_listings = []
                for dict_listing in results:
                    listing = Listing()

                    listing.id = dict_listing.LISTING_ID
                    listing.name = dict_listing.NAME
                    listing.description = dict_listing.DESCRIPTION
                    listing.picture_url = dict_listing.PICTURE_URL
                    listing.price = dict_listing.PRICE
                    listing.score = dict_listing.SCORE

                    valid_listings.append(listing)
                return valid_listings
        except Exception as error:
            print(error)
            return False
        finally:
            cursor.close()

    @staticmethod
    def search_price_filtered_listing(searchquery, price):
        print("Price in db quer")
        print(price)
        cursor = connection.cursor()
        try:
            destination = searchquery.get('destination')
            print(destination)
            from_date = searchquery.get('from_date')
            print(from_date)
            to_date = searchquery.get('to_date')
            print(to_date)
            num_guests = searchquery.get('num_guests')
            cursor.execute(dbqueries.search_price_filtered_listing,
                           [from_date, from_date, to_date, destination, num_guests,price])
            results = DBManager.named_tuple_fetchall(cursor)
            if len(results) == 0:
                print("None")
                return None
            else:
                valid_listings = []
                for dict_listing in results:
                    listing = Listing()

                    listing.id = dict_listing.LISTING_ID
                    listing.name = dict_listing.NAME
                    listing.description = dict_listing.DESCRIPTION
                    listing.picture_url = dict_listing.PICTURE_URL
                    listing.price = dict_listing.PRICE
                    listing.score = dict_listing.SCORE

                    valid_listings.append(listing)
                return valid_listings
        except Exception as error:
            print(error)
            return False
        finally:
            cursor.close()

    @staticmethod
    def search_customer_listing(searchquery):
        cursor = connection.cursor()
        try:
            destination = searchquery.get('destination')
            print(destination)
            from_date = searchquery.get('from_date')
            print (from_date)
            to_date = searchquery.get('to_date')
            print(to_date)
            num_guests = searchquery.get('num_guests')
            cursor.execute(dbqueries.search_customer_listing, [from_date, from_date, to_date, destination, num_guests])
            results = DBManager.named_tuple_fetchall(cursor)
            if len(results) == 0:
                print("None")
                return None
            else:
                valid_listings = []
                for dict_listing in results:
                    listing = Listing()
                    listing.id = dict_listing.LISTING_ID
                    listing.name = dict_listing.NAME
                    listing.description = dict_listing.DESCRIPTION
                    listing.picture_url = dict_listing.PICTURE_URL
                    listing.price = dict_listing.PRICE
                    listing.score = dict_listing.SCORE

                    valid_listings.append(listing)
                return valid_listings
        except Exception as error:
            print(error)
            return False
        finally:
            cursor.close()

