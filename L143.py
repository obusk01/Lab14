#Bethany B, Grace A, Olivia B
class Coffee_Mug:
    """Represents a coffee mug

    attributes:capacity, shape, material, color."""



def coffee_drinking_simulation(x):
    leftover=x.capacity-x.amount
    print(leftover)

a=Coffee_Mug()
a.capacity=200
a.shape="round"
a.material="ceramic"
a.amount=180

coffee_drinking_simulation(a)
