import argparse

parser = argparse.ArgumentParser(description="Optimize your Nuggets")
parser.add_argument('amount', metavar = 'N', type=int, help="The amount of nuggets you want to optimize")
args = parser.parse_args()
class Item:
    def __init__(self, amount, cost):
        self.cost = cost
        self.amount = amount
        try:
            self.efficiency = self.calculate_efficiency()
        except:
            self.efficiency = 0

    def calculate_efficiency(self):
        return (self.amount / self.cost)
    def __eq__(self,other):
         return self.efficiency == other.efficiency
    def __lt__(self,other):
         return self.efficiency < other.efficiency


sorted_items = [
    Item(12, 11.95),
    Item(10, 10.20),
    Item(6, 7.00),
    Item(3, 5.00)
]

target_total = args.amount

nodes = []
for i in range(len(sorted_items)):
    nodes.append(0)

def current_quantity():
    q = 0
    for i, node in enumerate(nodes):
        q += node * sorted_items[i].amount
    return q

def recursive(i):
    while current_quantity() < target_total:
        nodes[i] += 1
        if current_quantity() == target_total:
            return True
    nodes[i] -= 1
    #print("Beginning recursion {1} with nodes: {0}, processed maximum {2}".format(nodes, i, nodes[i]))

    while nodes[i] >= 0:
        if i is not len(nodes) - 1:
            #print("Stepping forward ({0}-{1})".format(i, i+1))
            forward = recursive(i + 1)
            #print("Returned to {0}, with {1} success ".format(i, forward))
            if forward:
                return True
        #print("Lowering {0} ({1}-{2}) and repeating if {2} is >= 0".format(i, nodes[i], nodes[i] - 1))
        nodes[i] -= 1
        if current_quantity() == target_total:
            return True
    nodes[i] = 0
    #print("Stepping back from {0}".format(i))
    return False

if recursive(0):
    print("The Optimal Nugget Configuration for {0} nuggets is:".format(target_total))
    for i, node in enumerate(nodes):
        if node is not 0:
            print(" - {0} x {1} nuggets for ${2} at ${3} each".format(node, sorted_items[i].amount, node * sorted_items[i].cost, sorted_items[i].cost))
    print("This will come to a total of ${0}").format(current_quantity())
else:
    print("There is no optimal nugget configuration for {0} nuggets".format(target_total))
