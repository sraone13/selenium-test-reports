import pytest
import os
import datetime

# Generate a unique report filename using a timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_filename = f"report_{timestamp}.html"

def test_google():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

if __name__ == "__main__":
    # Run pytest and generate the report with a unique filename
    pytest.main(["-v", f"--html={report_filename}"])
    
    # Call the upload script with the filename as an argument
    os.system(f"python upload_to_github.py {report_filename}")
