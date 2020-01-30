# Implement a cat and dog queue for an animal shelter.

class AnimalShelter:
    def __init__(self):
        self.h = None
        self.t = None

    def enqueue(self, a):
        if not self.h:
            self.h = a
            self.t = a
        else:
            # self.h.next = a
            self.t.next = a
            self.t = a

    def dequeueAny(self):
        if self.h:
            o = self.h.data
            self.h = self.h.next
            return o
        else:
            self.t = self.h

    def dequeueAnimal(self, tp):
        if not self.h:
            return

        # in head is dog
        if isinstance(self.h, tp):
            o = self.h.data
            self.h = self.h.next
            return o

        return self._dequeue(self.h, self.h.next, tp)

    def _dequeue(self, p, c,clss):
        if c is None:
            return

        if isinstance(c, clss):
            o = c.data
            p.next = c.next
            return o

        p = c
        c = c.next
        return self._dequeue(p, c, clss)


class Animal():
    def __init__(self, n):
        self.data = n
        self.next = None


class Cat(Animal):
    pass


class Dog(Animal):
    pass


import unittest


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Cat("Ton2"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAnimal(Dog)), "Pluto")
        self.assertEqual(str(shelter.dequeueAny()), "Garfield")
        self.assertEqual(str(shelter.dequeueAnimal(Dog)), "Clifford")
        self.assertEqual(str(shelter.dequeueAnimal(Cat)), "Tony")
        self.assertEqual(str(shelter.dequeueAnimal(Cat)), "Ton2")
        self.assertEqual(str(shelter.dequeueAny()), "Blue")
        self.assertEqual(str(shelter.dequeueAnimal(Dog)), "None")


if __name__ == "__main__":
    unittest.main()
