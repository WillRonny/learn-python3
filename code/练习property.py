#!/usr/bin/env python3
class Screen(object):
    @property
    def width(self, width):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width
    @property
    def height(self, height):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height
    @property
    def resolution(self):
        return self._width * self._height

a = Screen()
a.width = 1024
a.height = 768
print(a.resolution)
#assert a.resolution == 786432, '1024 * 768 = %d ?' % a.resolution