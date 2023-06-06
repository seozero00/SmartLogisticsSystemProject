from db import dbConn, dbSelect, nodeInit, dbDisconnect, dbInsert
from dijkstra import dijkstra, full
# from define import hubs, routes
from client import sockctConn, client
from collections import deque

hubs = {
    'A': deque(maxlen=5),
    'B': deque(maxlen=5),
    'C': deque(maxlen=5),
    'D': deque(maxlen=5),
    'E': deque(maxlen=5),
    'F': deque(maxlen=5),
    'G': deque(maxlen=5),
    'H': deque(maxlen=5),
    'I': deque(maxlen=5),
}

#DB Connect
conn = dbConn()

#Socket Connect
client_socket = sockctConn()

#Init Node(db hubs -> gragh)
sql = "SELECT name, dest, weight FROM HUBS"
cur = dbSelect(sql, conn)
graph = nodeInit(cur)


while True:
    data = client(client_socket)
    
    if data[1] == 'quit':
        print("quit")
        break
    
    print(f"received data : {data}")
    id = data[0]
    pkgName = data[1] #Package Name
    destHub = data[2] #Destination Hub
    
    #dijkstra with received data
    result = dijkstra(graph, destHub, hubs) #[weight, [route]]
    # route = result[1] #optimization route
    
    # routes[pkgName] = result[1]
    
    print(f'Result : {result}')
    # print(f'Routes : {routes}')
    
    route = '-'.join(result[1])
    
    #save packag information - id, name, dest, route
    sql = f"INSERT INTO PACKAGES (id, name, dest, root) VALUES ({id}, '{pkgName}', '{destHub}', '{route}');"
    dbInsert(sql, conn)
    
    current = result[1][0]  # 물류의 현재 허브 위치
    full(hubs, current, id, conn) #check if queue is full
    
    print()
    print(f'Hubs : {hubs}')
    
    print()
    print('--------------------------------------------')
    
    #STOP while when there's problem
    pass

#DB Disconnect
dbDisconnect(conn)
client_socket.close()
