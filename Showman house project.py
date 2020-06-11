import sqlite3
conn = sqlite3.connect('showman_house.sqlite3')
cur = conn.cursor()
def customers():
    cur.execute("CREATE TABLE IF NOT EXISTS Customers(CustomerID int identity (1,1) PRIMARY KEY, Name varchar(30) NOT NULL,"
                " Address varchar(30) NOT NULL, City varchar(40) NOT NULL, State varchar(30) NOT NULL, Phone int NOT NULL")
def payment_methods():
    cur.execute("CREATE TABLE IF NOT EXISTS PaymentMethods(PaymentMethodID int PRIMARY KEY, Description varchar(50) "
                "CHECK (Description in ( 'cash', 'cheque', 'credit card'))NOT NULL)")
def employee():
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(EmployeeID int identity (1,1) PRIMARY KEY, FirstName varchar(30) NOT "
                "NULL, LastName varchar(30) NOT NULL, Address varchar(50) NOT NULL, Phone varchar(50) NOT NULL, Title "
                "varchar(30) CHECK (Title in ( 'Executive', 'Senior Executive', 'Management Trainee', 'Event Manager', "
                "or 'Senior Event Manager') NOT NULL")
def event_type():
    cur.execute("CREATE TABLE IF NOT EXISTS EventType(EventTypeID int PRIMARY KEY, Description varchar(30) NOT NULL, "
                "ChangePerPerson int CHECK (ChangePerPerson > 0) NOT NULL)")
def events():
    cur.execute("CREATE TABLE IF NOT EXISTS Events(EventID int identity (1,1) PRIMARY KEY, EventName varchar(30) NOT NULL,"
                "EventType_ID int, FOREIGN KEY (EventType_ID) REFERENCES EventType(EventTypeID), Location varchar(30) NOT"
                " NULL, StartDate date CHECK (StartDate < EndDate AND StartDate > getDate()) NOT NULL, EndDate CHECK (EndDate > getDate()) date "
                "NOT NULL, StaffRequired int CHECK (StaffRequired>0) NOT NULL, Employee_ID int, "
                "FOREIGN KEY (Employee_ID) REFERENCES Employee(EmployeeID) ,Customer_ID int, FOREIGN KEY "
                "(Customer_ID) REFERENCES Customers(CustomerID) No_of_people int CHECK (NO_of_people >= 50)NOT NULL)")
def payments():
    cur.execute("CREATE TABLE IF NOT EXISTS Payments(PaymentID int identity (1,1) PRIMARY KEY, Event_ID int, "
                "FOREIGN KEY (Event_ID) REFERENCES Events (EventID), PaymentAmount int NOT NULL, PaymentDate date CHECK "
                "(PaymentDate <= StartDate AND PaymentDate >getDate()) NOT NULL, CreditCardNumber int, CardHoldersName "
                "varchar(30), CreditCardExpiryDate date CHECK (CreditCardExpiryDate > getDate) NOT NULL,"
                " PaymentMethod_ID int , FOREIGN KEY (PaymentMethod_ID) REFERENCES PaymentMethods (PaymentMethodID),"
                "  ChequeNo varchar (50))")
customers_solve = """
    INSERT INTO Customers VALUES (1, 'tomiwa', ' Moon crescent', 'Virginia', 'USA', '080-24-25-65-78') """
cur.execute(customers_solve)
payments_methodSolve = """
    INSERT INTO PaymentsMethods VALUES (1, 'cash') """
cur.execute(payments_methodSolve)
employee_solve = """
    INSERT INTO Employee VALUES (1, 'John', 'Okoro', ' 4 Lagos street Ikorodu', '080-43-54-67-87','Executive')
     """
cur.execute(employee_solve)
event_typeSolve = """
    INSERT INTO EventType VALUES (1, 2000, 'Birthday') """
cur.execute(event_typeSolve)
events_solve = """
    INSERT INTO Events VALUES (1, 'Tolu Birthday', 2000, 'ikeja', '2020-05-05', '2020-04-04', 200 ,50,2,60) """
cur.execute(events_solve)

payments_solve = """
    INSERT INTO Payments VALUES (1, 25, 21, 300, '2020-05-17', 2344656465785473, 'Ben', '2020-05-01', 'cash', 234323569854443) """
cur.execute(payments_solve)

cur.execute("SELECT Customer, Name, Address, City, State, Phone FROM Customers")
result1 = cur.fetchone()
print(result1)

cur.execute("SELECT PaymentMethodID , Description FROM PaymentMethods")
result2 = cur.fetchone()
print(result2)

cur.execute("SELECT EmployeeID, FirstName, LastName, Address, Phone, Title FROM Employee")
result3 = cur.fetchone()
print(result3)

cur.execute("SELECT EventTypeID, Description, ChangePerPerson FROM EventType")
result4 = cur.fetchone()
print(result4)

cur.execute("SELECT EventID , EventType_ID , Location, StartDate, EndDate, StaffRequired, Employee_ID, Customer_ID, No_of_people FROM Events")
result5 = cur.fetchone()
print(result5)

cur.execute("SELECT PaymentID, Event_ID, PaymentAmount, PaymentDate, CreditCardNumber, CardHoldersName, CreditCardExpiryDate, PaymentMethod_ID, ChequeNo  FROM Payments")
result6 = cur.fetchone()
print(result6)