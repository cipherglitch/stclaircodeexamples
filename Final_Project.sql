--
--This is the SQL code for my final project.
--
CREATE DATABASE CLOTHING_STORE;
--This creates the database itself.
--
--This line switches to the CLOTHING_STORE database
--
USE CLOTHING_STORE;
--
--These next lines create the 'Customer' table.
--
CREATE TABLE Customer(
CustNumber int(11) unique not null,
CustFirstName char(20),
CustLastName char(20) not null,
CustAddressLine1 char(50),
CustAddressLine2 char(50),
CustCity char(20),
CustState char(5),
CustZIPCode char(10),
CustPhone int(11),
CustEmail char(50)
PRIMARY KEY(CustNumber));
--
--These lines insert data into the 'Customer' table
--
INSERT INTO Customer VALUES
(1,'Scot','StClair','PO Box 713',null,'High Springs','FL','32655',3525551212,'scotstclair@gmail.com'),
(2,'Angie','Cowart','PO Box 713',null,'High Springs','FL','32655',3525551212,'angiecowart@aol.com'),
(3,'Chad','Thompson','123 Any St',null,'Gainesville','FL','32601',3525551212,'chadthompson@gmail.com'),
(4,'Jerry','Johnson','743 Main St',null,'Ocala','FL','34474',3525551212,'thebombdon@ymail.com'),
(5,'Christina','Marcheck','645 Spruce Creek Dr',null,'Alachua','FL','32615',3525551212,'ricososmooth@yowser.com');
--
--These lines create the 'Vendor' table
--
CREATE TABLE Vendor (
VendorNumber int(11) unique not null,
VendorName char(20),
VendorAddress1 char(50),
VendorAddress2 char(50),
VendorCity char(20),
VendorState char(5),
VendorZIP char(10),
VendorPhone int(11),
VendorAcctNumber int(11),
VendorTerms char(20),
VendorAcctContact char(20),
VendorContactEmail char(50)
PRIMARY KEY(VendorNumber));
--
--These lines insert data into the 'Vendor' table
--
INSERT INTO Vendor VALUES
(1,'T-Shirts R Us','123 Main St',null,'Albuquerque','NM','87101',5055551212,123456789,'Net 15','Joe Young','young.joe@tsru.com'),
(2,'Easy Shirt Design','764 W 42nd St',null,'New York','NY','10101',2125551212,123456789,'Net 30','Angus Young','ayoung@easyshirt.com'),
(3,'Shirt Off My Back','112 Mission St',null,'San Francisco','CA','94101',6285551212,123456789,'Net 15','Jim Morrison','lightmyfire@shirtback.com'),
(4,'Speedy T-Shirts','610 Syracuse St',null,'Athens','GA','30601',7065551212,123456789,'Net 30','David McFeely','dmcfeely@misterrogers.com'),
(5,'Radical Threads','420 Santa Monica Blvd',null,'Los Angeles','CA','90067',3235551212,123456789,'Net 30','Spliff Masterson','righteous@marley.com');
--
--These next lines create the 'Inventory' table
--
CREATE TABLE Inventory (
ItemNumber int(11) unique not null, 
Description char(200),
VendorNumber int(11),
ItemSize char(5),
Quantity int(4),
Cost decimal(5,2),
PRIMARY KEY(ItemNumber),
FOREIGN KEY (VendorNumber)
REFERENCES Vendor(VendorNumber));
--
--These lines insert data into the 'Invetory' table
--
INSERT INTO Inventory VALUES
(1,'T-Shirt',3,'S',30,11.99),
(2,'T-Shirt',5,'XL',50,12.99),
(3,'T-Shirt',2,'M',50,11.99),
(4,'T-Shirt',1,'XXL',60,13.99),
(5,'T-Shirt',4,'L',50,12.99);
--
--These lines will create the 'Orders' table
--
CREATE TABLE Orders (
--Had to name table 'Orders' as 'Order' is a protected word
OrderNumber int(11) unique not null,
CustNumber int(11) not null,
ItemNumber int(11) not null,
Quantity int(4),
Description char(200),
ItemSize char(5),
PriceEach decimal(5,2),
ExtendedPrice decimal(6,2),
Tax decimal(5,2),
Total decimal(7,2),
PaymentMethod char(20),
PaymentDetails char(30),
PRIMARY KEY(OrderNumber),
FOREIGN KEY(CustNumber)
REFERENCES Customer(CustNumber),
FOREIGN KEY(ItemNumber)
REFERENCES Inventory(ItemNumber));
--
--These lines will input data into the 'Orders' table.
--
INSERT INTO Orders VALUES
(1,2,3,2,'T-Shirt','M',19.99,39.98,2.8,42.78,'Visa',1234567890123456),
(2,1,5,1,'T-Shirt','L',19.99,19.99,1.4,21.39,'MC',1234567890123456),
(3,3,2,2,'T-Shirt','XL',19.99,39.98,2.8,42.78,'DSC',1234567890123456),
(4,5,1,1,'T-Shirt','S',19.99,19.99,1.4,21.39,'AMEX',1234567890123456),
(5,4,4,1,'T-Shirt','XXL',19.99,19.99,1.4,21.39,'Visa',1234567890123456);

--
--These lines will create the 'SupplyOrders' table
--
CREATE TABLE SupplyOrder (
SupplyOrderNumber int(11) unique  not null,
VendorNumber int(11) not null,
ItemNumber int(11) not null,
Quantity int (4),
Cost decimal(5,2),
SupOrderTotal decimal(6,2),
PRIMARY KEY(SupplyOrderNumber),
FOREIGN KEY(VendorNumber)
REFERENCES Vendor(VendorNumber),
FOREIGN KEY(ItemNumber)
REFERENCES Inventory(ItemNumber));
--
--These lines will insert data into the 'SupplyOrder' table
--
INSERT INTO SupplyOrder VALUES
(1,5,3,15,11.99,179.85),
(2,3,4,20,13.99,279.80),
(3,2,5,30,12.99,389.70),
(4,1,1,20,11.99,239.80),
(5,4,2,15,12.99,194.85);
