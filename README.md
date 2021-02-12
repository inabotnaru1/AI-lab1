## Laboratory Nr.1 Expert System
<br> 
Language: <b>python</b> <br>
Run command: <b>python main.py </b>

<br>

   To make the system "predict" the type of tourist, I researched different ways of solving such issues. From my perspective, the solution that I choose is simpler to understand and to implement than others. Thus, I started by creating a set of rules, in a form of a list. 
<br>   Thus, if a creature has two legs, skin color beige, has hair, the biggest value is empathy and go to the interstellar war with a gun, it means that he is from planet Earth, or how I call him: earthlender. The list looks like this:
<br><br><i>rules = [
<br>    ['beige', 2, 'hair','empathy','gun','earthlender'],
<br>    ['red', 0, 'horns','love','stones','martianin'],
<br>['blue', 10, 'tail','honest','stones','plutonist'],
<br>    ['red', 0, 'wings','love','fire','hottie'],
<br>    ['brown', 5, 'wings','wisdom','gun','jupiterman'],
<br>   ['blue', 2, 'tail','honest','gravity','loonie']
<br>]</i>

The first 5 columns provide features or attributes that describe the data. The last column gives the type of tourist we want to predict.
Now to build the tree, we use the decision tree learning algorithm called CART. At their core, they give us a procedure to decide which questions to ask and when. CART stands for Classification
and Regression Trees.
The root will receive the entire data set with attributes. Now each node will ask a true false question about one of the features and in response to this question, we split, or partition,
the data into two subsets. These subsets then become the input to two child nodes we add to the tree. And the goal of the question is to “unmix” the labels (to produce the purest possible distribution of the labels at each node. 
<br> <br>
Next it is possible to quantify the amount of uncertainty at a single node using a metric called <b> Gini</b>.
And we can quantify how much a question reduces that uncertainty using a concept called information gain which is basically the amount of information gained about a random variable or signal from observing another random variable.

In code I represent a question by storing a column number and a column value, or the threshold it will use to partition the data.
```
  class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            columns[self.column], condition, str(self.value)) 
```
```
  from __future__ import print_function
  from rules import rules, columns
  from helper import *
  from nodes import *


  def build_tree(rows):
      gain, question = find_best_split(rows)

      if gain == 0:
          return Leaf(rows)

      true_rows, false_rows = partition(rows, question)

      true_branch = build_tree(true_rows)
      false_branch = build_tree(false_rows)

      return Decision_Node(question, true_branch, false_branch)


  def predict_answer(node):

      if isinstance(node, Leaf):
          print( "The system says it's totally a ", next(iter(node.predictions)),'\n')
          return

      print(str(node.question))
      answer = input("$$ ")

      if answer == "true":
          predict_answer(node.true_branch)
      elif answer == "false":
          predict_answer(node.false_branch)
      else:
          print("Unvalid answer, try again")

  data_tree = build_tree(rules)

  print("__________________________________________________________________________\n")
  print("In order to find out the type of tourist, you should answer some questions:")
  print("__________________________________________________________________________\n")
  predict_answer(data_tree) ```
  
 ```
 You can see that the system finds the best question to ask, and after that, based on the answer, it continues to build the tree if the prediction is not 100%. 
 <br> 
 ![alt text](https://github.com/inabotnaru1/AI-lab1/blob/main/screenshots/Screen%20Shot%202021-02-11%20at%2022.34.48.png)
 
 ![alt text](https://github.com/inabotnaru1/AI-lab1/blob/main/screenshots/Screen%20Shot%202021-02-11%20at%2022.35.03.png)
