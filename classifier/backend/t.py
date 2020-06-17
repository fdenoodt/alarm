class Calculator:
    ik = 'hi'
    print("cool")

    @staticmethod
    def addNumbers():
        return Calculator.ik


print('Product:', Calculator.addNumbers())
print('Product:', Calculator.addNumbers())

##
