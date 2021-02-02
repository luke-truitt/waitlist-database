import psycopg2

conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = "rocknroll",
            host = "127.0.0.1",
            port = "3306"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM ")
        order_items = cur.fetchall()
        cur.close()
        conn.close()