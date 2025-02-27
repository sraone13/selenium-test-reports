import sys
import os

if len(sys.argv) < 2:
    print("Usage: python upload_to_github.py <report_filename>")
    sys.exit(1)

report_filename = sys.argv[1]

# Run Git commands to upload the report
os.system(f"git add {report_filename}")
os.system(f'git commit -m "Uploaded test report: {report_filename}"')
os.system("git push origin master")

print(f"✅ Successfully uploaded {report_filename} to GitHub!")
