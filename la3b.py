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

    def clear(self):
        self.tree.clear()

    def get(self, key, default=None):
        return self.tree.get(key, default)

    def setdefault(self, key, default=None):
        return self.tree.setdefault(key, default)

    def pop(self, key):
        return self.tree.pop(key)

    def items(self):
        return self.tree.items()

    def keys(self):
        return self.tree.keys()

    def values(self):
        return self.tree.values()

    def update(self, other):
        self.tree.update(other)

    def __len__(self):
        return len(self.tree)

# Создаем новый контейнер
btree_map = BTreeMap()

# Добавляем пары ключ-значение в контейнер
btree_map[1] = "one"
btree_map[2] = "two"
btree_map[3] = "three"

# Получаем значение по ключу
print(btree_map[2]) # "two"

# Изменяем значение по ключу
btree_map[2] = "new two"
print(btree_map[2]) # "new two"

# Добавляем новую пару ключ-значение
btree_map[4] = "four"
print(btree_map[4])
# Удаляем пару ключ-значение по ключу
del btree_map[1]
