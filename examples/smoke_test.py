import sys
import clr

dll_dir = r"C:\Users\glddm\source\repos\OptimalDecompression\TrinomialModel\bin\Debug\net462"
sys.path.append(dll_dir)

clr.AddReference("TrinomialModel")

from TrinomialModToPython import ToPython

node = ToPython.createNode(20.0, 0.0, 1.2, 0.95, 0.9, 1.0)
next_node = ToPython.stepFunction(node, 1.0/3.0, 10.0)

print("Init node:")
print(node)
print("Next node:")
print(next_node)

print("again")
print("Init node:")
print(node)
print("Next node:")
print(next_node)