file1 = "C:\\Users\\house\\Desktop\Db\\Bioinformatics project\\Motif1.txt"
file2 = "C:\\Users\\house\\Desktop\Db\\Bioinformatics project\\Test.csv"
def CountSequences(file,outFile):
    orgDict = {}
    readFile = open(file,'r')
    writeFile = open(outFile,'w')
    nextLine = 0
    for line in readFile:  
        if line[0:18] == "Non human Organism":
            orgKey = line[19:].replace('.tsv\n','')
            if orgKey not in orgDict:
                orgDict[orgKey] = {"4":0,"3":0,"2":0,"1":0}
        
        elif line[0:9] == "4 matches":
            nextLine = "4"
           
        elif line[0:9] == "3 matches":
            nextLine = "3"
            
        elif line[0:9] == "2 matches":
            nextLine = "2"
            
        elif line[0:9] == "1 matches":
            nextLine = "1"
        elif line[0] != " " and nextLine:
            
            orgDict[orgKey][nextLine] += 1
            
            
        
    for organism in orgDict:
        print(organism)
        writeFile.write(organism +','+ str(orgDict[organism]["4"]) +','+ str(orgDict[organism]["3"]) +','+ str(orgDict[organism]["2"]) +','+ str(orgDict[organism]["1"]) + '\n')
    readFile.close()
    writeFile.close()
CountSequences(file1,file2)
