from bintrees import RBTree

class BTreeMap:
    def __init__(self):
        self.tree = RBTree()

    def __getitem__(self, key):
        return self.tree[key]

    def __setitem__(self, key, value):
        self.tree[key] = value

    def __contains__(self, key):
        return key in self.tree

    def __delitem__(self, key):
        del self.tree[key]

    def __len__(self):
        return len(self.tree)
    
    def clear(self):
        self.tree.clear()  #очистка дерева

    def get(self, key, default=None):  #Метод get () возвращает значение по указанному ключу в параметрах.
        return self.tree.get(key, default)

    def setdefault(self, key, default=None):
        return self.tree.setdefault(key, default) #Метод setdefault() вернет значение словаря , соответствующее ключу key.Если указанный ключ key отсутствует, вставит его в словарь со значением default и вернет значение default. Если значение по умолчанию default не установлено и ключ отсутствует, метод вставит ключ в словарь со значением None, при этом никакое значение не возвращается.

    def pop(self, key):
        return self.tree.pop(key)  #Метод pop удаляет элемент по индексу и возвращает его. Если не указывать параметры, то будет удален последний элемент

    def items(self):
        return self.tree.items()

    def keys(self):
        return self.tree.keys()

    def values(self):
        return self.tree.values()

    def update(self, other):
        self.tree.update(other) #Метод update() обновляет/дополняет словарь с помощью пар ключ-значение из other, перезаписывая существующие ключи новыми значениями из other. Если ключ в словаре отсутствует, то он добавляется. Метод ничего не возвращает.

