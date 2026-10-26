import csv
import socket
import logging
import argparse
logging.basicConfig(
    filename="scanner.log",
    level=logging.INFO,format="%(asctime)s:%(levelname)s:%(message)s"
)
target=["127.0.0.1","192.168.1.1"]
ports=[22,80,443,8000,8080]
with open("scan_results.csv","w",newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["IP Address","Port","Status"])

    for targets in target:
        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)

                result = s.connect_ex((targets, port))

                if result == 0:
                    status = "OPEN"
                else:
                    status = "CLOSED"

                print(port, status)
                logging.info(f"{targets}-Port {port} - {status}")
                writer.writerow([targets, port, status])

            except socket.error as e:
                print("Socket Error: ",e)
                logging.error(f"{targets}-Port {port} -{e}")

            finally:
                if s is not None:
                    s.close()











