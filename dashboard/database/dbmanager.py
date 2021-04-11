from django.db import connection
from django.db.utils import IntegrityError
from collections import namedtuple

from dashboard.database import dbqueries


class DBManager:
    @staticmethod
    def named_tuple_fetchall(cursor):  # "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    @staticmethod
    def get_location_percent():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_location_percent)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                location_data = []
                for data in results:
                    location_data.append(data)
                return location_data
        except Exception as error:
            print("Error in GET_LOCATION_PERCENT")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_chart_data(state):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_chart_data, [state])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                chart_data = []
                for data in results:
                    chart_data.append(data)
                return chart_data
        except Exception as error:
            print("Error in get_chart_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_single_private_room_data(state):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_single_private_rooms, [state])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                print(results)
                singlePrivateRoom = results[0].SINGLEPRIVATEROOM
                return singlePrivateRoom
        except Exception as error:
            print("Error in get single private room_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_entire_apt_data(state):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_entire_apt, [state])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                entire_apt_data = results[0].ENTIREROOMS
                return entire_apt_data
        except Exception as error:
            print("Error in get entire apt_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_single_shared_room_data(state):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_single_shared_rooms, [state])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                SharedRooms = results[0].SHAREDROOMS
                return SharedRooms
        except Exception as error:
            print("Error in get single shared room_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_states():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_all_states)
            results = DBManager.named_tuple_fetchall(cursor)
            if results is None:
                return None
            else:
                states = []
                for data in results:
                    state = data.STATE
                    states.append(state)
                return states

        except Exception as error:
            print("Error in get all states")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_best_state():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_max_state_month)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                best_state = results[0].STATE
                return best_state
        except Exception as error:
            print("Error in GET_best_state")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_best_listing():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_best_home)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                best_home = results[0].ID
                return best_home
        except Exception as error:
            print("Error in GET_best_listing")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_best_host():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_best_host)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                best_host = results[0].HOST
                return best_host
        except Exception as error:
            print("Error in GET_best_host")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_least_available():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_least_avail)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                least_avail = results[0].NAME
                return least_avail
        except Exception as error:
            print("Error in least_avail")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_info_table_data():
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_info)
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                info_data = []
                for data in results:
                    info_data.append(data)
                return info_data
        except Exception as error:
            print("Error in get_info_table_data")
            print(error)
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_profit_peryear(state):
        cursor = connection.cursor()
        try:
            cursor.execute(dbqueries.get_profit,[state])
            results = DBManager.named_tuple_fetchall(cursor)

            if results is None:
                return None
            else:
                chart3_data = []
                for data in results:
                    chart3_data.append(data)
                return chart3_data
        except Exception as error:
            print("Error in get_chart3_data")
            print(error)
            return None
        finally:
            cursor.close()