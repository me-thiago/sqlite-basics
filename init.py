import sqlite3
from users import User

conn = sqlite3.connect('users')

c = conn.cursor()
c.execute("SELECT * FROM users")
total = c.fetchall()
new_id = len(total) + 1

def create_user(id, name, email):
    c.execute(f"INSERT INTO users VALUES (:id, :name, :email)", {'id':id, 'name':name, 'email':email})
    print(f'new user added')
print(f'total: {total}')
print(f'new_id: {new_id}')

name = input('enter name')
create_user(new_id, name, 'gi@test.io')
# c.execute("""CREATE TABLE users (
#           id integer primary key, 
#           name text not null,
#           email text not null
#           )""")

# c.execute("INSERT INTO users VALUES (3, 'thiago', 'thiago3@test.io')")
c.execute("SELECT * FROM users ")

print(c.fetchall())


conn.commit()

conn.close()