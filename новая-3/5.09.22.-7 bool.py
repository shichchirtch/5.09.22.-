class City:
    def __init__(self, name:str):
        # self.name = name.title()
        self.name = " ".join(x.title() for x in name.split())
    def __str__(self):
        return self.name
    def __bool__(self):
        return self.name[-1] not in ("a", "e", "i", "o", "u")


d  = City("tbilici mchet")
print(d.name)
print(bool(d))
print(d.n)
