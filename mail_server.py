import smtplib
import email.message

account = ""
password = ""

msg = email.message.EmailMessage()

receiver = ""

msg["From"] = account
msg["To"] = receiver
msg["Subject"] = "XX自動化系統_推送通知"

def send_message(add_number, add_content):

    server = smtplib.SMTP_SSL("Your smtp server", PORT)
    server.login(account, password)

    msg.add_alternative(f'<h2>有人投稿了新貼文</h2><h3>貼文編號: #{add_number}</h3><h3>貼文內容: {add_content}</h3><br><a href="https://example.com/post.html#{add_number}">查看貼文</a><br><a href="https://example.com/">XX網站</a><p style="color: red;">此訊息為系統自動發送! 請勿直接回覆!</p>', subtype="html")
    server.send_message(msg)
    server.close()
