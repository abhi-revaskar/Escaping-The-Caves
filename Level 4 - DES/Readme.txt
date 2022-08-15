1. Generating input Plaintexts using "Generating_input.ipynb" file (output:- plaintexts.txt)

2. Generating Script(.sh) file that helps to generate ciphertexts for the corresponding plaintexts using "Generating_scriptfile.ipynb" file  (input:- plaintexts.txt ,output:- script.sh)

3. Run "command.sh" that uses "script.sh" to generate the ciphertexts for the corresponding plaintexts (input:- script.sh, output:- output.txt)

4. Generated "output.txt" file is processed using "Generating_ciphertext_file.ipynb" file (input:- output.txt, output:- ciphertexts.txt)

5. Processing "ciphertexts.txt" to convert it into binary using "Ciphertext_to_binary.ipynb" (input:- ciphertexts.txt, outputs:- binary_cipher.txt and bin_cipher.txt)

6. Using "Differential_cryptanalysis.ipynb" to generate Expansion box output XOR file (ebox_op.txt),S-Box input XOR( sbox_ip.txt) and S-Box output XOR (sbox_op.txt)

7. Extract S-Box keys using "sbox_key_generation.ipynb" file and got the possible keys for the S-Boxes 1,2,5,6,7,8.

8. Using these S-Box keys, we generate all possible 56-Bit Keys using "Possible_keys.ipynb" file (output:- possible_keys.txt)

9. Using "Extracting_Key.ipynb" program and "possible_keys.txt" we have extracted the final 56-bit key.

10.Finally run "DES.cpp" which gives the ascii values for the decrypted password which further converted to their corresponding ascii characters and got the password using which we cleared the level.

Note:- "All_files" folder contains  script.sh , plaintexts.txt, ciphertexts.txt, output.txt, bin_cipher.txt, binary_cipher.txt,         ebox_op.txt, possible_keys.txt, sbox_ip.txt, sbox_op.txt.