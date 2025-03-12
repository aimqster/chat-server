from flask import Flask, request

app = Flask(__name__)

# ��� ������ �������
CHAT_LOG = "chat.txt"

# ���� ������
@app.route("/")
def home():
    return "������! ������� ���� ����� ??"

# ����� �����
@app.route("/send", methods=["POST"])
def send():
    data = request.json
    username = data.get("username")
    message = data.get("message")

    if not username or not message:
        return {"status": "error", "message": "��� ����� ��� �������� ��������"}

    with open(CHAT_LOG, "a", encoding="utf-8") as file:
        file.write(f"{username}: {message}\n")

    return {"status": "success", "message": "�� ����� �������!"}

# ������� �������
@app.route("/messages")
def messages():
    try:
        with open(CHAT_LOG, "r", encoding="utf-8") as file:
            chat = file.readlines()
        return {"status": "success", "messages": chat}
    except FileNotFoundError:
        return {"status": "success", "messages": []}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
