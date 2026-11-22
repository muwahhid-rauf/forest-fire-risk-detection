import serial
import csv
import time


port = "COM3"

baud_rate = 115200

ser = serial.Serial(port, baud_rate, timeout=1)


with open("fire_risk_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    

    writer.writerow(["Time", "Temperature", "Light"])

    print("Collecting data... Press Ctrl+C to stop")

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()

            if line:
                print(line)

              

                temp = parts[0].split(":")[1]
                light = parts[1].split(":")[1]

                current_time = time.strftime("%H:%M:%S")

                writer.writerow([current_time, temp, light])

    except KeyboardInterrupt:
        print("Data collection stopped")

ser.close()