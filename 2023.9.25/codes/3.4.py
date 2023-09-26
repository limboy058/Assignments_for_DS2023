class My_node():

    def __init__(self, val):
        self.value = val
        self.next = None


class My_list_head():

    def __init__(self):
        self.value = 0
        self.next = None

    def empty(self):
        return self.value == 0

    def length(self):
        return self.value

    def insert(self, idx, val):
        if idx < 0 or idx > self.length():
            print('IndexError')
            return

        it = self.next
        cnt = 0
        pre = self
        now = My_node(val)

        while cnt != idx:
            if cnt == idx - 1:
                pre = it
            it = it.next
            cnt += 1

        pre.next = now
        now.next = it
        self.value += 1

    def erase(self, idx):
        if idx < 0 or idx >= self.length():
            print('IndexError')
            return
        cnt = 0
        it = self.next
        pre = self
        while cnt != idx:
            if cnt == idx - 1:
                pre = it
            it = it.next
            cnt += 1
        pre.next = it.next
        self.value -= 1

    def change(self, idx, val):
        if idx < 0 or idx >= self.length():
            print('IndexError')
            return

        it = self.next
        cnt = 0

        while cnt < idx:
            it = it.next
            cnt += 1
        it.value = val

    def items(self):
        it = self
        while it.next != None:
            it = it.next
            yield it.value

    def find(self, val):
        return val in self.items()


lis = My_list_head()
print(lis.length(), list(lis.items()))
print()

lis.insert(-1, 1212)
print(lis.length(), list(lis.items()))
print()

lis.insert(0, "92182")
print(lis.length(), list(lis.items()))
print()

lis.insert(1, 123)
print(lis.length(), list(lis.items()))
print()

lis.insert(1, 444)
print(lis.length(), list(lis.items()))
print()

lis.insert(10, 999)
print(lis.length(), list(lis.items()))
print()

print(lis.find(444))
print()

lis.erase(2)
print(lis.length(), list(lis.items()))
print()

lis.erase(2)
print(lis.length(), list(lis.items()))
print()

lis.change(0, 000)
print(lis.length(), list(lis.items()))
print()

lis.change(2, 3948)
print(lis.length(), list(lis.items()))
print()
