insert_booking = "INSERT INTO BOOKING(LISTING_ID, CUSTOMER_ID, CHECK_IN, CHECK_OUT, PRICE, NUMBER_OF_GUESTS)" \
                 " VALUES(%s, %s, TO_DATE(%s,'DD-Mon-YY'), TO_DATE(%s,'DD-Mon-YY'), %s, %s);"

get_listing_ids = "SELECT ID FROM LISTING;"
get_listing_for_id = "SELECT LISTING.*, (USERS.FIRST_NAME ||' '|| USERS.LAST_NAME) AS HOST_NAME, " \
                     "USERS.EMAIL_ADDRESS AS HOST_CONTACT, SCORE " \
                     "FROM LISTING, USERS, (SELECT ROUND(AVG(SCORE)/2) " \
                     "AS SCORE FROM REVIEW WHERE LISTING_ID = %s)" \
                     " WHERE ID = %s  AND USERS.USER_ID = LISTING.HOST_ID"

get_listing_reviews = "SELECT REVIEW.*, USERS.FIRST_NAME AS REVIEWER_NAME FROM REVIEW, USERS " \
                      "WHERE USERS.USER_ID = REVIEWER_ID AND Listing_id = %s ORDER BY REVIEW_DATE DESC;"

get_popularity_trend = "SELECT ROUND(AVG(BOOKINGS)) AS \"BOOKINGS\", " \
                       "TO_CHAR(TO_DATE(\"MON\", 'MM'), 'Mon') AS \"MONTH\"" \
                       "FROM (SELECT COUNT(*) AS BOOKINGS, " \
                       "EXTRACT(MONTH FROM CHECK_IN) AS \"MON\", " \
                       "EXTRACT(YEAR FROM CHECK_IN) AS \"YEAR\" " \
                       "FROM BOOKING WHERE LISTING_ID = %s " \
                       "GROUP BY  EXTRACT(MONTH FROM CHECK_IN), " \
                       "EXTRACT(YEAR FROM CHECK_IN)) " \
                       "GROUP BY \"MON\" " \
                       "ORDER BY \"MON\";"

get_monthly_price_trend = "SELECT TO_CHAR(TO_DATE(MON, 'MM'), 'Month') AS MONTH, "\
                          "ROUND(AVG_PRICE, 2) AS PRICE "\
                          "FROM ("\
                          "SELECT MON, AVG(PRICE_PER_GUEST_PER_DAY) AS AVG_PRICE "\
                          "FROM "\
                          "(SELECT MON, "\
                          "PRICE_PER_GUEST/NUMBER_OF_DAYS AS PRICE_PER_GUEST_PER_DAY "\
                          "FROM "\
                          "(SELECT EXTRACT(MONTH FROM CHECK_IN) AS MON, "\
                          "PRICE, "\
                          "PRICE/ NUMBER_OF_GUESTS AS PRICE_PER_GUEST, "\
                          "(CHECK_OUT-CHECK_IN) AS "\
                          "NUMBER_OF_DAYS, "\
                          "NUMBER_OF_GUESTS "\
                          "FROM BOOKING "\
                          "WHERE LISTING_ID = %s) "\
                          ") "\
                          "GROUP BY MON) " \
                          "ORDER BY MON;"

get_available_dates_with_price = "SELECT TO_CHAR(AVAILABILITY_DATE, 'DD-Mon-YY') AS AVAILABILITY_DATE, PRICE" \
                                " FROM AVAILABLE WHERE LISTING_ID = %s AND IS_AVAILABLE = 1;"

get_best_time_to_visit = "SELECT TO_CHAR(TO_DATE(MON, 'MM'), 'Month') AS MONTH FROM "\
                         "       ( "\
                         "        "\
                         "           SELECT MON, ROUND(AVG(PRICE_PER_GUEST_PER_DAY), 2) AS PRICE, SUM(NUMBER_OF_DAYS)" \
                         "               AS TOTAL_DAYS FROM ( "\
                         "               SELECT MON, PRICE_PER_GUEST/NUMBER_OF_DAYS AS PRICE_PER_GUEST_PER_DAY, "\
                         "               NUMBER_OF_DAYS FROM "\
                         "                ( "\
                         "                    SELECT EXTRACT(MONTH FROM CHECK_IN) AS MON, "\
                         "                    PRICE/NUMBER_OF_GUESTS AS PRICE_PER_GUEST, "\
                         "                    (CHECK_OUT-CHECK_IN) AS NUMBER_OF_DAYS "\
                         "                    FROM BOOKING WHERE LISTING_ID = %s "\
                         "                ) "\
                         "            ) "\
                         "            GROUP BY MON "\
                         "       ) "\
                         "    ORDER BY TOTAL_DAYS DESC, PRICE ASC FETCH FIRST 1 ROWS ONLY"

get_past_weekly_price_trend = "WITH "\
    " DATES AS (SELECT UPPER_BOUND.CURRENT_DATE - ROWNUM AS VALID_DATE "\
    "            FROM ALL_OBJECTS, " \
    "            (SELECT TO_DATE(%s, 'DD-Mon-YY') AS CURRENT_DATE FROM DUAL) UPPER_BOUND WHERE  ROWNUM <= 4), "\
    " DATA_TABLE AS (SELECT CHECK_IN, CHECK_OUT, (PRICE/(CHECK_OUT-CHECK_IN)) AS PAST_PRICE, "\
    "                           VALID_DATE FROM BOOKING, "\
    "                            DATES WHERE LISTING_ID = %s AND to_number(to_char(DATES.VALID_DATE, 'DDD')) "\
    "                            BETWEEN to_number(to_char(CHECK_IN, 'DDD')) "\
    "                            AND "\
    "                            to_number(to_char(CHECK_OUT, 'DDD'))) "\
    " SELECT PAST_PRICE AS PRICE, TO_CHAR(VALID_DATE, 'DD-Mon-YY') AS \"DATE\",  NVL(PRICE, 0) AS CURRENT_PRICE FROM "\
    " (SELECT  NVL(ROUND(AVG(PAST_PRICE), 2), 0) AS PAST_PRICE, "\
    " DATES.VALID_DATE "\
    " FROM "\
    " DATA_TABLE "\
    " RIGHT JOIN DATES ON DATES.VALID_DATE = DATA_TABLE.VALID_DATE "\
    " GROUP BY DATES.VALID_DATE"\
    " ORDER BY DATES.VALID_DATE) "\
    " LEFT JOIN AVAILABLE ON AVAILABLE.AVAILABILITY_DATE = VALID_DATE AND AVAILABLE.LISTING_ID = %s;"


get_future_weekly_price_trend = "WITH "\
    " DATES AS (SELECT UPPER_BOUND.CURRENT_DATE + ROWNUM AS VALID_DATE "\
    "            FROM ALL_OBJECTS, " \
    "            (SELECT TO_DATE(%s, 'DD-Mon-YY') AS CURRENT_DATE FROM DUAL) UPPER_BOUND WHERE  ROWNUM <= 4), "\
    " DATA_TABLE AS (SELECT CHECK_IN, CHECK_OUT, (PRICE/(CHECK_OUT-CHECK_IN)) AS FUTURE_PRICE, "\
    "                           VALID_DATE FROM BOOKING, "\
    "                            DATES WHERE LISTING_ID = %s AND to_number(to_char(DATES.VALID_DATE, 'DDD')) "\
    "                            BETWEEN to_number(to_char(CHECK_IN, 'DDD')) "\
    "                            AND "\
    "                            to_number(to_char(CHECK_OUT, 'DDD'))) "\
    " SELECT FUTURE_PRICE AS PRICE, TO_CHAR(VALID_DATE, 'DD-Mon-YY') AS \"DATE\",  NVL(PRICE, 0) AS CURRENT_PRICE FROM "\
    " (SELECT NVL(ROUND(AVG(FUTURE_PRICE), 2), 0) AS FUTURE_PRICE, "\
    " DATES.VALID_DATE "\
    " FROM "\
    " DATA_TABLE "\
    " RIGHT JOIN DATES ON DATES.VALID_DATE = DATA_TABLE.VALID_DATE "\
    " GROUP BY DATES.VALID_DATE"\
    " ORDER BY DATES.VALID_DATE) "\
    " LEFT JOIN AVAILABLE ON AVAILABLE.AVAILABILITY_DATE = VALID_DATE AND AVAILABLE.LISTING_ID = %s;"
