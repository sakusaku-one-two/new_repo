
class A:
    @classmethod
    def show(cls):
        print(
            cls.__name__
        )

class B(A):
    pass

class C(B):
    pass


def subclasses(cls)->type:
    yield cls
    for subclass in cls.__subclasses__():
        yield from subclasses(subclass)




for cls in subclasses(A):
    cls.show()


gen = subclasses(A)

gen.__next__()

for sub in gen:
    sub.show()


try:
    next = gen.__next__()
except :
    pass
finally :
    print(next)
    
    
    
