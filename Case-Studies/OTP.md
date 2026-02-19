# **One-Time Password(OTP) algorithm in Cryptography**
An OTP is a password that is valid for only one login session or transaction. It prevents **replay attacks** because even if someone steals the password it cannot be reused.

There are two major meaning of OTP in cryptography:
  - One-Time Pad (Theoretical perfect encryption)
  - One-Time Password (authentication method)

# technique 1: One-Time Pad(OTP) – An Encryption Algorithm
The OTP is a symmetric encryption technique that is mathematically unbreakable if used correctly.We'll look at this later...

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


**Step 1:  Alice enables 2 FA**
- Alice logs into her account and clicks  "Enable Two-factor Authentication (2FA)". Now server generates a secret key eg. Secret Key = JBSWY3DPEHPK3PXP .

**Step 2: Server creates a QR Code**
- The server does not send OTP directy. Instead , it creates a QR code.
- The OTP contains the secret key, algorithm name(TOTP), Time step useually 30 sec, app/ account name.
  
eg. otpauth://totp/Google:alice@gmail.com?
secret=JBSWY3DPEHPK3PXP&
algorithm=SHA1&
digits=6&
period=30

So, the QR code is just a way to safely send the SECRET to Alice's phone.

**Step 3: Alice scans QR Code**
- Alice installs Google authenticator. She scans QR now the secret key is stored inside her phone , the phone now knows the secret. 
- So Now, server has secret key, Alice's phone has secret key and after this no mor communication is needed. 

**Step 4 : How OTP is generated**
For every 30 seconds, 
Phone does: 
- Time Counter = Current Unix Time / 30
- Then, OTP = HMAC-SHA1(secret_key, time_counter)
- Then, take last 6 digits , show on screen eg. 628374
- server is doing same calculation at same time because same secret, same time, same formula so both gets 628374

**Step 5: Login process**
- Now Alice tries to login, 
- She enters: Username and Password. 
- Server says : Enter tje OTP, 
- She checks phone: 628374 and types it, 
- Server checks, it calculates its own OTP and if it matches - > login process

So, 
**What flows during setup?**
Server ➝ QR Code ➝ Phone
(Secret key flows ONCE)

**What flows during login?**
User ➝ OTP ➝ Server
(Just the 6-digit number)

# Why server and app don't communicate ?
Because both:
  - Already know the secret
  - Already knew the time
  - Already know the formula
,So they independently generate the same OTP.

- **thus, TOTP works because both the server and the authenticator app share a secret key and use the current time to independently generate the same one-time password.**

# Important
- In this case study, we used Google Authenticator as the OTP delivery method. However, it is important to understand that Google Authenticator is not the only option. OTPs can also be delivered through other methods such as SMS, email, hardware tokens, or push notifications.

- If a different OTP delivery method is used, the system needs some changes. For example, in SMS-based OTP, the server must generate the OTP and send it to the user’s registered mobile number through an SMS gateway. In email-based OTP, the system must be connected to an email service. For hardware tokens or authenticator apps, the system must securely generate and store a shared secret key.

- Each method has different security levels and infrastructure requirements. Authenticator apps and hardware tokens are generally more secure because they do not rely on network transmission for every login, while SMS and email methods are easier to implement but slightly less secure.

- So, depending on the security needs, budget, and system design, any suitable OTP delivery method can be used with the required technical adjustments.
