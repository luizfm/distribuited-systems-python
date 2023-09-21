class SimpleCache:
    # Constructor: Passing self object and a property called cache
    def __init__(self): 
        self.cache = {}

    # the get method receives the self object by default, and when called external, it receives only the dynamic value
    def get(self, key):
        return self.cache.get(key, None)
    
    # The set method receives the self object by default and when called external, key and value should be provided
    def set(self, key, value):
        self.cache[key] = value

cache = SimpleCache()
cache.set('a', 1)
print(cache.get('a'))