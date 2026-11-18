
import io

# Sample file content stored in memory
virtual_files = {
    "mess_oct.txt":
    "192311001,Ravi,1250.50\n"
    "192311002,Arun,1400\n"
    "192311003,Meena,abc\n"
    "192311004,Divya,1200\n"
}

def process_file(filename):
    total = 0.0
    report = []
    rejected = []

    try:
        file = io.StringIO(virtual_files[filename])

        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                parts = line.split(",")

                if len(parts) != 3:
                    raise ValueError("Expected 3 fields")

                reg_no, name, amount = parts
                amount = float(amount)

                total += amount
                report.append(name + " " + str(amount))

            except ValueError as error:
                rejected.append((line_number, line, str(error)))

        file.close()

        print("MESS BILL REPORT")
        for item in report:
            print(item)

        print("Total Amount:", round(total, 2))

        print("\nRejected Records:")
        for item in rejected:
            print(item)

    except KeyError:
        print("File not found:", filename)

process_file("mess_oct.txt")
