class A:
    def __init__(self, name):
        print("init")
        self.name = name
        self.children = set()

    def __del__(self):
        print("delete", self.name)

    def add(self, child):
        self.children.add(child)


if __name__ == '__main__':
    a = A("1")
    b = A("2")
    a.add(b)
    print("end")


"""
print 결과
-----------
init
init
end
delete 1
delete 2
"""
