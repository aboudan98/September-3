class AlwaysTrueWhenCompared:
    # We change the __eq__ method to always return true so everytime the equality check is called
    # it returns true
    def __eq__(self, other):
        return True

def equals():
    return AlwaysTrueWhenCompared()

# comparing anything to equals will return true because we changed the dunder method __eq__
print(equals() == 0)
print(equals() == [])
print(equals() == (lambda: 1))
print(equals() == 'nothing')
print(equals() == '')