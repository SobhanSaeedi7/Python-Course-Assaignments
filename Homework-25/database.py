import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("alarms.db")
        self.cursor = self.con.cursor()

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_new_task(self, new_title, new_hour, new_min):
        try:
            query = f"INSERT INTO alarms(title, hour, min) VALUES('{new_title}', {new_hour}, {new_min})"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def update(self, id, title, hour, min):
        try:
            query = f"UPDATE alarms SET title= '{title}' , hour= {int(hour)} , min= {int(min)} WHERE id= {int(id)}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def is_on(self, id, is_on):
        try:
            if is_on == 0:
                is_on = 1
            else:
                is_on = 0
            query = f"UPDATE alarms SET is_on={int(is_on)} WHERE id={int(id)};"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def remove(self, id):
        try:
            query = f"DELETE FROM alarms WHERE id={int(id)}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
