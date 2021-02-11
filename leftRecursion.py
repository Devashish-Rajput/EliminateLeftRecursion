def readInputFile(file):
    f = open(file)
    map1 = {}
    for line in f:
        line = line.replace('\n','')  
        rules = line.split(':') 
        rules[0] = rules[0].strip()
        map1[rules[0]] = rules[1]
    return map1

def readRightSide(map):
    for element, body in map.items() :
        body = body.strip()
        map[element]= body.split('|')
    for key,value in map.items() :
        if 'epsilon' in value :
            value.remove('epsilon')
            for key1,value1 in map.items() :
                for element in value1 :
                    if key.strip() in element.strip() :
                        newstr = element.replace(key, '')
                        value1.append(newstr)
    return map

def eliminate_indirect(map):
    i = 0
    j = 0
    for key, value in map.items() :
        for key1, value1 in map.items() :
            if j > i :
                for v in value1 :
                    if v[0] == key :
                        vv = v[1:]
                        new_values = []
                        for v1 in value :
                            new_values.append(v1+vv)
                        value1 += new_values
                        value1.remove(v)            
            j+=1
        i+=1
        j=0            
    print(map)                       
    return map

def eliminate_direct(map):
    newRules = {}
    exist = False
    for key,value in map.items():
        for v in value :
            if v[0] == key :
                exist = True
        if exist==False:
            newRules[key] = value 
        else :
            key1 = key
            key2 = key+'\''
            value1 = []
            value2 = [] 
            for v in value :
                if v[0] != key:
                    value1.append(v+key2)
                else :
                    value2.append(v[1:]+key2)    
            value2.append('epsilon')
            newRules[key1] = value1
            newRules[key2] = value2
        exist = False    
    print(newRules)        
    return newRules        
    
mappy=readInputFile("leftRecursionInput.txt")
print(mappy)
print('Hello')
right = readRightSide(mappy)
eliminate_indirect = eliminate_indirect(right)
eliminate_direct = eliminate_direct(eliminate_indirect)
f = open("result.txt", "w")
for key,value in eliminate_direct.items() :
    f.write(key+' : ')
    for v in value :
        f.write(v)
        if not v is value[-1]:
            f.write(' | ')
    f.write('\n')    
    
f.close()