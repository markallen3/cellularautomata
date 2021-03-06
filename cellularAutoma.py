#Mark Tillinghast
#replication of crucial experiment by Stephen Wolfram.
#this is my own work, provided for anyone who has knowledge
# of python for use in any way for the betterment of humankind.
# (c) 2017
#Notes:
# The contractive mapping on either side is counter intuitive, but because of the rules, must be in place
# otherwise the universe shrinks down to nothing.
# The use of trits in genomics is profoundly similar.
# see: https://en.wikipedia.org/wiki/Genetic_code#RNA_codon_table
rule=range(256)
current_rule=bin(102)
current_rule=current_rule[2:]
current_rule="0"*(8-len(current_rule))+current_rule
print current_rule,len(current_rule)

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

first_line="0"*75+"1"+"0"*25 #if you don't start with a 1 somewhere, you don't get anything.
print first_line.strip()
#import pdb
#pdb.set_trace()
current_line=first_line.strip()
for itheir in  range(0,900):
    next_line=""
    for j in range(0,len(current_line)-3): #why does this fail badly when =1
       #print itheir,j,current_line[j:j+3],dict_110[current_line[j:j+3]]
       next_line=next_line+dict_102[current_line[j:j+3]]
    print next_line
    current_line="0"+next_line+"00"  # it is a contractive mapping so we need to add back the universe on either side.
