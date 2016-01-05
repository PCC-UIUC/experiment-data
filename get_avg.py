import re
import sys


def calculate_avg_thp(data):
    throughputs = []
    for line in data:
        match = re.match(
            r'throughput rate ([0-9.]*) mbps', line)
        if match:
            throughput = match.group(1)
            if throughput:
                throughputs.append(float(throughput))
    return sum(throughputs) / len(throughputs)

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        data = f.readlines()
        print calculate_avg_thp(data)
