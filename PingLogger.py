from pythonping import ping
from datetime import datetime
import csv
import time

host = "123.123.123.123"
outputfilename = "missedpings.csv"
timeout = 1;

while True:
    now = datetime.now()
    current_date = now.strftime("%b/%d/%Y")
    current_time = now.strftime("%H:%M:%S")

    response_list = ping(host, size=40, count=1)

    output_string = current_time + " Pinging: " + host + "  Result: " + str(response_list)
    print(output_string)

    if("timed out" not in response_list):
            with open(outputfilename, 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow([current_date, current_time, host])
    time.sleep(timeout)

def writeheader():
    with open(outputfilename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(["Date", "Time", "Host"])

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")