# 📋Online Exam Registration portal System (python Tkinter Project)

## 📌 Project Description
Live Exams is a desktop-based Examination Registration System built using **Python Tkinter** and **MySQL**.  
The application allows students to register, verify email via OTP, fill personal & educational details, update information, and view their exam form.

This project demonstrates GUI development, database integration, and authentication handling in Python.

---

## 🚀 Features

- 🔐 User Registration & Login
- 📧 Email OTP Verification
- 🧑 Personal Details Form
- 📚 Educational Details Form
- 💾 MySQL Database Integration
- ✏️ Update User Information
- 👀 View Submitted Registration Form

---
## 🛠 Technologies Used

- Python
- Tkinter (GUI)
- MySQL

--- 

## 🔧 tools Used

- pycharm
- mySqlworkbench

---
## 🗄 Database Setup

1. Install MySQLWorkbanch
2. Create database:

```sql
CREATE DATABASE reg;
```
3.create table
```
CREATE TABLE reg1 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    password VARCHAR(50),
    aadharno VARCHAR(20),
    yourname VARCHAR(50),
    mobilenumber VARCHAR(15),
    address VARCHAR(200),
    gender VARCHAR(10),
    yourage VARCHAR(5),
    dateofbirth VARCHAR(20),
    fathername VARCHAR(50),
    institution VARCHAR(100),
    higherqualification VARCHAR(100),
    yearofpassing VARCHAR(10),
    nationality VARCHAR(50),
    mothertongue VARCHAR(50),
    otherlanguage VARCHAR(50),
    yourstate VARCHAR(50),
    yourcity VARCHAR(50)
);
```
3.connect the database to python:
-use database hostname,username,userpassword(create pass while open the database) and database name("reg").
```
"host='localhost',user='root',password='python',db='reg'"
```

---

## 💻Screenshots

### main Page
![main](images/home.png)









