
'''''
اسكربت بتديله ملف نصي وكلمه اي خط جوا الملف النصي موجود فيه الكلمه دي هيجمعه في ملف نصي تاني 
مثلا في نتايج بتاعت اداه kxss النتائج اللي انت محتاجها بس هي اللي فيها "> وهكذا 
'''''
import os

# Define path of the input file
input_file = r'C:\Users\Karem\OneDrive\Desktop\3.txt'

# Define the keyword to search for in each line
keyword = ''

# Define path of the output file for removed lines
removed_file = r'C:\Users\Karem\OneDrive\Desktop\3.txt'

# Open the input file in read mode with different encodings
encodings = ['utf-8-sig', 'latin-1', 'cp1252']
for encoding in encodings:
    try:
        with open(input_file, 'r', encoding=encoding) as f_input:
            # Open the output file in write mode with utf-8 encoding for non-removed lines
            with open(input_file + '.tmp', 'w', encoding='utf-8') as f_output:
                # Open the removed lines file in write mode with utf-8 encoding
                with open(removed_file, 'w', encoding='utf-8') as f_removed:
                    # Loop over each line in the input file
                    for line in f_input:
                        # Check if the keyword is in the line
                        if keyword in line:
                            # Write the line to the removed lines file if the keyword is found
                            f_removed.write(line)
                        else:
                            # Write the line to the output file if the keyword is not found
                            f_output.write(line)

        # Remove the original input file
        os.remove(input_file)

        # Rename the temporary output file to the input file name
        os.rename(input_file + '.tmp', input_file)

        # Print a message to indicate the code has finished running
        print('Done!')
        
        # Exit the loop if the code runs successfully
        break

    except UnicodeDecodeError:
        # If a decoding error occurs, try the next encoding in the list
        continue

# Print an error message if none of the encodings work
else:
    print('Error: Unable to decode the')
