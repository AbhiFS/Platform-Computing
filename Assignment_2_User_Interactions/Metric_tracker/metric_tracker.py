import time
from selenium import webdriver
import csv


def writeToCSV(filename: str, metrics: list):
    fieldnames = ["TIMESTAMP (HH:MM:SS)", "Presence time (Seconds)", "Scrolling (Pixels)"]
    with open(filename, mode="w", newline="") as fp:
        # Create a writer object
        writer = csv.DictWriter(fp, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for metric in metrics:
            writer.writerow(metric)


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website
    driver.get("http://localhost:3000/")

    # Initialize variables
    metrics = []  # List to store metrics
    SAMPLE_SIZE = 2
    count = 0
    start_time = time.time()
    while count < SAMPLE_SIZE:
        # Track presence time
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")

        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")

        # Append metric to the list
        metrics.append({ "TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
            "Presence time (Seconds)": presence_time,
            "Scrolling (Pixels)": current_scroll / scroll_height
        })

        count += 1
        time.sleep(2)

    # Close the browser
    driver.quit()

    # Write metrics to CSV file
    writeToCSV("metrics.csv", metrics)


if __name__ == "__main__":
    main()

