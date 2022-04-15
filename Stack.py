# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Basic example of an adapter class to provide a stack interface to Python's list."""

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]    
    # the last item in the list

  def bottom(self):
      if self.is_empty():
          raise Empty('Stack is empty')
      return self._data[0]
    

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()               # remove last item from list



Original = AS()
Fidelity = AS()
Helper = AS()

Original.push('JAMFX')
Original.push('FSELX')
Original.push('FOCPX')
Original.push('AFOIX')
Original.push('TEFQX')
Original.push('FSRPX')
Original.push('MSSMX')
Original.push('FSCSX')
Original.push('FSPTX')
Original.push('FCPGX')
Original.push('MACGX')
Original.push('JMCGX')
Original.push('FCVSX')
Original.push('NEXTX')
Original.push('BFOCX')
Original.push('BFGFX')
Original.push('ADNPX')
Original.push('FDSVX')
Original.push('FSAVX')
Original.push('FHKCX')
Original.push('SAGAX')
Original.push('FSEAX')
Original.push('CPOAX')
Original.push('FDCPX')
Original.push('FTRNX')
Original.push('FNCMX')
Original.push('FBGRX')
Original.push('FSMEX')




def func1(Original, Fidelity, Helper):
   for i in range(Original.__len__()):
       Helper.push(Original.pop())
   for i in range(Helper.__len__()):
     if Helper.top()[0] == 'F':
       Fidelity.push(Helper.pop())
     else:
       Original.push(Helper.pop())
     
   return ((Fidelity.top(), Fidelity.bottom()), (Original.top(), Original.bottom()))

if __name__ == "__main__":
  print(func1(Original, Fidelity, Helper))
  