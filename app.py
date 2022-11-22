import time
import os
import logging
import urllib3

def start_service():
    logging.info("starting service intialization")
    initialize_connections()
    logging.info("starting recieve connections")
    run()

def run():
    while True:
        logging.info("running")
        time.sleep(0.2)

def initialize_connections():
    logging.info("starting service intialization")
    fetch_configuration()
    

def fetch_configuration():
    conn = create_connection()
    return conn

def create_connection():
    return conn_auth()

def conn_auth():
    logging.info("connection verified")

if __name__ == "__main__":
    start_service()