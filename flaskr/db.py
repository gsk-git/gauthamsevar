import mysql.connector, uuid, os

#Database credentials
db_pswd = os.environ.get('wip_db_password')
print(db_pswd)

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
def insertQuery (uuid,lname,fname,city,gen,mobile):
    #Creating a cursor object using the cursor() method
    #Preaparing SQL query to INSERT a record into the database.
    query = "INSERT INTO Users (UUID, LastName, FirstName, City, Gender, Mobile) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (uuid, lname, fname, city, gen, mobile)
    #Executing the SQL query
    mycursor.execute(query, values)
    #Commit the transaction
    wip_db.commit()
    #Closing the connection
    
    

#calling the insertQuery function
insertQuery(genUUID(), "Kumar", "Rahul", "Bangalore", "Male", "9876543210")
insertQuery(genUUID(), "Smith", "John", "New York", "Male", "1234567890")
insertQuery(genUUID(), "Doe", "Jane", "Los Angeles", "Female", "0987654321")
insertQuery(genUUID(), "Williams", "James", "Mumbai", "Male", "1112223334")
insertQuery(genUUID(), "Brown", "Patricia", "Delhi", "Female", "2223334445")
insertQuery(genUUID(), "Jones", "Robert", "Chennai", "Male", "3334445556")
insertQuery(genUUID(), "Garcia", "Linda", "Kolkata", "Female", "4445556667")
insertQuery(genUUID(), "Miller", "Michael", "Hyderabad", "Male", "5556667778")
insertQuery(genUUID(), "Davis", "Barbara", "Pune", "Female", "6667778889")
insertQuery(genUUID(), "Rodriguez", "William", "Ahmedabad", "Male", "7778889990")
insertQuery(genUUID(), "Martinez", "Elizabeth", "Surat", "Female", "8889990001")
insertQuery(genUUID(), "Hernandez", "David", "Jaipur", "Male", "9990001112")
insertQuery(genUUID(), "Lopez", "Jennifer", "Lucknow", "Female", "0001112223")
wip_db.close()


print(mycursor.rowcount, "record inserted.")