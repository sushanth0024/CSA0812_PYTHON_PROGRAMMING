
import io

# Simulated input files
day_files = {
    "day1.txt": "Python Basics\nData Structures",
    "day2.txt": "Computer Networks\nOperating Systems",
    "day3.txt": "Machine Learning\nArtificial Intelligence"
}

# Simulated output files
returns_log = io.StringIO()
error_log = io.StringIO()


def save_returns(books):
    for book in books:
        returns_log.write(book + "\n")


def process(day_file):
    try:
        if day_file not in day_files:
            raise FileNotFoundError(day_file)

        with io.StringIO(day_files[day_file]) as file:
            books = file.read().splitlines()

        save_returns(books)
        print(day_file, "processed successfully")

    except FileNotFoundError as error:
        print("Missing file:", day_file)
        error_log.write(str(error) + "\n")

    except OSError as error:
        print("File error:", error)
        error_log.write(str(error) + "\n")


# Process three days
for filename in day_files:
    process(filename)

# Test missing file
process("day4.txt")

print("\nFINAL RETURNS LOG")
print(returns_log.getvalue())

print("ERROR LOG")
print(error_log.getvalue())

returns_log.close()
error_log.close()
