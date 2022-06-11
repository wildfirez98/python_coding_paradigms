# Functional Prompt

"""
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
"""

def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
    return sorted(arr)

print(flatten_and_sort([]), [])
print(flatten_and_sort([[], []]), [])
print(flatten_and_sort([[], [1]]), [1])
print(flatten_and_sort([[12, 19, 6], [7, 13, 20], [2, 10, 6]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])


'''
How does this solution ensure data immutability?

  The function is not pulling data from another source, rather the data for the array is being passed in, the function sorts the array and then just returns it.

Is this solution a pure function? Why or why not?

  Yes it is. The function takes in an argument, sorts the data, returns it and passes execution control back to the caller.

Is this solution a higher order function? Why or why not?

  This solution is a higher order solution, because it is using the 'sorted' method to return our array.

Would it have been easier to solve this problem using a different programming style?

  Not to my knowledge. This seems like an effective solution to its problem within 6 lines of code and should be consistent with its results.

Why in particular is functional programming a helpful paradigm when solving this problem?

  Functional programming provides consistent, clear and concise programming by taking a problem and breaking it down into functions that should be understandable and predictable which is a great thing as software developers.

'''

# Object Oriented Prompt

'''
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

Define a repair() method that will update the condition of the podracer to "repaired".

Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
    
Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "Repaired!"
    
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
    
  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self):
    self.condition = "Trashed!"

Racer_1 = Podracer(1, "Trashed!", 5000)
Racer_2 = Podracer(3, "Brand New!", 4500)
Racer_3 = AnakinsPod(2, "Brand New!", 6000)
Racer_4 = SebulbasPod(4, "Brand New!", 3000)

Racer_1.repair()
print(Racer_1.condition)

print(Racer_2.condition)

Racer_3.boost()
print(Racer_3.max_speed)

Racer_4.flame_jet()
print(Racer_4.condition)

'''

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

Encapsulation:
      We are encapsulating information or code within our classes
    
Abstraction:
      By encapsulating our code, we are hiding unecessary information for our race or game that could otherwise be potentially used as a vulnerability. Its a good idea to hide Anakins boost function within his class, wherein other racers might try to somehow exploit this given knowledge about where it resides.
  
Inheritance:
      We are using inheritance in this code by using the Podracer class. This allows us to not have to define a class for each racer's Pod and instead just reference the Podracer class as the basis for each racer and then add specific features to each racer as desired. The specific features to a racer would allow us to more easily troubleshoot specific problems with that feature that we might encounter.

Polymorphism:
      I believe that we are by using the Podracer class. Each racer class is using the Podracer class interface.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

      I don't believe so. For making a racing game it makes alot of sense that we have a base race class and that all other racers inherit from that. Any additional features we want to add are done so in that object which makes it easier to work with. 

How in particular did Object Oriented Programming assist in the solving of this problem?

      As mentioned above, the Podracer class has a set or baseline of features for all racers to inherit which allows us a baselevel of consistency for the program. Additional optional features can be added to the racer as we so desire.

'''
