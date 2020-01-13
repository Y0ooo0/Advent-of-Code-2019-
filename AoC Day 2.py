def Intcode(intcode, noun, verb):
    inc = 0
    intcode[1] = noun
    intcode[2] = verb
    for num in intcode:
        if intcode[inc] == 99:
            break
        op1 = intcode[intcode[inc + 1]]        
        op2 = intcode[intcode[inc + 2]]        
        result = intcode[inc + 3]
        if intcode[inc] == 1:                  
            intcode[result] = op1 + op2
        elif intcode[inc] == 2:          
            intcode[result] = op1 * op2
        inc += 4
    if intcode[0] == 19690720:
        print (100 * noun + verb)

for noun in range(0,100):
     for verb in range(0, 100):
         inc = 0
         input = []
         intcode = []
         with open(r'C:\Users\loriy\Documents\Python\Day2AoC.txt', "r") as file:
            input.append((file.read()).split(','))

         for x in input[0]:
            intcode.append(int(input[0][int(inc)]))
            inc += 1
                
         Intcode(intcode, noun, verb)

#9507


        



