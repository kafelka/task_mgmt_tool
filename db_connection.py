import sqlite3


def create_table(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS task_management(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, status TEXT, important BOOLEAN, date TEXT)")
    conn.commit()
    c.close()
    

def add_task(conn, name, description, status, important, date):
    c = conn.cursor()
    c.execute('''INSERT INTO task_management(name, description, status, important, date) 
        VALUES(?, ?, ?, ?, ?)''',
        (name, description, status, important, date))
    conn.commit()
    c.close()
    

def delete_task(conn, id):
    c = conn.cursor()
    c.execute('DELETE FROM task_management WHERE id = ?', (id,))
    conn.commit()
    c.close()
    
    
def update_task(conn, id, name, description, status, important, date):
    c = conn.cursor()
    c.execute('''UPDATE task_management
               SET name=?, description=?, status=?, important=?, date=?
               WHERE id=?''',
               (name, description, status, important, date, id))
    conn.commit()
    c.close()
    
        
def get_all_tasks(conn):
    c = conn.cursor()
    c.execute('SELECT id, name, description, status, important, date FROM task_management ORDER BY date')
    columns = ["id", "name", "description", "status", "important", "date"]
    result = [dict(zip(columns, row)) for row in c.fetchall()] #combines two lists into a list of tuples
#    print(result)
    c.close()
    return result
    

# get_tasks_for_date(conn, date)
def get_tasks_for_date(conn, date):
    c = conn.cursor()
    c.execute(('SELECT * FROM task_management WHERE date=?'), (date,))
    columns = ["id", "name", "description", "status", "important", "date"]
    result = [dict(zip(columns, row)) for row in c.fetchall()]
#    print(result)
    c.close()
    return result

# get_tasks_between_dates(conn, from_date, to_date)
def get_tasks_between_dates(conn, from_date, to_date):
    c = conn.cursor()
    c.execute(('SELECT * FROM task_management WHERE date BETWEEN ? AND ?'),(from_date, to_date,))
    columns = ["id", "name", "description", "status", "important", "date"]
    result = [dict(zip(columns, row)) for row in c.fetchall()]
#    print(result)
    c.close()
    return result

def get_task_by_id(conn, id):
    c = conn.cursor()
    c.execute(('SELECT * FROM task_management WHERE id=?'),(id,))
    columns = ["id", "name", "description", "status", "important", "date"]
    result = [dict(zip(columns, row)) for row in c.fetchall()]
#    print(result)
    c.close()
    return result



if __name__ == "__main__":
    conn = sqlite3.connect("task_management.db")
    create_table(conn)
    conn.close()
