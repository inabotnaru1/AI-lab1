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
predict_answer(data_tree)
