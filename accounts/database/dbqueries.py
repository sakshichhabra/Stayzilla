insert_user = "INSERT INTO USERS(Password, Email_Address, First_Name, Last_Name) VALUES(%s, %s, %s, %s)"

get_user = "SELECT * FROM USERS WHERE User_ID = %s"
get_customer_id = "SELECT CUSTOMER_ID FROM CUSTOMER"

authenticate_user = "SELECT * FROM USERS WHERE Email_Address = %s AND Password = %s"


