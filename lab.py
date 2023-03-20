from bintrees import FastBinaryTree

class btree_map:
    def __init__(self):
        self.tree = FastBinaryTree() # создаем пустое дерево
        self.size = 0 # определяем начальный размер дерева

    def __len__(self):
        return self.size # возвращаем размер дерева

    def __getitem__(self, key):
        return self.tree.get(key) # получаем значение по ключу

    def __setitem__(self, key, value):
        self.tree.insert(key, value) # устанавливаем новое значение для ключа

    def __delitem__(self, key):
        self.tree.remove(key) # удаляем пару ключ-значение по ключу

    def __contains__(self, key):
        return key in self.tree # проверяем, содержит ли дерево ключ

btmap = btree_map() # создаем новый btree_map

# добавляем новую пару ключ-значение
btmap['dog'] = 'собака'
btmap['cat'] = 'кошка'
btmap['bird'] = 'птица'

# получаем значение по ключу
print(btmap['dog']) 

# изменяем значение по ключу
btmap['cat'] = 'пантера'
print(btmap['cat']) 

# удаляем пару ключ-значение по ключу
del btmap['bird']

# проверяем, содержит ли дерево ключ
print('cat' in btmap) 
print('bird' in btmap) 

# получаем размер дерева
print(len(btmap)) 