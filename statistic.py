TextFile = open("qbdata.txt", "r")
TextFile = TextFile.readlines()

counter = 0
spacecounter = 0
nameindex = []
scoreindex = []
for line in TextFile:
    while spacecounter != 2:
        if line[counter] == ' ':
            spacecounter = spacecounter + 1
        counter = counter + 1
    name = line[ : counter]
    name = name.strip(' ')
    counter = 0
    spacecounter = 0
    reverseline = line[::-1]
    while spacecounter != 1:
        if line[counter] == ' ':
            spacecounter = spacecounter + 1
        counter = counter + 1
    score = reverseline[ : counter]
    score = score[::-1]
    score = score.strip(' ')
    score = score.strip("\n")
    if eval(score) >= 60:
        nameindex.append(name)
        scoreindex.append(score)
    counter = 0
    spacecounter = 0

OutFile = open("Output.txt", "w")

for i in range(len(nameindex)):
    write = nameindex[i] + ' ' + "has a rating of" + ' ' + scoreindex[i]
    print(write)
    print()
    OutFile.write(write + "\n" )

OutFile.close()
    

    
    
        
        
        
           
            
            
            
    
    
        
    