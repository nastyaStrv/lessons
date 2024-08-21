def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function() #Работает
inner_function() #NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                 #Является ошибкой т.к. разные пространства имен. Мы не можем достать функцию которая находится внутри функции.