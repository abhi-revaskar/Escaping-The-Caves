import numpy as np

print("Started plaintext generation....")

#mapping only char between f to u is used only
mapping = {'0000': 'f','0001': 'g','0010': 'h','0011': 'i','0100': 'j','0101': 'k','0110': 'l','0111': 'm','1000': 'n','1001': 'o','1010': 'p','1011': 'q','1100': 'r','1101': 's','1110': 't','1111': 'u'}

#generating plaintext values
li=[]
for i in range(8):
    st=""
    for j in range(128):
        binary = bin(j)[2:].zfill(8)
        plaintext = 'ff'*i + mapping[binary[:4]] + mapping[binary[4:]] + 'ff'*(8-i-1)
        st+=(plaintext+" ")
    li.append(st)        

#write values into plaintext values
file=open("plaintext.txt","w+")
for i in li:
    file.write(i)
    file.write("\n")
file.close()
print("Generating plaintext Done....")