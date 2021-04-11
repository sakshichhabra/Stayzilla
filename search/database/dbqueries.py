search_customer_listing = \
" WITH "\
   " DATES AS "\
   "(SELECT "\
   " TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum AS VALID_DATE "\
   " FROM all_objects "\
   " WHERE TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum <= TO_DATE(%s, 'DD-Mon-YY')) "\
" SELECT LTABLE.ID AS LISTING_ID, LTABLE.NAME, SUBSTR(LTABLE.DESCRIPTION,0,60)AS DESCRIPTION,LTABLE.PICTURE_URL,PRI_SCORE.PRICE, NVL(round(PRI_SCORE.SCORE/2),0) AS SCORE "\
"FROM "\
"(SELECT LISTING.ID, LISTING.NAME, LISTING.DESCRIPTION,LISTING.PICTURE_URL FROM LISTING WHERE UPPER (LISTING.CITY )= UPPER(%s) AND " \
    "LISTING.ACCOMMODATES >= %s) LTABLE "\
"JOIN "\
"(SELECT "\
   " A.LISTING_ID, "\
   " A.PRICE, "\
   " B.SCORE "\
   " FROM "\
   "(SELECT "\
   "LISTING_ID,  "\
   "round(AVG(PRICE)) AS PRICE "\
   "FROM AVAILABLE, DATES "\
   "WHERE AVAILABLE.AVAILABILITY_DATE = DATES.VALID_DATE "\
   "AND AVAILABLE.IS_AVAILABLE = 1 "\
   "GROUP BY LISTING_ID "\
   "ORDER BY LISTING_ID) A "\
   "LEFT JOIN "\
   "(SELECT "\
        "LISTING_ID, "\
        "ROUND(AVG(SCORE)) AS SCORE "\
        "FROM REVIEW "\
        "GROUP BY "\
        "LISTING_ID) B "\
   "ON A.LISTING_ID = B.LISTING_ID "\
   "ORDER BY A.LISTING_ID "\
")PRI_SCORE "\
"ON LTABLE.ID = PRI_SCORE.LISTING_ID ORDER BY LISTING_ID DESC"

search_price_filtered_listing= \
" WITH "\
   " DATES AS "\
   "(SELECT "\
   " TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum AS VALID_DATE "\
   " FROM all_objects "\
   " WHERE TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum <= TO_DATE(%s, 'DD-Mon-YY')) "\
" SELECT LTABLE.ID AS LISTING_ID, LTABLE.NAME, SUBSTR(LTABLE.DESCRIPTION,0,60)AS DESCRIPTION,LTABLE.PICTURE_URL,PRI_SCORE.PRICE, NVL(round(PRI_SCORE.SCORE/2),0) AS SCORE "\
"FROM "\
"(SELECT LISTING.ID, LISTING.NAME, LISTING.DESCRIPTION,LISTING.PICTURE_URL FROM LISTING WHERE UPPER (LISTING.CITY )= UPPER(%s) AND " \
    "LISTING.ACCOMMODATES >= %s) LTABLE "\
"JOIN "\
"(SELECT "\
   " A.LISTING_ID, "\
   " A.PRICE, "\
   " B.SCORE "\
   " FROM "\
   "(SELECT "\
   "LISTING_ID,  "\
   "round(AVG(PRICE)) AS PRICE "\
   "FROM AVAILABLE, DATES "\
   "WHERE AVAILABLE.AVAILABILITY_DATE = DATES.VALID_DATE "\
   "AND AVAILABLE.IS_AVAILABLE = 1 "\
   "GROUP BY LISTING_ID "\
   "ORDER BY LISTING_ID) A "\
   "LEFT JOIN "\
   "(SELECT "\
        "LISTING_ID, "\
        "ROUND(AVG(SCORE)) AS SCORE "\
        "FROM REVIEW "\
        "GROUP BY "\
        "LISTING_ID) B "\
   "ON A.LISTING_ID = B.LISTING_ID "\
   "ORDER BY A.LISTING_ID "\
")PRI_SCORE "\
"ON LTABLE.ID = PRI_SCORE.LISTING_ID WHERE PRI_SCORE.PRICE <= %s ORDER BY PRI_SCORE.PRICE DESC"

search_score_filtered_listing= \
" WITH "\
   " DATES AS "\
   "(SELECT "\
   " TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum AS VALID_DATE "\
   " FROM all_objects "\
   " WHERE TO_DATE(%s, 'DD-Mon-YY') - 1 + rownum <= TO_DATE(%s, 'DD-Mon-YY')) "\
" SELECT LTABLE.ID AS LISTING_ID, LTABLE.NAME, SUBSTR(LTABLE.DESCRIPTION,0,60)AS DESCRIPTION,LTABLE.PICTURE_URL,PRI_SCORE.PRICE, NVL(round(PRI_SCORE.SCORE/2),0) AS SCORE "\
"FROM "\
"(SELECT LISTING.ID, LISTING.NAME, LISTING.DESCRIPTION,LISTING.PICTURE_URL FROM LISTING WHERE UPPER (LISTING.CITY )= UPPER(%s) AND " \
    "LISTING.ACCOMMODATES >= %s) LTABLE "\
"JOIN "\
"(SELECT "\
   " A.LISTING_ID, "\
   " A.PRICE, "\
   " B.SCORE "\
   " FROM "\
   "(SELECT "\
   "LISTING_ID,  "\
   "round(AVG(PRICE)) AS PRICE "\
   "FROM AVAILABLE, DATES "\
   "WHERE AVAILABLE.AVAILABILITY_DATE = DATES.VALID_DATE "\
   "AND AVAILABLE.IS_AVAILABLE = 1 "\
   "GROUP BY LISTING_ID "\
   "ORDER BY LISTING_ID) A "\
   "LEFT JOIN "\
   "(SELECT "\
        "LISTING_ID, "\
        "ROUND(AVG(SCORE)) AS SCORE "\
        "FROM REVIEW "\
        "GROUP BY "\
        "LISTING_ID) B "\
   "ON A.LISTING_ID = B.LISTING_ID "\
   "ORDER BY A.LISTING_ID "\
")PRI_SCORE "\
"ON LTABLE.ID = PRI_SCORE.LISTING_ID WHERE round(PRI_SCORE.SCORE/2) >= %s ORDER BY SCORE ASC"