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

### main page
<img width="500" height="500" alt="Screenshot (29)" src="https://github.com/user-attachments/assets/7c745788-7165-4f2e-900b-4292f3cd6038" /> <img width="500" height="500" alt="Screenshot (30)" src="https://github.com/user-attachments/assets/538fd214-3632-4f7c-84c1-ea51bc686a68" />

### mail varification and regisration pages
<img width="500" height="500" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/08895917-703c-468d-a9c5-b1c0c56b14d8" /> <img width="500" height="500" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/bd4e48fa-6ef4-4f6b-be7c-334b72f0deba" />

### personal and other-detials page 
<img width="500" height="500" alt="Screenshot (33)" src="https://github.com/user-attachments/assets/c52f8b94-e22d-4a07-b1fd-f4bb6e6bf022" /> <img width="500" height="500" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/a46a5f1a-4b1b-4a63-94e3-e2edb557602f" />

## form page
<img width="500" height="500" alt="Screenshot (36)" src="https://github.com/user-attachments/assets/c3d17381-8dda-49f3-9624-d55a0ad39be8" /> <img width="500" height="500" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/637d7b16-a5b2-4645-afb1-5d42bbf8867a" />

## login and user-home page
<img width="500" height="500" alt="Screenshot (38)" src="https://github.com/user-attachments/assets/b8cd6d9e-13d6-4b40-a6c8-2bc94e3b7aa3" /> <img width="500" height="500" alt="Screenshot (39)" src="https://github.com/user-attachments/assets/f5f98f5f-a7ea-4dec-984a-877ae3f604fd" />

### personal ,other-details and form page
<img width="500" height="500" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/349d8713-ce52-48dd-bf76-ca7e1dcf1166" /> <img width="500" height="500" alt="Screenshot (42)" src="https://github.com/user-attachments/assets/2c919a7d-47d1-4501-9e1b-239e176e541d" />
<img width="500" height="500" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/c4390da7-9443-48f2-be3c-78960716ec45" />

-with the help of login we all retrive and update our data 




