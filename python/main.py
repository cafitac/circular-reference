class A:
    def __init__(self, name):
        print("init")
        self.name = name
        self.parent = None
        self.children = set()

    def __del__(self):
        print("delete", self.name)

    def add(self, child):
        self.children.add(child)


if __name__ == '__main__':
    a = A("1")
    b = A("2")
    b.parent = a
    a.parent = b

    print("end")


"""
print 결과
-----------
init
init
end
delete 1  # 순환 참조로 인해 __del__ 함수의 실행 여부가 보장되지 않음 (해당 코드에서는 호출된 모습)
delete 2  # 순환 참조로 인해 __del__ 함수의 실행 여부가 보장되지 않음 (해당 코드에서는 호출된 모습)
"""
