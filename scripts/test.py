def function1():
    print("invoking function1")
    import pdb; pdb.set_trace()
    print("function1 invoked")


def function2():
    print("invoking function2")
    function1()
    print("function2 invoked")


def function3():
    print("inside function3")
    function2()
    print("function3 invoked")


# starting the call with function2()

function3()