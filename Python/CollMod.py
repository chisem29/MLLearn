import collections

s = "Helloeee"
c = collections.Counter(s)

c.subtract(collections.Counter("wwwH")) # уменьшает количество значений у каждего элемента под ключом

'''m = {} // реализация методов values и keys у Counter
for i in set(s) :
    m[i] = s.count(i) '''

print(c.values(), ":", c.keys())

print(c.most_common(3)) # выведет tuple, в которых содержатся ключи и их значения по порядку до n

od =  collections.OrderedDict() #обычный dict, за исключением одного - запоминает порядок вставки значений, от него зависит порядок вывода
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['a'] = 5
for a, b in od.items() :
    print(a, b)

dd = collections.defaultdict(int) # автоматически создает переменную вместо вызова KeyError, key в формате int
dd[1] += 15
print(dd)

chm = collections.ChainMap({"username" : "Chisem", "password" : "123qwdqwad2"}, {"email" : "sosiska100@gmail.eu", "age" : 17}) # обьединяет dict в один

print(f'My name is {chm["username"]}. I`m {chm["age"]} years old.')

nmdt = collections.namedtuple("Human", ["name", "gender", "age"])

Gman = nmdt("Rayan", "male", 20)

print(Gman[0], Gman.gender) 

deq = collections.deque([1, 2, 3, 4, 5, 6])

deq.rotate(2) # сдвига на два элемента вправо

deq.popleft() # удаленный с начала списка элемент

deq.appendleft(7) # добавление элемента в начало списка 

print(deq)

# обьекты UserDict, UserList, UserString для создания пользовательского класса на основе наследия их, в котором будут модифицированные или добавленные пользователем методы

class MyString(collections.UserString) :
    def append(self, s : str) :
        self.data += s

myStr = MyString("Sel")
myStr.append("in")
print(myStr.data)