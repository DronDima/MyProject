import mysql.connector


def getLinksToPosts(oldCount, newCount):
    count = newCount - oldCount
    mydb = sqlIn()
    cursor = mydb.cursor()
    result = []
    cursor.execute("SELECT link FROM posts ORDER BY dattime DESC LIMIT %s;", (count,))
    for row in cursor.fetchall():
        result.append(row[0])
    sqlOut(mydb)
    return result


def countOfRows():
    mydb = sqlIn()
    cursor = mydb.cursor()
    cursor.execute("SELECT id FROM posts;")
    results = cursor.fetchall()
    sqlOut(mydb)
    return len(results)


def writeData(data):
    input = []
    for d in data:
        input.append((d["title"], d["link"]))

    mydb = sqlIn()
    cursor = mydb.cursor()

    sql = "INSERT IGNORE INTO posts (title, link, dattime) VALUES(%s, %s, NOW());"

    cursor.executemany(sql, input)
    mydb.commit()

    sqlOut(mydb)

def sqlIn():
    mydb = mysql.connector.connect(
        host="localhost",
        user="dima",
        password="Admin.123",
        database="MyProject"
    )
    return (mydb)
def sqlOut(mydb):
    mydb.close()



