import subprocess

def run_load_test():
    endpoint = input("Enter the load balancer endpoint or IP address: ")
    num_users = input("Enter the number of virtual users to simulate: ")
    
    # Execute Gatling command to run the load test
    subprocess.run([
        "sh", 
        f"{GATLING_HOME}/bin/gatling.sh", 
        "-s", "your_simulation_file", 
        "-u", num_users, 
        "-e", 
        "-o", "results"
    ], check=True)
