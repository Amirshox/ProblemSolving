import requests
import mysql.connector

url = 'https://student-api.cambridgeonline.uz/v1/student/event/next'

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3N0dWRlbnQtYXBpLmNhbWJyaWRnZW9ubGluZS51ei92MS9hdXRoL2xvZ2luIiwiaWF0IjoxNjc2NzUyMDA3LCJleHAiOjE2NzY3NTU2MDcsIm5iZiI6MTY3Njc1MjAwNywianRpIjoiOEJ6VHFFeGVGaGpsOFZ5VCIsInN1YiI6IjYzODUzIiwicHJ2IjoiMjFmMThjZjQ1NDEwMzI5NTQ1YTYzNDA5YTIyZTQ4MGU2NjRiNzllZiJ9.LO4qpg6RtxAvMJ_GrKJAC0LgMW-Hhle7VgFmecfCTUs"
}

conn = mysql.connector.connect(
    host="localhost",
    database="leetcode",
    user="admin",
    password="1"
)

cursor = conn.cursor()


def get_students():
    response = requests.get(url, headers=headers)
    return response.json()['data'][0]['students']


def exists(id):
    sql_script_if_exists = "SELECT EXISTS(SELECT * FROM students_of_cambridge WHERE id = %s)" % id
    cursor.execute(sql_script_if_exists)
    result = cursor.fetchone()[0]
    return bool(result)


def insert_to_table(**kwargs):
    sql_script_insert = 'INSERT INTO students_of_cambridge(' \
                        'id, first_name, last_name, phone_number, gender, photo, birth_date)' \
                        'VALUES (' \
                        f'{kwargs["id"]},' \
                        f"'{kwargs['first_name']}'," \
                        f"'{kwargs['last_name']}'," \
                        f"'{kwargs['phone_number']}'," \
                        f"'{kwargs['gender']}'," \
                        f"'{kwargs['photo']}'," \
                        f"'{kwargs['birth_date']}'" \
                        ')'

    try:
        cursor.execute(sql_script_insert)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def update_to_table(**kwargs):
    sql_script_update = "UPDATE students_of_cambridge SET " \
                        f"first_name={kwargs['first_name']}, " \
                        f"last_name={kwargs['last_name']}, " \
                        f"phone_number={kwargs['phone_number']}, " \
                        f"gender={kwargs['gender']}, " \
                        f"photo={kwargs['photo']}, " \
                        f"birth_date={kwargs['birth_date']}" \
                        f" WHERE id={kwargs['id']}"
    try:
        cursor.execute(sql_script_update)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    students = get_students()
    for student in students:
        id = student['id']
        first_name = student['name']
        last_name = student['surname']
        phone_number = student['phone']
        gender = student['gender']
        photo = student['photo']
        birth_date = student['date_of_birth']
        if exists(id):
            update_to_table(
                id=id,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                gender=gender,
                photo=photo,
                birth_date=birth_date
            )
        else:
            insert_to_table(
                id=id,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                gender=gender,
                photo=photo,
                birth_date=birth_date
            )


if __name__ == '__main__':
    main()
