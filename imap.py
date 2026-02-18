import imaplib
import keys
import email
import ollama


imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("dollardev05@gmail.com", keys.email_api_key)
imap.select("inbox")

status, messages = imap.search(None, "ALL")
last_5 = messages[0].split()[::-1][:5]
print(last_5)
for i in range(5):
    status, msg_data = imap.fetch(last_5[i], "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            email_body = part.get_payload(decode=True).decode('utf-8')
            response = ollama.generate(
                model='deepseek-r1:latest',
                prompt=f"{email_body} this is an email i got can you summarize this into a short brief summary and then give me actionable steps",
                options={
                    'temperature': 0.8,
                    'num_ctx': 4096  # Set a custom context length
                }
)
            print(response['response'])

        