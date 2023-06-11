'''''
دا بتستخدمه مع اداه paramspider بتديها ملف نصي بليست من الدومانت وهي بتخرجلك ملفات المخفيه في كل الدومنات 
ممكن تعدل فيه وتستخدمه علي اي اداه بس غير المسار الاداه والكوماند بتاع الاداه 
'''''
import subprocess

# Path to ParamSpider directory
paramspider_path = r"C:\Users\Karem\ParamSpider"

# Path to the text file containing domains
domains_file = r"C:\Users\Karem\OneDrive\Desktop\2.txt"

# Output file to save the results
output_file = r"C:\Users\Karem\OneDrive\Desktop\3.txt"

# Read domains from the text file
with open(domains_file, "r") as file:
    domains = file.readlines()

# Remove whitespace and newline characters from each domain
domains = [domain.strip() for domain in domains]

# Loop through each domain and execute ParamSpider
for domain in domains:
    # Construct the ParamSpider command
    command = f"python paramspider.py -d {domain}"
    
    # Execute ParamSpider command and capture the output
    process = subprocess.run(command, cwd=paramspider_path, shell=True, capture_output=True, text=True)
    output = process.stdout
    
    # Append the output to the file
    with open(output_file, "a") as file:
        file.write(output)

print('Finished!')
