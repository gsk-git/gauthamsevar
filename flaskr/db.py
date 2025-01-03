import mysql.connector, uuid, os

#Database credentials
db_pswd = os.environ.get('wip_db_password')
#print(db_pswd)

#Generating a unique id function
def genUUID ():
    return str(uuid.uuid4())

#Connecting to the database
wip_db = mysql.connector.connect(host="localhost", user="root", passwd=db_pswd, database="wip")

#print(wip_db)

#Creating a cursor object using the cursor() method
mycursor = wip_db.cursor()

#Drop Table
def dropTableQuery ():
    query = "DROP TABLE IF EXISTS Users"
    mycursor.execute(query)
    wip_db.commit()
    wip_db.close()

#Creating a table
def createTableQuery ():
    #Creating a cursor object using the cursor() method
    mycursor = wip_db.cursor()
    #Preparing SQL query to CREATE a table in the database
    query = "CREATE TABLE Users (\
    AID INT NOT NULL AUTO_INCREMENT,\
    UUID varchar(255) NOT NULL,\
    LastName varchar(255),\
    FirstName varchar(255),\
    EmailID varchar(255),\
    City varchar(255),\
    Gender varchar(255),\
    Mobile varchar(255),\
    CREATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
    UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
    PRIMARY KEY (AID, UUID));\
    ALTER TABLE Users AUTO_INCREMENT=100;"
    #Executing the SQL query
    mycursor.execute(query)
    #Commit the transaction
    wip_db.commit()
    wip_db.close()

#Inserting data into table
def insertQuery (uuid,lname,fname, email, city, gen, mobile, pswd):
    db_pswd = os.environ.get('wip_db_password')
    wip_db = mysql.connector.connect(host="localhost", user="root", passwd=db_pswd, database="wip")
    mycursor = wip_db.cursor()
    #Creating a cursor object using the cursor() method
    #Preaparing SQL query to INSERT a record into the database.
    query = "INSERT INTO Users (UUID, LastName, FirstName, EmailID, City, Gender, Mobile, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (uuid, lname, fname, email, city, gen, mobile, pswd)
    #Executing the SQL query
    mycursor.execute(query, values)
    #Commit the transaction
    wip_db.commit()
    #Closing the connection
    #wip_db.close()
    

#calling the insertQuery function
#insertQuery(genUUID(), "Kumar", "Rahul", "rahul.kumar@example.com", "Bangalore", "Male", "9876543210", "holaholahola")
wip_db.close()


print(mycursor.rowcount, "record inserted.")