class Human:
    def __init__(self, name, height, weight) -> None:
        self.name = name
        self.height = height
        self.weight = weight
    
    def hello(self):
        print('name : ', self.name)
        print('height : ', self.height)
        print('weight : ', self.weight)
        print('!!!hello!!!')

yamada = Human('tanaka', 174, 75)
yoshida = Human('yoshida', 164, 55)

yamada.hello()
yoshida.hello()