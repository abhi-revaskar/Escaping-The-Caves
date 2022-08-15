Group Name :- DECODERS
---------------------------
1. To generate plaintexts we have used "Plaintext_generation.py".
   This program generates the "plaintext.txt" file

2. To generate corresponding ciphertext we have used "Ciphertext_generation.py".
   This program generates the "ciphertext.txt" file

3. To decrypt the password, we have to run "EAES_ALGO.py" file which accesses "plaintext.txt" and "ciphertext.txt"  files and generates the password.

4. "Generating_script.py" is used to generate "script.sh" file which further use to get ciphertext

5. "command.sh" uses "script.sh" which helps to generate ciphertexts from server for plaintexts.

---------------------------
About Makefile:-
Make file helps to install required dependancies and also calls "command.sh" to generate "output.txt" file which further uses to get "ciphertext.txt"
---------------------------


Steps to run the program:
1. unzip the folder "DECODERS.zip" and open terminal in that directory.
2. enter "make attack" command in the terminal and press enter which generates "plaintext.txt" and "ciphertext.txt" files.It takes some time to generate the password. After executing all the neccessory programs it prints the password in the terminal. 

Example command to enter in terminal: $ make attack