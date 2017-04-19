#Mark Tillinghast
#replication of crucial experiment by Stephen Wolfram.
#this is my own work, provided for anyone who has knowledge
# of python for use in any way for the betterment of humankind.
# (c) 2017
rule_110="01101110"
rule_102="01100110"
dict_102 = {"000" : "0",
            "001" : "1", 
            "010" : "1",
            "011" : "0",
            "100" : "0",
            "101" : "1",
            "110" : "1",
            "111" : "0" }

first_line="0"*75+"1"+"0"*25
print first_line
#import pdb
#pdb.set_trace()
current_line=first_line.strip()
for itheir in  range(0,900):
    next_line=""
    for j in range(0,len(current_line)-3): #why does this fail badly when =1
       #print itheir,j,current_line[j:j+3],dict_110[current_line[j:j+3]]
       next_line=next_line+dict_102[current_line[j:j+3]]
    print next_line
    current_line="0"+next_line+"00" 
