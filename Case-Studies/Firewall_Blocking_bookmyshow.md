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
![Uploading image.png…]()

