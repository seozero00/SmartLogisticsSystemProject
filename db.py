import pymysql
from ignore import user, password, db


def dbConn():
    connect = pymysql.connect(
        host='localhost', 
        user=user, 
        password=password, 
        db=db, 
        charset='utf8mb4',
        )
    return connect
    
def dbInsert(sql, conn):

    #Insert Query
    # sql = f"INSERT INTO PACKAGES (id, name, dest, root) VALUES ({id}, {name}, {dest}, {root});"

    conn.cursor().execute(sql)
    conn.commit()

def dbSelect(sql, conn):
    # Select Query
    # cur.execute("SELECT id, name, arrive, dest, root FROM PACKAGES")
    cur = conn.cursor()
    cur.execute(sql)
    # row = cur.fetchone()

    # while row:
    #     print("id : " + str(row[0]) + ", name : " + str(row[1]) + ", arrive : " + str(row[2]) + ", dest : " + str(row[3]) + ", root : " + str(row[4]))
    #     row = cur.fetchone()
    # print()
    
    return cur

def dbDisconnect(conn):
    conn.close()

def resultPrt(cur):
    row = cur.fetchone()
    #cur.fetchall()
    
    while row:
        print(row)
        row = cur.fetchone()
        
def nodeInit(cur):
    dic = dict()
    rows = cur.fetchall()
    for row in rows:
        if not row[0] in dic:
            dic[row[0]] = dict()
            
        if not row[1] in dic:
            dic[row[1]] = dict()
            
        dic[row[0]][row[1]] = row[2]
        dic[row[1]][row[0]] = row[2]
    
    # print(dic)
    # print()
    
    print("===========gragh===========")
    for k in dic.keys():
        print(f"{k} : {dic[k]}")
    print("===========================")
        
    return dic
    

# conn = dbConn()

# sql = "INSERT INTO PACKAGES (id, name, arrive, dest) VALUES (1124, 'jjung', 'A', 'I');"
# dbInsert(sql, conn)
# sql = "SELECT id, name, arrive, dest, root FROM PACKAGES"
# dbSelect(sql, conn)

# Init Node(db hubs -> gragh)
# sql = "SELECT name, dest, weight FROM HUBS"
# cur = dbSelect(sql, conn)
# graph = nodeInit(cur)

# dbDisconnect(conn)
