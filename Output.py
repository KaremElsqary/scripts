def process_domain(domain, words):
    processed_domains = []
    for word in words:
        processed_domain = f"{domain}?{word}=\">karem"
        processed_domains.append(processed_domain)
    return processed_domains


def main():

    # Update with the path to your test file
    
    file_path = r"C:\Users\Karem\OneDrive\Desktop\words.txt"
    domain = input("Enter the domain: ")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        words = [word.strip() for line in lines for word in line.split(",")]
    
    processed_domains = process_domain(domain, words)
    for processed_domain in processed_domains:
        print(processed_domain)


if __name__ == "__main__":
    main()
