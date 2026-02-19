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
   -  An example of this OTP generation is the Time Based OTP Algorithm (TOTP) described as follows:
  <img width="745" height="960" alt="image" src="https://github.com/user-attachments/assets/60a6b5bb-515b-4328-9896-ad4dd9dfa3c8" />

  
