import time
from selenium import webdriver
import mysql.connector

def insert_into_database(metrics):
    # Initialize MySQL connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ronaldinho10!",  
        database="metrics_database"
    )
    cursor = connection.cursor()

    try:
        # Insert metrics into the database
        for metric in metrics:
            query = "INSERT INTO metrics (`TIMESTAMP (HH/MM/SS)`, `presence_time`, `scrolling`) VALUES (%s, %s, %s)"
            values = (metric["TIMESTAMP (HH:MM:SS)"], metric["Presence time (Seconds)"], metric["Scrolling (Pixels)"])
            cursor.execute(query, values)

        # Commit changes
        connection.commit()

    finally:
        # Close MySQL connection
        cursor.close()
        connection.close()

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
        metrics.append({
            "TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
            "Presence time (Seconds)": presence_time,
            "Scrolling (Pixels)": current_scroll / scroll_height
        })

        count += 1
        time.sleep(2)

    # Close the browser
    driver.quit()

    # Insert metrics into the MySQL database
    insert_into_database(metrics)


if __name__ == "__main__":
    main()
