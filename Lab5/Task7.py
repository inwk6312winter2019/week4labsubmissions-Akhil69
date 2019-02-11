class Kangaroo:
    def __init__(self, name, contents=None):
        self.name = name
        self.pouch_contents = contents or []

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch('function call')
roo.put_in_pouch('new wallet')
roo.put_in_pouch('new car keys')
roo.put_in_pouch('new function call')

print(kanga)
print(roo)
