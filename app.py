from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/oauth2callback")
def oauth2callback():
    code = request.args.get("code")
    if not code:
        return "❌ 인증 코드 없음", 400

    try:
        # 라즈베리파이 IP 수정하세요
        requests.post("http://192.168.0.123:7733/receive_code", json={"code": code}, timeout=3)
        msg = "✅ 인증 코드가 라즈베리파이로 전송됨"
    except Exception as e:
        msg = f"❌ 전송 실패: {e}"

    return render_template_string(f"""
    <h2>인증 완료</h2>
    <p>{msg}</p>
    <p>코드: {code}</p>
    """)
