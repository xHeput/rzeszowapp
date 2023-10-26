CREATE DATABASE MyLIFE_CLINIC;

USE MyLIFE_CLINIC;

CREATE TABLE position (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(255) NOT NULL
);

CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    imie VARCHAR(50),
    nazwisko VARCHAR(70),
    numer_tel VARCHAR(15),
    postion_id INTEGER NOT NULL,
    FOREIGN KEY (postion_id) REFERENCES position (id)
);

CREATE TABLE medicine (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(255) NOT NULL
);

CREATE TABLE prescription (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(255) NOT NULL,
    created_at datetime default CURRENT_TIMESTAMP
);

CREATE TABLE prescription_medicine (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    medicine_id INTEGER NOT NULL,
    prescription_id INTEGER NOT NULL,
    FOREIGN KEY (medicine_id) REFERENCES medicine(id),
    FOREIGN KEY (prescription_id) REFERENCES prescription(id)
);

CREATE TABLE adress (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    miasto VARCHAR(50),
    wojewodztwo VARCHAR(50),
    kraj VARCHAR(50),
    ulica VARCHAR(50),
    numer_domu VARCHAR(50),
    numer_mieszkania VARCHAR(50),
    kod_pocztowy VARCHAR(50)
);

CREATE TABLE permissions (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(255) NOT NULL
);

CREATE TABLE permissions_employee (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    permissions_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (permissions_id) REFERENCES permissions(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

CREATE TABLE patient (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    imie VARCHAR(50),
    nazwisko VARCHAR(70),
    birth_date DATE,
    numer_tel VARCHAR(15),
    pesel VARCHAR(11),
    gender TINYINT(1),
    adress_id INTEGER NOT NULL,
    FOREIGN KEY (adress_id) REFERENCES adress(id)
);

CREATE TABLE permissions_patient (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    permissions_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    FOREIGN KEY (permissions_id) REFERENCES permissions(id),
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);

CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(255) NOT NULL,
    adress_id INTEGER NOT NULL,
    FOREIGN KEY (adress_id) REFERENCES adress(id)
);

CREATE TABLE hospital_referral (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    opis VARCHAR(255) NOT NULL,
    created_at datetime default CURRENT_TIMESTAMP
);
 
CREATE TABLE appointment (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    date_of DATE,
    opis VARCHAR(255) NOT NULL,
    hospital_referral_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    prescription_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (prescription_id) REFERENCES prescription(id),
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (hospital_referral_id) REFERENCES hospital_referral(id)
);
