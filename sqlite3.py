import sqlite3
vt = sqlite3.connect('utopian.sqlite')
sv = vt.cursor()
sv.execute("CREATE TABLE utopianio (name, last name)")
veri_gir = """INSERT INTO utopianio VALUES ('john', 'Brayn')"""
sv.execute(veri_data)
sv.commit()
data = sv.fetchall()
print(data)
