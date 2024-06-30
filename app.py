import os
import json
import mail_server
from flask import Flask, url_for, request, redirect, render_template
from datetime import datetime,timezone,timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add.html", methods = ['GET', 'POST'])
def add():

    with open("news.json", "r", encoding="utf-8") as read_number:
        serial_number = json.load(read_number)
    
    max_number_list = max(serial_number, key=lambda x: int(x["number"]))
    max_number = max_number_list["number"]
    add_number = int(max_number) + 1

    if request.method == 'POST':

        add_content = request.values['content']

        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
        add_time = dt2.strftime("%Y-%m-%d %H:%M:%S")

        message_data = {
            'number': add_number,
            'content': add_content,
            'created_at': add_time,
        }
        
        if os.path.exists('news.json') and os.path.getsize('news.json') > 0:
            with open("news.json", "r", encoding="utf-8") as load_file:
                messages = json.load(load_file)
        else:
            messages = []

        messages.append(message_data)

        with open("news.json", "w", encoding="utf-8") as dump_file:
            json.dump(messages, dump_file, indent=4)

        #if you want to send email when the send button be put
        # mail_server.send_message(add_number, add_content)

        read_number.close()
        return redirect(url_for('post'))
    
    return render_template("add.html", add_number = add_number)

@app.route("/post.html", methods = ['GET', 'POST'])
def post():

    with open ("news.json", "r", encoding="utf-8") as read_file:
        messages = json.load(read_file)

    with open("comment.json", "r", encoding="utf-8") as load2_file:
        replyss = json.load(load2_file)

    if request.method == 'POST':

        snumber = request.values["stex-number"]
        nickname = request.values["nickname"]
        reply_content = request.values["comment_reply"]

        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
        add_time = dt2.strftime("%Y-%m-%d %H:%M:%S")

        reply_data = {
            "number": int(snumber),
            "nickname": nickname,
            "content": reply_content,
            "time": add_time
        }

        if os.path.exists('comment.json') and os.path.getsize('comment.json') > 0:
            with open("comment.json", "r", encoding="utf-8") as load_file:
                reply = json.load(load_file)
        else:
            reply = []

        reply.append(reply_data)

        with open("comment.json", "w", encoding="utf-8") as dump_file:
            json.dump(reply, dump_file, indent=4)

        read_file.close()
        load2_file.close()
        return redirect(url_for('post'))

    reverse = sorted(messages, key=lambda x: x["number"], reverse=True)

    return render_template("post.html", messages = reverse, replyss = replyss)

@app.route("/support.html", methods = ['GET', 'POST'])
def support():

    if request.method == 'POST':

        type = request.values["account"]
        nickname = request.values["name"]
        content = request.values["content"]

        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
        add_time = dt2.strftime("%Y-%m-%d %H:%M:%S")

        message_data = {
            'type': type,
            'nickname': nickname,
            'content': content,
            'time': add_time
        }

        if os.path.exists('support.json') and os.path.getsize('support.json') > 0:
            with open("support.json", "r", encoding="utf-8") as load_file:
                messages = json.load(load_file)
        else:
            messages = []

        messages.append(message_data)

        with open("support.json", "w", encoding="utf-8") as dump_file:
            json.dump(messages, dump_file, indent=4)

        dump_file.close()
    return render_template("support.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)