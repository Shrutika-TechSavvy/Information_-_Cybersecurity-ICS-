# Blocking Access to BookMyShow Using Windows Firewall (Case Study)

## Introduction

In this case study, we demonstrate how to block access to a specific website, BookMyShow, on a Windows machine using Windows Defender Firewall.

This task helps in understanding:
- How outbound firewall rules work
- How websites are accessed over networks
- How IP-based blocking can restrict access

The objective is to prevent any application on the system from connecting to BookMyShow servers.
## Objective

To configure Windows Firewall such that access to https://www.bookmyshow.com is blocked for all applications on the system.
## Background Concepts

Before implementing the solution, it is important to understand:

- Websites are accessed using domain names (e.g., bookmyshow.com)
- These domain names are translated into IP addresses using DNS
- Firewalls operate at the network level and can block traffic based on IP addresses
- Outbound rules control traffic leaving the system

Since BookMyShow uses multiple IP addresses (via CDN services), multiple IPs need to be considered.

### Step 1: Open Windows Defender Firewall with Advanced Security

Press `Win + R`, type `wf.msc`, and press Enter.

This opens the advanced firewall configuration panel where custom rules can be created.
<img width="899" height="732" alt="image" src="https://github.com/user-attachments/assets/0aa1a137-1e19-4983-97d8-717e9ef56006" />

### Step 2: Create a New Outbound Rule

Navigate to "Outbound Rules" and click on "New Rule".

Outbound rules control traffic leaving the system. Since we want to block access to a website, we create an outbound rule.
### Step 3: Select Rule Type as Custom

Choose "Custom" to gain full control over the rule configuration.

This allows specifying:
- Programs
- Protocols
- IP addresses
- <img width="1311" height="987" alt="image" src="https://github.com/user-attachments/assets/f42d1dfc-ea5b-4e33-8bc9-a6e3b53f2aed" />
### Step 4: Apply Rule to All Programs

Select "All programs".

This ensures that no application (browser or otherwise) can access the target website.
<img width="1315" height="988" alt="image" src="https://github.com/user-attachments/assets/506bb578-82de-4668-bee6-90fdcbf163a7" />

### Step 5: Protocol and Ports Configuration

Leave the default settings (Any protocol and port).

This ensures that all types of traffic (HTTP, HTTPS, etc.) are blocked.
<img width="1315" height="987" alt="image" src="https://github.com/user-attachments/assets/16979c84-e565-40b0-9963-3715add86cbf" />


### Step 6: Configure Remote IP Addresses

Select "These IP addresses" under Remote IP address and add the IPs obtained using nslookup.

Example:
- 104.17.185.195
- 104.17.186.195
- 104.17.187.195
- 104.17.188.195
- 104.17.189.195

This step defines which destination servers should be blocked.

<img width="1313" height="979" alt="image" src="https://github.com/user-attachments/assets/85c4e40b-4079-4494-ab97-3aec2f854eb0" />

### Step 7: Select Action as "Block the Connection"

This ensures that any traffic matching the rule is denied.
<img width="1318" height="990" alt="image" src="https://github.com/user-attachments/assets/ba8c40e2-aab1-4b0d-92dd-d6004991ca1e" />
### Step 8: Apply Rule to All Profiles

Select Domain, Private, and Public profiles.

This ensures the rule is active on all network types.
<img width="1305" height="989" alt="image" src="https://github.com/user-attachments/assets/0e97b16c-c963-4ea4-bf89-07f6074f9527" />
**
### Step 9: Name the Rule

Provide a descriptive name such as "Block BookMyShow".

This helps in identifying and managing the rule later.
<img width="1915" height="1028" alt="image" src="https://github.com/user-attachments/assets/50f7ab3f-772a-4c8e-9716-e965abc7d2bf" />

![Uploading image.png…]()

Note ; SOmetimes even with these changs , it is possible that the website might nto get blocked.
