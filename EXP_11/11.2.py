message = "Call me at 415-555-1011 tomorrow, or at 415-555-9999 for office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Phone number found:", chunk)
