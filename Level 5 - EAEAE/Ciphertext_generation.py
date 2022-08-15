
print("Generating Corresponding ciphertext....")

with open('output.txt', 'r') as f:
    b = f.read().splitlines()

cp = open('ciphertext.txt','a+')

li=[]
for i in b:
    if '\t\t' in i:
        s=i.split('\t')[-1]
        li.append(s)
        
li=li[4:]

k=0
for i in range(8):
    for j in range(128):
        cp.write(li[k]+" ")
        k+=1
    cp.write('\n')
cp.close()

print("ciphertext generation done....")


