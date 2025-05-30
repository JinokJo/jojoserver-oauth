from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/oauth2callback")
def oauth2callback():
    code = request.args.get("code")
    if not code:
        return "❌ 인증 코드 없음", 400

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>인증 코드 반환</title>
        <style>
            textarea {{
                width: 90%;
                height: 80px;
                font-size: 16px;
                padding: 10px;
                margin-bottom: 10px;
            }}
            button {{
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h2>✅ 인증 코드 반환</h2>
        <p>아래 코드를 복사하여 전자액자 설정페이지에 입력하세요.</p>
        <textarea id="codeBox" readonly>{code}</textarea><br>
        <button onclick="copyCode()">📋 복사하기</button>

        <script>
            function copyCode() {{
                var copyText = document.getElementById("codeBox");
                copyText.select();
                copyText.setSelectionRange(0, 99999); // 모바일 대응
                document.execCommand("copy");
                alert("복사되었습니다!");
            }}
        </script>
    </body>
    </html>
    """)

@app.route("/privacy")
def privacy():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>개인정보처리방침</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto; }
        </style>
    </head>
    <body>
        <h1>개인정보처리방침</h1>
        <p>이 앱은 사용자 정보를 저장하거나 추적하지 않습니다.</p>
        <p>Google OAuth 인증을 위해 사용자 이메일을 식별 목적으로만 사용합니다.</p>
        <p>저장된 토큰은 사용자 디바이스 내에서만 사용되며 외부 서버로 전송되지 않습니다.</p>
        <p>기타 문의: contact@jojoserver.com</p>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/terms")
def terms():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>서비스 이용약관</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto; }
        </style>
    </head>
    <body>
        <h1>서비스 이용약관</h1>
        <p>이 서비스는 Google OAuth 인증을 통해 사용자 계정을 연동합니다.</p>
        <p>이용자는 본인의 Google 계정 정보를 통해 인증하며, 인증 과정에서 발급된 토큰은 로컬 디바이스에 저장됩니다.</p>
        <p>본 서비스는 사용자 데이터를 외부로 전송하지 않으며, Google API 사용 정책을 따릅니다.</p>
        <p>이용자는 언제든지 연동된 계정을 해제할 수 있습니다.</p>
        <p>기타 문의: contact@jojoserver.com</p>
    </body>
    </html>
    """
    return render_template_string(html)
