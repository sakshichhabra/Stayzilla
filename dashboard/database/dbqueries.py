# get_states = 'SELECT DISTINCT upper(state) AS \"state\" FROM listing;'

get_location_percent = "SELECT round(COUNT(*) * 100/(select count(*) from listing),2) as percent, state" \
                       " FROM (SELECT distinct(listing.id), state FROM LISTING" \
                       " JOIN BOOKING ON booking.listing_id = listing.id " \
                       "where listing.id in(SELECT DISTINCT listing_id from booking) " \
                       "order by listing.id desc) " \
                       "group by state;"

get_chart_data = " select TO_CHAR(TO_DATE(mon, 'MM'), 'Mon') as Mont,bookingprice as booking, state "\
                 "from (select mon ,round(avg(price)) as bookingprice, state  "\
                 "from (select Round((total_price/(total_guests * no_of_days)),2) as price,mon, state "\
                 "from(select state, Round(SUM(price),2)as total_price, " \
                 "Round(Sum(number_of_guests),2) as total_guests,id,mon," \
                 " sum(number_of_days) as no_of_days "\
                "from(select listing.id, price, state, number_of_guests ," \
                 " extract(MONTH FROM CHECK_IN) as mon,(check_out-check_in) as number_of_days "\
                "  from booking join listing on booking.listing_id = listing.id) "\
                " group by id,mon,state "\
                " ))group by mon, state order by mon ) "\
                " WHERE state = %s;"

get_all_states = "select distinct state as state from listing order by state ASC;"


get_single_private_rooms = "select count(booking) as SINGLEPRIVATEROOM from "\
                 "(select booking.id as booking, "\
                 "room_type from booking, listing "\
                 "WHERE booking.listing_id = listing.id "\
                 "AND state = %s "\
                 "AND (UPPER(room_type) LIKE UPPER('Private Room') " \
                 " OR " \
                 " UPPER(room_type) LIKE UPPER('Private_Room') "\
                 "))"

get_entire_apt = "select count(booking) as ENTIREROOMS from "\
                 "(select booking.id as booking, "\
                 "room_type from booking, listing "\
                 "WHERE booking.listing_id = listing.id "\
                 "AND state = %s "\
                 "AND (UPPER(room_type) LIKE UPPER('Entire home/apt') " \
                 "OR UPPER(room_type) LIKE UPPER('Entire place') " \
                 "OR UPPER(room_type) LIKE UPPER('Entire_place')) "\
                 ")"

get_single_shared_rooms = "select count(booking) as SHAREDROOMS from "\
                 "(select booking.id as booking, "\
                 "room_type from booking, listing "\
                 "WHERE booking.listing_id = listing.id "\
                 "AND state = %s "\
                 "AND (UPPER(room_type) LIKE UPPER('Shared room') " \
                 "OR UPPER(room_type) LIKE UPPER('Shared_room'))"\
                 ")"

get_max_state_month = "select state||' in '|| TO_CHAR(TO_DATE(mon, 'MM'), 'Month') as STATE" \
                      " from(select count(*) as number_of_booking, state, mon " \
                 "from( select extract(MONTH FROM CHECK_IN) as mon,listing_id, state " \
                 "from booking join listing on booking.listing_id = listing.id)" \
                 " group by mon, state) order by number_of_booking desc " \
                 "fetch first 1 row only;"

get_best_home ="select id as ID from(select id, (price/nog) as priceperguest, review from(select listing.id as id," \
               " sum(price)as price, sum(number_of_guests) as nog, sum(score) as review from booking " \
               "join listing on booking.listing_id = listing.id " \
               "join review on review.listing_id = booking.listing_id " \
               "group by listing.id)) order by priceperguest asc, " \
               "review desc fetch first 1 row only"

get_best_host = "select first_name||' '||last_name ||' having ' ||" \
                " TO_CHAR(max_profit, 'L999,999,999.00') || ' of sales' as HOST from "\
                "(select sum(price) as max_profit, host.host_id as host "\
                " from listing join host on host.host_id = listing.host_id "\
                " join booking on booking.listing_id = listing.id  "\
                " group by host.host_id order by max_profit desc "\
                " fetch first 1 row only) "\
                " JOIN USERS ON users.user_id = host"

get_least_avail = "SELECT first_name||' '||last_name as NAME FROM "\
            "(  "\
            "    SELECT USER_ID AS HOST_ID, SUM(AVAILABLES) AS TOTAL_AVAILABLES FROM "\
            "        (  "\
            "            SELECT USER_ID, LISTING_ID, COUNT(AVAILABILITY_DATE) AS AVAILABLES FROM  "\
            "            LISTING "\
            "            JOIN USERS ON LISTING.host_id = USERS.USER_ID "\
            "            JOIN AVAILABLE ON AVAILABLE.LISTING_ID = ID "\
            "            WHERE "\
            "            AVAILABLE.IS_AVAILABLE = 1 "\
            "            GROUP BY USER_ID, LISTING_ID "\
            "        )  "\
            "    GROUP BY USER_ID   "\
            ") "\
            "JOIN USERS ON USERS.USER_ID = HOST_ID "\
            "ORDER BY TOTAL_AVAILABLES DESC "\
            "FETCH FIRST ROW ONLY "

get_info = "SELECT 'Listing' AS NAME, COUNT(*) AS Count FROM LISTING UNION " \
           "SELECT 'Review' AS NAME, COUNT(*) AS Count FROM REVIEW UNION " \
           "SELECT 'Booking' AS NAME, COUNT(*) AS Count FROM BOOKING UNION " \
           "SELECT 'Available' AS NAME, COUNT(*) AS Count FROM AVAILABLE UNION " \
           "SELECT 'Host' AS Name,COUNT(*) AS Count FROM HOST UNION " \
           "SELECT 'Customer' AS Name, COUNT(*) AS Count FROM CUSTOMER UNION " \
           "SELECT 'Users' AS NAME , COUNT(*) AS Count FROM USERS;"


get_profit = "select (sum(price)* 0.1) as profit, yea as yr from " \
             "(select price,extract(YEAR FROM CHECK_IN) as yea from booking " \
             "join listing on listing.id = booking.listing_id " \
             "where state = %s)group by yea;"