f = open("day1_data.txt", "r")
masses = f.readlines()
f.close()

def calculate_fuel(masses):
    total_fuel = 0
    for mass in masses:
        mass = int(mass.strip())
        fuel = mass // 3 - 2
        total_fuel += fuel
    return total_fuel

print("Total fuel required", calculate_fuel(masses))
