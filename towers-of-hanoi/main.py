stacks = []

while True:
    disks = int(input("How many disks do you want? "))
    if disks >= 3:
        break
    print("You must have at least 3 disks!")

stacks.append([i for i in range(disks, 0, -1)])
for _ in range(disks - 1):
    stacks.append([])

def display_stacks():
    for stack in stacks:
        for i in range(disks + 3):
            height = disks + 3 - i
            if height + 1 - i < disks:
                disk = stack[height - 1]
                print("{:^10}".format("=" * disk + "=" + "=" * disk))
            else:
                print("{:^10}".format("|"))
        print("____|_____")

display_stacks()
