# csi_3680_final
## RSA Encryption
A data encryption and decryption tool
• e.g., Implement RSA algorithm from scratch, and the RSA modulus must be at least
1024 bits long.
• Randomly generate private key and public key from RSA algorithm, therefore to
encrypt and decrypt any file.

## Requirements
Python based.
A topic with potential practical usage.
At least define and use TWO functions in a meaningful way.
At least import ONE third-party library/package to support your
implementation.
At least ONE file I/O operation, either read or write or both.
Use exceptions to check whether each file was opened without an error.
Visualize your outcomes
Plot, image, webpage,GUI … something other than console output!

## Instructions

pip install pypdf

1.	Run the Python file, main.py
a.	You will see the following screen:
 
2.	First, input a number for e or leave blank if you would like to use the default value of 65537
a.	Select “Generate Keys”
b.	It will create two files, privateKey.txt and publicKey.txt
i.	Stored in the same folder as main.py
ii.	Holds private key and public key respectively
iii.	Do not share the private key

3.	Encrypt File (simulating sending to another user)
a.	Select the file you want to encrypt to send to another user
i.	“Browse”, under Selected File to Encrypt
b.	Assume that the other user has shared their public key
i.	Select the public key file that they have shared with you
1.	For example, publicKey.txt
ii.	“Browse”, under
c.	Select “Submit”
d.	If successful, you will see the following window
e.	It will be stored in the same folder 
i.	“Encrypted – filename.txt”

4.	Encrypt File (proving your identity)
a.	Same steps as 3, except, you would select your private key file

5.	Decrypt File (Receiving a file from another user sent to you)
a.	Select the file sent by another user that you want to decrypt 
i.	“Browse”, under Selected File to Decrypt
b.	Assume that the other user has shared their public key
i.	Select the public key file that they have shared with you
1.	For example, publicKey.txt
ii.	“Browse”, under
c.	Select “Submit”
d.	If successful, you will see the following window
e.	It will be stored in the same folder
i.	“Decrypted – filename.txt”

6.	 Decrypt File (Authenticating sender’s identity)
a.	Same steps as 5, except, you would select their public key

## Sources
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

https://math.asu.edu/sites/default/files/rsa_0.pdf

https://docs.python.org/3/library/random.html?highlight=random#module-random# CSI_3680_Final_Project_Public
