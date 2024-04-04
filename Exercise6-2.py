#2.Tower of Hanoi using recursion

def tower_of_hanoi(disks, source, auxiliary, destination):
  if disks == 1:
    print(f"Move disk 1 from rod {source} to rod {destination}")
    return

  # Move n-1 disks from source to auxiliary using destination as auxiliary
  tower_of_hanoi(disks - 1, source, destination, auxiliary)

  # Move the remaining largest disk from source to destination
  print(f"Move disk {disks} from rod {source} to rod {destination}")

  # Move n-1 disks from auxiliary to destination using source as auxiliary
  tower_of_hanoi(disks - 1, auxiliary, source, destination)

n=int(input("Enter the Number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')