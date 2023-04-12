f = open("day1_data.txt")
masses = [int(line.strip()) for line in f.readlines()]
f.close()

def calculate_fuel(masses):
    total_fuel = 0
    for mass in masses:
        fuel_for_module = 0
        while mass > 0:
            mass = mass // 3 - 2 
            fuel_for_module += max(mass, 0)
        total_fuel += fuel_for_module
    return total_fuel

print(calculate_fuel(masses))