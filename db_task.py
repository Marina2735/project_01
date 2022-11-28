import sqlite3

connection = sqlite3.connect('students.db')

cursor = connection.cursor()
query_table = """CREATE TABLE Students 
(
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query_table)
connection.commit()

cursor = connection.cursor()
query_details = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);
"""
cursor.execute(query_details)
connection.commit()

def get_students_details(Student_Id):
    try:
      connection = sqlite3.connect('students.db')
      cursor = connection.cursor()
      select_query = """SELECT * FROM Students WHERE Student_id = ?"""
      cursor.execute(select_query, (Student_Id,))
      records = cursor.fetchall()
      for row in records:
        print("Student_Id", row[0])
        print("Student_Name", row[1]) 
        print("School_Id", row[2])
      connection.close()
    except (Exception, sqlite3.Error) as error:
      print ('Ошибка в получении данных', error)
connection.close()
get_students_details(202)
print ("\n")