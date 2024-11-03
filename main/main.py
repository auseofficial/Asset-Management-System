

conn = psycopg2.connect(
    host="localhost",
    dbname="postgress",  
    user="postgres",
    password="1234",  
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS person (r
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR
    );
""")

conn.commit()
cur.close()
conn.close()
