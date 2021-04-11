from django.db import connection
from collections import namedtuple
from listing.database import dbqueries
from listing.models import Listing, Review


class DBManager:

    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod
    def add_bookings(bookings):
        rows = []
        for booking in bookings:
            listing_id = booking.listing_id
            customer_id = booking.customer_id
            check_in = booking.check_in
            check_out = booking.check_out
            price = booking.price
            number_of_guests = booking.number_of_guests
            row = {'1': listing_id,
                   '2': customer_id,
                   '3': check_in,
                   '4': check_out,
                   '5': price,
                   '6': number_of_guests}
            rows.append(row)

        cursor = connection.cursor()
        try:
            print("Inserting values")
            cursor.executemany(dbqueries.insert_booking, rows)
            connection.commit()
        except ConnectionError as ex:
            obj, = ex.args
            print("Context:", obj.context)
            print("Message:", obj.message)
        finally:
            cursor.close()

    @staticmethod
    def add_booking(booking):
        cursor = connection.cursor()
        try:
            listing_id = booking.get('listing_id')
            customer_id = booking.get('customer_id')
            check_in = booking.get('check_in')
            check_out = booking.get('check_out')
            price = booking.get('price')
            number_of_guests = booking.get('number_of_guests')

            cursor.execute(dbqueries.insert_booking,
                           [listing_id, customer_id, check_in, check_out, price, number_of_guests])
            return True
        except Exception as error:
            print(error)
            return error
        finally:
            cursor.close()

    @staticmethod
    def get_listing_for_id(id):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_listing_for_id, [id, id])
            results = DBManager.named_tuple_fetchall(cursor)

            if len(results) == 0:
                return None
            else:
                dict_listing = results[0]

                listing = Listing()

                listing.id = dict_listing.ID
                listing.host_id = dict_listing.HOST_ID
                listing.host_name = dict_listing.HOST_NAME
                listing.host_contact = dict_listing.HOST_CONTACT
                listing.name = dict_listing.NAME
                listing.description = dict_listing.DESCRIPTION
                listing.house_rules = dict_listing.HOUSE_RULES
                listing.accommodates = dict_listing.ACCOMMODATES
                listing.cancellation_policy = dict_listing.CANCELLATION_POLICY
                listing.room_type = dict_listing.ROOM_TYPE
                listing.property_type = dict_listing.PROPERTY_TYPE
                listing.amenities = dict_listing.AMENITIES
                listing.picture_url = dict_listing.PICTURE_URL
                listing.latitude = dict_listing.LATITUDE
                listing.longitude = dict_listing.LONGITUDE
                listing.city = dict_listing.CITY
                listing.street = dict_listing.STREET
                listing.state = dict_listing.STATE
                listing.zip_code = dict_listing.ZIP_CODE
                listing.score = dict_listing.SCORE

                return listing
        finally:
            cursor.close()

    @staticmethod
    def get_listing_id():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_listing_ids)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                listing_ids = []
                for dict in results:
                    listing_ids.append(dict.ID)
                return listing_ids
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_reviews(listing_id):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_listing_reviews, [listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                reviews = []
                for dict_review in results:
                    id = dict_review.ID
                    listing_id = dict_review.LISTING_ID
                    reviewer_id = dict_review.REVIEWER_ID
                    reviewer_name = dict_review.REVIEWER_NAME
                    date = dict_review.REVIEW_DATE
                    score = dict_review.SCORE
                    comments = dict_review.COMMENTS
                    review = Review(id, listing_id, reviewer_id, reviewer_name, date, score, comments)
                    reviews.append(review)
                return reviews
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_popularity_trend(listing_id):
        cursor = connection.cursor()
        try:
            # print(dbqueries.get_popularity_trend)
            cursor.execute(dbqueries.get_popularity_trend, [listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                bookings = []
                for dict_booking in results:
                    bookings.append(dict_booking)
                return bookings
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_monthly_price_trend(listing_id):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_monthly_price_trend, [listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                bookings = []
                for dict_booking in results:
                    bookings.append(dict_booking)
                return bookings
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_past_weekly_price_trend(listing_id, date):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_past_weekly_price_trend, [date, listing_id, listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                prices = []
                for dict_price in results:
                    date = dict_price.DATE
                    price = dict_price.PRICE
                    current_price = dict_price.CURRENT_PRICE
                    dict_data = {'date': date, 'price': price, 'current_price': current_price}
                    prices.append(dict_data)
                return prices
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_future_weekly_price_trend(listing_id, date):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_future_weekly_price_trend, [date, listing_id, listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                prices = []
                for dict_price in results:
                    date = dict_price.DATE
                    price = dict_price.PRICE
                    current_price = dict_price.CURRENT_PRICE
                    dict_data = {'date': date, 'price': price, 'current_price': current_price}
                    prices.append(dict_data)
                return prices
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_available_dates_with_price(listing_id):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_available_dates_with_price, [listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                availability = []
                for dict_availability in results:
                    date = dict_availability.AVAILABILITY_DATE
                    price = dict_availability.PRICE
                    dict = {'date': date, 'price': price}
                    availability.append(dict)
                return availability
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_best_time_to_visit(listing_id):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_best_time_to_visit, [listing_id])
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                month = results[0].MONTH
                return month
        except Exception as error:
            print(error)
            return None
        finally:
            cursor.close()
