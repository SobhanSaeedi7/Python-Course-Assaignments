import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()

    
    def get_tasks(self):
        query = "SELECT * FROM tasks ORDER BY is_done"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    
    def add_new_task(self, new_title, new_description, new_datetime, new_priority):
        try:
            query = f"INSERT INTO tasks(title, description, datetime, priority) VALUES('{new_title}', '{new_description}', '{new_datetime}', {new_priority})"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    
    def remove_task(self, id):
        # try:
            query = f"DELETE FROM tasks WHERE id={id}"
            self.cursor.execute(query)
            self.con.commit()
        #     return True
        # except:
        #     return False

    
    def task_done(self, task_id, is_done_task):
            if is_done_task == 0:
                is_done = 1
            else:
                is_done = 0
            query = f"UPDATE tasks SET is_done= {is_done} WHERE id={task_id};"
            self.cursor.execute(query)
            self.con.commit()


