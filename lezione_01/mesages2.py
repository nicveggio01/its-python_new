
def send_messages(messages):
    sent_messages = []
    while messages: 
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
    print("\nAll messages have been sent.")
    return sent_messages
messages = ["ciao", "come va?", "tutto bene?", "oggi che fai?"]
sent_messages = send_messages(messages[:])
print("\nFinal lists:")
print(messages)
print(sent_messages)