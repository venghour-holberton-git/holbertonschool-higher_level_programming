import os

def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            print("template is not a string")
            return
        if isinstance(attendees, list) and all(isinstance(att, dict) for att in attendees):
            print ("attendees type error")
            return
        if len(template) <= 0:
            print("Template is empty, no output files generated.")
            return
        if len(attendees) == 0 or attendees == None:
            print("No data provided, no output files generated.")
            return
        index = 1
        for attendee in attendees:
            fileContent = template.format(
                name = attendee["name"] if "name" in attendee and attendee["name"] != None else "N/A",
                event_title = attendee["event_title"] if "event_title" in attendee and attendee["event_title"] != None else "N/A",
                event_date = attendee["event_date"] if "event_date" in attendee and attendee["event_date"] != None else "N/A",
                event_location = attendee["event_location"] if "event_location" in attendee and attendee["event_location"] != None else "N/A"
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