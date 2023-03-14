import sqlite3
import asyncio


conn = sqlite3.connect('../../res/db/users.db')
cursor = conn.cursor()

async def user_exist_check(user_id):
    result = 0
    query = f'SELECT user_id FROM users WHERE user_id={str(user_id)}'
    try:
        cursor.execute(query)
        if cursor.fetchall()[0][0] == user_id:
            print(cursor.fetchall()[0][0])
            result = 200
        cursor.close()
    except IndexError as e:
        print(e)
        result = 400
    return await result

def user_add(user_id):
    query = f'INSERT INTO users (user_id) VALUES ({str(user_id)})'
    cursor.execute(query)
    conn.commit()

#user_add('4321')
#print(user_exist_check('4321'))