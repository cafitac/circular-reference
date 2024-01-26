class A:
    def __init__(self):
        print("init")

    def __del__(self):
        print("delete")


if __name__ == '__main__':
    a = A()
    print("end")


"""
print 결과
-----------
init
end
delete
"""
