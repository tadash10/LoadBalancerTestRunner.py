import os

def generate_report():
    # Generate and display the load test report
    report_path = "results"  # Path to the Gatling report directory
    
    if os.path.exists(report_path):
        print("Generating load test report...")
        
        # Add code here to process the report and display or save the results
        # Based on ISO standards, ensure report generation follows standardized formats
        
        print("Load test report generated.")
    else:
        print("Load test report not found. Please run the load test first.")
