

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity # calls setter '@capacity' method
        self.cookie_jar = []

    def __str__(self):
        # self.size calls '@property for size()
        return self.size * "🍪"

    def deposit(self, n): # n arguiment comes from user
        for _ in range(n):
            self.cookie_jar.append("🍪")
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        for _ in range(n):
            self.cookie_jar.pop()
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity): # 'capacity' comes from the programmer or user; from __init__()
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return len(self.cookie_jar)

jar = Jar()

jar.deposit(5)
print(jar)
jar.withdraw(2)
print(jar)



# Note that it’s not as easy to test instance methods as it is to test functions
# alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables).
# To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit).
# But the method you call first might itself not be correct!

# And so programmers sometimes mock (i.e., simulate) state when testing methods, as
# with Python’s own mock object library, so that you can call just the one method
# but modify the underlying state first, without calling the other method to do so.

# For simplicity, though, no need to mock any state. Implement your tests as you normally would!