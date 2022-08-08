import sqlite3
import csv

conn = sqlite3.connect('unifespSubjects.db')
cur = conn.cursor()

def create_database(conn, cur):
        cur.execute("""
        CREATE TABLE if not exists ucs
        (
            id                  unique primary key,
            subjectName         varchar(50),
            category            varchar(50),
            chTotal             int,
            requirements        varchar(300),
            semesterAvailable   varchar(25)
        )
        """)
        conn.commit()

        cur.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS
            temp_line_index on ucs (subjectName)
        """)

def process_file(conn, cur, filename):
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(csv.reader(f), None)


        for entry in reader:
            try:
                print(reader.line_num)
                record = (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5])

                # build SQL Insert statement with placeholders
                stmt = "INSERT INTO ucs(id, subjectName, category, chTotal, requirements, semesterAvailable)";
                stmt += "values(?, ?, ?, ?, ?, ?)"

                # execute statement with tuple data
                cur.execute(stmt, record)

                if cur.lastrowid % 268 == 0:
                    conn.commit()

            except csv.Error as e:
                print(f"line: {reader.line_num}, Record:{record}")

create_database(conn, cur)
process_file(conn, cur, '/Users/lewdamy/my-projects/fix_unifesp/csvFiles/Materias-Unifesp-Atualizada.csv')
conn.commit()
conn.close()
print("Job Complete")

