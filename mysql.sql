CREATE TABLE users
(
   ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
   username varchar(255),
   password varchar(255),
   mail varchar (255),
   rank  ENUM ('Fresh meat', 'Intern','Janitor','Lieutenant','Supreme being') DEFAULT 'Fresh meat',
);