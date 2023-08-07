# #3.4.4
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json

js = json.loads(input()) #считываем словарь
#сериализуем его в джейсон структуру, как строку
sp = {element["name"]: []for element in js}

for k in js:
    for l in sp:
        if l in k['parents']:
            sp[l].append(k['name'])

for e in sp:
    sp[e] = set(sp[e])
         
def dfs(graph, start, visited=None): #Функция обхождения вершин графа по алгоритму dfs
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for e in sorted(sp.keys()):
    print(e, ':', len(dfs(sp, e)))

    


