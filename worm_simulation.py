import random
import csv

IP_RANGE = 100000
SCAN_RATE = 2

def initialize_ips():
    """
    Initialize the IPs and their statuses.
    The vulnerable IPs are the ones whose last three digits are 001-010 in each 1000.
    The initially infected machine is IP 4009 (infected at tick 0).
    """
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


def code_red(status:dict, run:int):
    """
    Simulate the Code Red worm infection process.
    The worm scans the entire IP range and infects vulnerable machines.
    """
    tick = 0

    # Record I(0): the number of infected machines at each tick
    it_counts = [(tick, sum(1 for t in status["infected"].values() if t <= tick))]

    while status["vulnerable"]:
        tick += 1
        for ip, infected_tick in list(status["infected"].items()):
            for _ in range(SCAN_RATE):
                if tick >= infected_tick+30:
                    target = random.randint(1, IP_RANGE)
                    infect_ip(status, target, tick)
        active_infections = sum(1 for t in status["infected"].values() if t <= tick)
        it_counts.append((tick, active_infections))
    
    # Save infection data as CSV
    with open(f"code_red_{run}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Tick", "Infected_Count"])
        for tick, count in it_counts:
            writer.writerow([tick, count])


def code_red_II(status:dict, run:int):
    """
    Simulate the Code Red II worm infection process.
    The worm scans a range of 20 IPs around the infected machine or randomly selects a target.
    """
    tick = 0

    # Record I(0): the number of infected machines at each tick
    it_counts = [(tick, sum(1 for t in status["infected"].values() if t <= tick))]

    while status["vulnerable"]:
        tick += 1
        for ip, infected_tick in list(status["infected"].items()):
            for _ in range(SCAN_RATE):
                if tick >= infected_tick+30:
                    if random.random() < 0.5:
                        target = random.randint(ip-10, ip+10)
                    else:
                        target = random.randint(1, IP_RANGE)
                    infect_ip(status, target, tick)
        active_infections = sum(1 for t in status["infected"].values() if t <= tick)
        it_counts.append((tick, active_infections))

    # Save infection data as CSV
    with open(f"code_red_II_{run}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Tick", "Infected_Count"])
        for tick, count in it_counts:
            writer.writerow([tick, count])


def infect_ip(status, target_ip, tick):
    """
    Infect a target IP if it is vulnerable.
    If the target IP is already infected, do nothing.
    """
    if target_ip in status["infected"]:
        return

    if target_ip in status["vulnerable"]:
        status["infected"][target_ip] = tick + 1
        status["vulnerable"].remove(target_ip)
        print(f"IP {target_ip} is infected.")

if __name__ == "__main__":
    # Simulate Code Red worm three times
    for run in range (1, 3+1):
        # Simulate Code Red worm
        status = initialize_ips()
        code_red(status, run)

    # Simulate Code Red II worm three times
    for run in range(1, 3+1):
        # Simulate Code Red II worm
        status = initialize_ips()
        code_red_II(status, run)
