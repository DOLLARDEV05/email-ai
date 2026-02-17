import imaplib
import email
import codecs
# import regex
import string



imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("dollardev05@gmail.com", "mdjd tfkk pvcj uujk")
# imap.select("inbox")

# status, messages = imap.search(None, "ALL")
# messages = messages[0].split(b' ')
# for mail in messages:
#     _, msg = imap.fetch(mail, "(RFC822)")
#     for response in msg:
#         if isinstance(response, tuple):
#             msg = email.message_from_bytes(response[1])
#             subject = msg["subject"]
#             print(subject)
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     content_type = part.get_content_type()
#                     content_disposition = str(part.get("Content-Disposition"))
#                     try:
#                         body = part.get_payload(decode=True).decode()
#                     except:
#                         pass
#                     if content_type == "text/plain" and "attachment" not in content_disposition:
#                         print(body)
#             else:
#                 content_type = msg.get_content_type()
#                 body = msg.get_payload(decode=True).decode()
#                 if content_type == "text/plain":
#                     print(body) 