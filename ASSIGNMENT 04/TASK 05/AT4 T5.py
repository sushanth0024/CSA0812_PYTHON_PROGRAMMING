
import io

def read_attendance(content):
    records = []

    with io.StringIO(content) as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 3 and parts[2] in ("P", "A"):
                records.append(parts)

    return records


def percentage(records):
    counts = {}

    for reg_no, date, status in records:
        if reg_no not in counts:
            counts[reg_no] = [0, 0]

        if status == "P":
            counts[reg_no][0] += 1
        else:
            counts[reg_no][1] += 1

    result = {}

    for reg_no, values in counts.items():
        total = values[0] + values[1]
        result[reg_no] = values[0] / total * 100

    return result


def consecutive_absences(records):
    dates = {}

    for reg_no, date, status in records:
        dates.setdefault(reg_no, []).append((date, status))

    result = []

    for reg_no, entries in dates.items():
        entries.sort()

        for i in range(len(entries) - 2):
            if all(
                entries[j][1] == "A"
                for j in range(i, i + 3)
            ):
                result.append(reg_no)
                break

    return result


def write_report(result):
    report = io.StringIO()

    for reg_no, value in result.items():
        report.write(f"{reg_no}: {value:.2f}%\n")

    print("\nATTENDANCE REPORT")
    print(report.getvalue())

    report.close()


if __name__ == "__main__":

    data = (
        "192311001,2026-10-01,P\n"
        "192311001,2026-10-02,A\n"
        "192311001,2026-10-03,A\n"
        "192311001,2026-10-04,A\n"
        "192311002,2026-10-01,P\n"
        "192311002,2026-10-02,P\n"
    )

    records = read_attendance(data)
    result = percentage(records)

    write_report(result)

    print("Students absent for 3 consecutive days:")
    print(consecutive_absences(records))
