# Copyright 2020 Ian Rankin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
# to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
# Edge.py
# Written Ian Rankin October 2019
#
# Rather a directed edge, but called an edge for short.
# Contains the basic implementation for an edge.
# Particular designed to be extendable to allow different information to be
# stored.

class Edge(object):
   # constructor
   # Pass the parent and child nodes directly (not indcies)
   def __init__(self, parent, child, cost = 1.0):
      # should be handed the parent node directly.
      self.p = parent
      self.c = child

      # don't reference directly rather reference the getCost function.
      self.cost = cost

   # get function for cost.
   # This shoud be called rather than directly referencing
   # in case the function is overloaded.
   def getCost(self):
      return self.cost


   # checks if connecting id's are the same and cost is the same (could potentially)
   # have two different edges to the same two nodes.
   def __eq__(self, other):
      return isinstance(other, Edge) and self.c.id == other.c.id and self.p.id == other.p.id \
                and self.cost() == other.cost()

   def __str__(self):
      return 'e(p.id='+str(self.p.id)+',c.id='+str(self.c.id)+',cost='+str(self.cost)+')'
