def find_inputs_for_output(program):

    target_output = 19690720

    for noun in range(100):
        for verb in range(100):

            p = program[:]
            p[1] = noun
            p[2] = verb

            for i in range(0, len(p), 4):
                opcode = p[i]
                if opcode == 1:
                        p[p[i+3]] = p[p[i+1]] + p[p[i+2]]
                elif opcode == 2:
                        p[p[i+3]] = p[p[i+1]] * p[p[i+2]]
                elif opcode == 99:
                        break

            if p[0] == target_output:
                print(100 * noun + verb)
                break
        else:
            continue
        break