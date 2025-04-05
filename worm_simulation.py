import random
import json
import csv

IP_RANGE = 100000
SCAN_RATE = 2


def initialize_ips():
    status = {
        "infected": {},
        "vulnerable": [],
    }

    # Initialize IPs
    for ip in range(1, IP_RANGE+1):
        if ip == 4009:
            status["infected"][ip] = 0
        elif 1 <= ip % 1000 <= 10:
            status["vulnerable"].append(ip)
    return status


def code_red(status):
    
    tick = 1
    while True:
        for ip, infected_tick in list(status["infected"].items()):
            for _ in range(SCAN_RATE):
                if infected_tick <= tick+30:
                    target = random.randint(1, IP_RANGE+1)
                    infect_ip(status, target, tick)
        
        if status["vulnerable"] == []:
            print("All vulnerable IPs have been infected.")
            break

        tick += 1
    
    # Save infection data as CSV
    with open("infected_ips.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Infected_Tick", "IP"])
        for ip, infected_tick in sorted(status["infected"].items()):
            writer.writerow([infected_tick, ip])


def code_red_II(status):
    tick = 1
    while True:
        for ip, infected_tick in list(status["infected"].items()):
            for _ in range(SCAN_RATE):
                if infected_tick <= tick+30:
                    if random.random() < 0.5:
                        target = random.randint(ip-10, ip+10+1)
                    else:
                        target = random.randint(1, IP_RANGE+1)
                    infect_ip(status, target, tick)
        
        if status["vulnerable"] == []:
            print("All vulnerable IPs have been infected.")
            break

        tick += 1


def infect_ip(status, target_ip, tick):
    if target_ip in status["infected"]:
        return

    if target_ip in status["vulnerable"]:
        status["infected"][target_ip] = tick + 1
        status["vulnerable"].remove(target_ip)
        print(f"IP {target_ip} is infected.")

def main():

    # Simulate Code Red worm
    status = initialize_ips()
    code_red(status)

    # Simulate Code Red II worm
    status = initialize_ips()
    code_red_II(status)
        

if __name__ == "__main__":
    main()
