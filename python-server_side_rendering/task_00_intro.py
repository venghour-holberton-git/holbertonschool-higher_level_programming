def generate_invitations(template, attendees):
    index = 1
    for attendee in attendees:
        fileContent = template.format(
            name = attendee["name"],
            event_title = attendee["event_title"],
            event_date = attendee["event_date"],
            event_location = attendee["event_location"]
        )
        with open(f"output_{index}.txt", "w") as f:
            f.write(fileContent)
        index+=1