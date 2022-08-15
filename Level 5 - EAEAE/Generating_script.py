print("started generating script")
string = ''
f= open('plaintext.txt','r')
for i in f.readlines():
    li = i.split()
    for j in li:
        if(j=='\n'):
            continue
        string = string + j + "\\" + "n"  + 'c' + "\\n"
string

string = 'echo -e "DECODERS\\ncypertine@28\\n5\\ngo\\nwave\\ndive\\ngo\\nread\\n' + string +'back\\nexit"'
j= open('script.sh','w+')
j.write(string)
j.close()

print("script generation done")