class VirtualEnvironment:
    def __init__(self):
        self._variables = {}

    def set_var(self, name, value):
        self._variables[name] = value
    
    def get_var(self, key):
        return self._variables[key]
    
env = VirtualEnvironment()
env.set_var("x", 10)
x = 5
print(x)
print(env.get_var("x"))