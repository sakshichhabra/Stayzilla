insert_listing = "INSERT INTO LISTING(HOST_ID, NAME, ROOM_TYPE, PROPERTY_TYPE, STREET, STATE," \
                 " CITY, ZIP_CODE, AMENITIES, HOUSE_RULES, DESCRIPTION, ACCOMMODATES, PICTURE_URL," \
                 " CANCELLATION_POLICY,LATITUDE,LONGITUDE) " \
                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, 0, 0)"

add_availability = "INSERT INTO AVAILABLE(AVAILABILITY_DATE, PRICE, IS_AVAILABLE) " \
                   "VALUES(TO_DATE(:1, 'DD-MM-YY'), to_number(:2), to_number(:3))"
