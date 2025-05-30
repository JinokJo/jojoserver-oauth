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
        <p>아래 코드를 복사하여 라즈베리파이에 입력하세요.</p>
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
