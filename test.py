
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
    
