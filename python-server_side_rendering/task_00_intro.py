import os

def generate_invitations(template, attendees):
    try:
        if len(template) <= 0:
            print("Template is empty, no output files generated.")
            return
        if len(attendees) == 0 or attendees == None:
            print("No data provided, no output files generated.")
            return
        index = 1
        for attendee in attendees:
            fileContent = template.format(
                name = attendee["name"] if attendee["name"] != None else "N/A",
                event_title = attendee["event_title"] if attendee["event_title"] != None else "N/A",
                event_date = attendee["event_date"] if attendee["event_date"] != None else "N/A",
                event_location = attendee["event_location"] if attendee["event_location"] != None else "N/A"
            )
            if os.path.exists(f"output_{index}.txt"):
                print("file already exist")
                index+=1
                continue
            with open(f"output_{index}.txt", "w") as f:
                f.write(fileContent)
            index+=1
    except Exception as e:
        print(f"error: {e}")