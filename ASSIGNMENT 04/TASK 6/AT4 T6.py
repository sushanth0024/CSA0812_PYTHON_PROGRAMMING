
import io

# Sample department files
department_files = {
    "CSE.txt":
    "192311001,Ravi,CSE,ravi@gmail.com,Singing;Dancing\n"
    "192311002,Arun,CSE,arun@gmail.com,Drama;Singing\n"
    "192311003,Meena,CSE,meenagmail.com,Dancing\n",

    "ECE.txt":
    "192311001,Ravi,ECE,ravi@gmail.com,Singing\n"
    "192311004,Divya,ECE,divya@gmail.com,Painting\n"
    "192311005,Kiran,ECE,kiran@gmail.com\n",

    "EEE.txt":
    "192311006,Anu,EEE,anu@gmail.com,Dancing;Drama\n",

    "IT.txt":
    "192311007,John,IT,john@gmail.com,Painting;Singing\n"
}

departments = ["CSE", "ECE", "EEE", "IT", "MECH"]

students = {}
event_participants = {}
errors = []


def valid_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


for department in departments:
    filename = department + ".txt"

    try:
        if filename not in department_files:
            raise FileNotFoundError(filename)

        with io.StringIO(department_files[filename]) as file:

            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 5:
                        raise ValueError("Invalid number of fields")

                    reg_no, name, dept, email, events = parts

                    if not valid_email(email):
                        raise ValueError("Invalid email")

                    if reg_no in students:
                        errors.append(
                            f"{filename}, Line {line_number}: "
                            f"Duplicate registration {reg_no}"
                        )
                        continue

                    chosen_events = [
                        event.strip()
                        for event in events.split(";")
                        if event.strip()
                    ]

                    if not chosen_events:
                        raise ValueError("No events selected")

                    students[reg_no] = {
                        "name": name,
                        "department": dept,
                        "email": email,
                        "events": chosen_events
                    }

                    for event in chosen_events:
                        event_participants.setdefault(
                            event, []
                        ).append(reg_no)

                except ValueError as error:
                    errors.append(
                        f"{filename}, Line {line_number}: {error}"
                    )

    except FileNotFoundError:
        errors.append(filename + ": Department file missing")

    except OSError as error:
        errors.append(filename + ": " + str(error))


# Create output files in memory
master_list = io.StringIO()
summary_report = io.StringIO()
error_log = io.StringIO()

master_list.write("MASTER STUDENT LIST\n")

for reg_no, details in students.items():
    master_list.write(
        f"{reg_no}, {details['name']}, "
        f"{details['department']}, {details['email']}, "
        f"{';'.join(details['events'])}\n"
    )

summary_report.write("COLLEGE FEST SUMMARY\n")
summary_report.write(
    "Total valid registrations: " + str(len(students)) + "\n"
)

for event, participants in event_participants.items():
    summary_report.write(
        event + ": " + str(len(participants)) + " participants\n"
    )

for error in errors:
    error_log.write(error + "\n")


# Display results
print("VALID REGISTRATIONS:", len(students))

print("\nMASTER LIST")
print(master_list.getvalue())

print("EVENT-WISE PARTICIPANTS")

for event, participants in event_participants.items():
    print(event, ":", participants)

print("\nSUMMARY REPORT")
print(summary_report.getvalue())

print("ERROR LOG")
print(error_log.getvalue())

master_list.close()
summary_report.close()
error_log.close()
