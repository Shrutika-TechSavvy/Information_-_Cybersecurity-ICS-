# **One-Time Password(OTP) algorithm in Cryptography**
An OTP is a password that is valid for only one login session or transaction. It prevents **replay attacks** because even if someone steals the password it cannot be reused.

There are two major meaning of OTP in cryptography:
  - One-Time Pad (Theoretical perfect encryption)
  - One-Time Password (authentication method)

# One-Time Pad(OTP) – An Encryption Algorithm
The OTP is a symmetric encryption technique that is mathematically unbreakable if used correctly.

# Technique 2 : One-Time Password (OTP) for Authentication
A One-Time Password (OTP) is a dynamically generated password that is valid for only one login session or transaction.We mainly use this in Internet banking, email login, online payments, two factor authentication (2FA).

Types of OTP: 
1. Time-Based OTP (TOTP)
   - The most common way for the generation of OTP defined by The Initiative for Open Authentication (OATH) is the Time Based One Time Passwords (TOTP), which is a Time Synchronized OTP.
   -  In these OTP systems, time is the cardinal factor to generate the unique password. The password generated is created using the current time and it also factors in a secret key.
   -  An example of this OTP generation is the Time Based OTP Algorithm (TOTP) described as follows: Example picture from the google
The TOTP works because:
  - Both the server and your phone have the same secret key
  - Both use the same time
  - Both apply the same math formula
  - So both them generate the same Otp - without talking to each other, like image we have below
<img width="800" height="375" alt="image" src="https://github.com/user-attachments/assets/0255a747-f5ee-4077-be6a-770597f17342" />
Explaining the diagram :
  <img width="745" height="960" alt="image" src="https://github.com/user-attachments/assets/60a6b5bb-515b-4328-9896-ad4dd9dfa3c8" />

Step by step flow of diagrma :
**We have 3 main characters:**
- Alice (User)
- Service Provider (Google, FB, etc)
- Authenticator app (Google authenticator)


Step 1:  Alice enables 2 FA
Alice logs into her account and clicks  "Enable Two-factor Authentication (2FA)". Now server generates a secret key eg. Secret Key = JBSWY3DPEHPK3PXP .

Step 2: Server creates a QR Code
- The server does not send OTP directy. Instead , it creates a QR code.
- The OTP contains the secret key, algorithm name(TOTP), Time step useually 30 sec, app/ account name.
  
eg. otpauth://totp/Google:alice@gmail.com?
secret=JBSWY3DPEHPK3PXP&
algorithm=SHA1&
digits=6&
period=30

So, the QR code is just a way to safely send the SECRET to Alice's phone.


Step 3: Alice scans QR Code
Alice installs Google authenticator. She scans QR now the secret key is stored inside her phone , the phone now knows the secret. 
So Now, server has secret key, Alice's phone has secret key and after this no mor communication is needed. 




