def pipeline():
    graph = {}
    function = {}
    def decorator(depends_on=None):
        if depends_on is None:
            depends_on = []
        def register(func):
            graph.update({func.__name__: depends_on})
            def inner():
                for point in graph[func.__name__]:
                    function[point]()
                return func()
            function.update({func.__name__: inner})
            return inner
        if callable(depends_on):
            return decorator()(depends_on)
        return register
    return decorator


# def test_example() -> None:
#     register = pipeline()
#
#     answer = []
#
#     @register
#     def step1():
#         answer.append(1)
#
#     @register(["step1"])
#     def step2():
#         answer.append(2)
#
#     @register(["step1", "step2"])
#     def step3():
#         answer.append(3)
#
#     step3()
#     print(answer)
#
#
# test_example()