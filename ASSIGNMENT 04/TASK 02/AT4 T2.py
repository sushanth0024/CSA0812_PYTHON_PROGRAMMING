
import io

# Simulated daily attendance files
files = {
    "day1.txt":
    "192311001,2026-10-01,P\n"
    "192311002,2026-10-01,A\n"
    "192311003,2026-10-01,P\n",

    "day2.txt":
    "192311001,2026-10-02,P\n"
    "192311002,2026-10-02,P\n"
    "192311003,2026-10-02,X\n"
}

attendance = {}
errors = []

for filename, content in files.items():
    file = io.StringIO(content)

    for line_no, line in enumerate(file, start=1):
        try:
            parts = line.strip().split(",")

            if len(parts) != 3:
                raise ValueError("Invalid number of fields")

            reg_no, date, status = parts

            if status not in ("P", "A"):
                raise ValueError("Invalid status")

            if reg_no not in attendance:
                attendance[reg_no] = [0, 0]

            if status == "P":
                attendance[reg_no][0] += 1
            else:
                attendance[reg_no][1] += 1

        except ValueError as error:
            errors.append(
                (filename, line_no, str(error))
            )

    file.close()

print("ATTENDANCE REPORT")

for reg_no, values in attendance.items():
    present, absent = values
    total = present + absent
    percentage = present / total * 100

    print(reg_no, ":", round(percentage, 2), "%")

    if percentage < 75:
        print("Below 75% attendance")

print("\nDAMAGED LINE REPORT")

for error in errors:
    print(error)

# Simulated output report files
report = io.StringIO()
for reg_no, values in attendance.items():
    present, absent = values
    percentage = present / (present + absent) * 100
    report.write(f"{reg_no}: {percentage:.2f}%\n")

error_report = io.StringIO()
for error in errors:
    error_report.write(str(error) + "\n")

print("\nREPORT FILE CONTENT:")
print(report.getvalue())

print("ERROR FILE CONTENT:")
print(error_report.getvalue())

report.close()
error_report.close()
