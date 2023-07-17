# LoadBalancerTestRunner.py
markdown

# Load Balancer Test Script

This script allows you to perform load testing on a load balancer using Gatling. It provides a menu system to run load tests, generate reports, and perform cleanup tasks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/load-balancer-test.git

    Change into the project directory:

    bash

cd load-balancer-test

Install Gatling (if not already installed) following the official instructions for your platform.

Set the GATLING_HOME environment variable to the path of your Gatling installation:

bash

    export GATLING_HOME=/path/to/gatling

Usage

    Run the script:

    bash

python3 LBTestRunner.py

The script will display a menu with the following options:

    1. Run Load Test: Perform a load test on the specified load balancer.
    2. Generate Report: Generate and display the load test report.
    3. Cleanup: Perform cleanup tasks after the load test.
    4. Exit: Exit the script.
