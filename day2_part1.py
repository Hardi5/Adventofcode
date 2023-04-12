with open("day2_data.txt") as f:
    intcode = [int(x) for x in f.read().split(',' )]
    

    def run_intcode_program(intcode):
        i = 0
        while i < len(intcode):
            opcode = intcode[i]
            if opcode == 1:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
            elif opcode == 2:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
            elif opcode == 99:
                break
            i += 4
        return intcode

result = run_intcode_program(intcode)
print(result)
