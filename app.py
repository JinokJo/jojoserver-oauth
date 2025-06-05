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
        <title>인증 코드 발급</title>
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
        <h2>✅ 인증 코드 발급완료!</h2>
        <p>아래 코드를 복사하여 전자액자 설정페이지에 입력하세요.</p>
        <textarea id="codeBox" readonly>{code}</textarea><br>
        <button onclick="copyCode()" style="font-weight: bold;">📋 복사하기</button>

        <script>
            function copyCode() {{
                var copyText = document.getElementById("codeBox");
                copyText.select();
                copyText.setSelectionRange(0, 99999); // 모바일 대응
                document.execCommand("copy");
                alert("✅ 복사되었습니다.");
                window.close();  // 🔴 창 닫기 시도
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
    
        <h2>1. Google 계정 연동 시 수집하는 정보</h2>
        <p>사용자가 Google 계정으로 서비스를 연동할 경우, Google OAuth 2.0 인증을 통해 다음과 같은 정보가 수집될 수 있습니다.</p>
        <ul>
            <li>Google 계정 식별자 (예: 이메일 주소)</li>
            <li>액세스 토큰 및 리프레시 토큰</li>
            <li>Google Drive, Google Photos, Gmail 등 사용자가 명시적으로 동의한 범위 내 정보</li>
        </ul>
        <p>이 정보는 사용자 인증 및 서비스 연동 기능 제공에만 사용되며, 사용자 동의 없이 다른 목적으로 활용되지 않습니다.</p>
    
        <h2>2. 수집한 정보의 이용 목적</h2>
        <ul>
            <li>Google Drive / Google Photos 등 외부 서비스 연동</li>
            <li>사용자 별 맞춤 콘텐츠 제공</li>
            <li>연동 상태 확인 및 유지</li>
            <li>액세스 토큰을 통한 주기적인 동기화</li>
        </ul>
    
        <h2>3. OAuth 토큰 저장 및 보안 조치</h2>
        <ul>
            <li>액세스 토큰과 리프레시 토큰은 사용자의 디바이스 또는 내부 저장소(<code>/home/pi/token/</code>)에 암호화된 파일로 안전하게 저장됩니다.</li>
            <li>토큰 저장 시 Google 사용자 이메일을 기준으로 파일명이 생성되며, 이를 통해 사용자 구분 및 관리가 용이합니다.</li>
            <li>본 시스템은 제3자 서버에 인증 정보를 전송하지 않으며, 모든 인증 및 저장은 사용자 디바이스 내에서만 수행됩니다.</li>
            <li>인증 흐름은 <code>http://localhost:7733/oauth2callback</code>과 같은 로컬 리디렉션 URI를 사용하여 외부 노출을 최소화합니다.</li>
        </ul>
    
        <h2>4. 사용자 권리</h2>
        <ul>
            <li>사용자는 언제든지 연결된 Google 계정을 해제하거나, 저장된 인증 정보를 삭제할 수 있습니다.</li>
            <li>Google 계정의 권한은 Google 계정의 보안 설정 페이지 (<a href="https://myaccount.google.com/permissions" target="_blank">https://myaccount.google.com/permissions</a>)에서 철회할 수 있습니다.</li>
        </ul>
    
        <h2>5. 제3자 제공 없음</h2>
        <p>본 서비스는 사용자의 Google OAuth 인증 정보를 외부에 제공하지 않으며, 제3자 서버를 통한 중계 또는 수집을 하지 않습니다.</p>
    
        <h2>6. 보안 책임</h2>
        <p>Google OAuth 인증 과정에서 수집된 정보는 보안 강화를 위해 다음과 같은 조치를 취하고 있습니다.</p>
        <ul>
            <li>로컬 인증 서버는 HTTPS 기반 Flask 로컬 서버로만 작동</li>
            <li>Google API 요청은 최소 권한 범위(Scope)만 요청</li>
            <li>정기적 토큰 무효화 및 만료 시 사용자 재인증 요구</li>
        </ul>
    
        <h2>7. 삭제 및 해지 처리</h2>
        <p>사용자가 Google 연동을 해제하거나 서비스 탈퇴를 요청하는 경우, 해당 사용자의 모든 OAuth 관련 정보(토큰, 연동 설정 등)는 즉시 삭제됩니다.</p>
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
    
        <h2>제1조 (목적)</h2>
        <p>본 약관은 사용자가 본 애플리케이션(이하 "서비스")에서 제공하는 Google 계정 연동 및 외부 서비스 연결 기능을 이용함에 있어, 회사와 사용자 간의 권리, 의무 및 책임사항을 규정함을 목적으로 합니다.</p>
    
        <h2>제2조 (용어의 정의)</h2>
        <ul>
            <li>“서비스”란 사용자가 Google 계정을 연동하여 Google Drive, Google Photos 등 외부 자원을 연결할 수 있도록 제공되는 일련의 기능을 의미합니다.</li>
            <li>“이용자”란 본 약관에 따라 서비스를 이용하는 개인 또는 단체를 의미합니다.</li>
            <li>“인증정보”란 OAuth 2.0 인증을 통해 생성된 액세스 토큰, 리프레시 토큰, 이메일 주소 등 Google 인증 과정에서 수집되는 정보를 의미합니다.</li>
        </ul>
    
        <h2>제3조 (서비스의 제공)</h2>
        <ul>
            <li>회사는 사용자가 Google 계정을 통해 본인의 데이터를 연동할 수 있도록 OAuth 2.0 기반 인증 기능을 제공합니다.</li>
            <li>Google 인증을 통해 수집된 정보는 서비스 연동, 동기화 등의 기능 제공 외 다른 목적으로 사용되지 않습니다.</li>
            <li>토큰 및 계정 정보는 사용자의 디바이스 내에 안전하게 저장되며, 외부 서버로 전송되지 않습니다.</li>
        </ul>
    
        <h2>제4조 (이용자의 의무)</h2>
        <ul>
            <li>이용자는 본인의 Google 계정을 스스로의 책임하에 사용해야 하며, 인증 정보의 유출이나 무단 사용에 대해 책임을 져야 합니다.</li>
            <li>이용자는 타인의 정보를 무단으로 도용하거나 허위 정보를 입력해서는 안 됩니다.</li>
            <li>서비스를 통해 제공되는 정보를 무단으로 수집, 복제, 유포해서는 안 됩니다.</li>
        </ul>
    
        <h2>제5조 (금지행위)</h2>
        <p>이용자는 다음 각 호에 해당하는 행위를 해서는 안 됩니다.</p>
        <ul>
            <li>타인의 Google 계정을 무단으로 사용하는 행위</li>
            <li>본 서비스의 시스템, 보안을 침해하거나 무단으로 접근하려는 행위</li>
            <li>서비스 제공 목적에 반하는 자동화 프로그램, 스크립트 등을 사용하는 행위</li>
            <li>Google OAuth 정책을 위반하는 행위</li>
        </ul>
    
        <h2>제6조 (계정 연동 및 해제)</h2>
        <ul>
            <li>사용자는 언제든지 Google 계정 연동을 해제할 수 있으며, 이 경우 해당 계정에 대한 인증정보는 즉시 삭제됩니다.</li>
            <li>Google 계정 권한 해지는 <a href="https://myaccount.google.com/permissions" target="_blank">https://myaccount.google.com/permissions</a> 에서 직접 처리할 수 있습니다.</li>
        </ul>
    
        <h2>제7조 (책임 제한)</h2>
        <ul>
            <li>회사는 사용자의 기기에서 발생한 인증 정보 유출, 저장 오류, 권한 설정 오류 등에 대해 책임을 지지 않습니다.</li>
            <li>Google API 또는 외부 서비스의 변경 또는 장애로 인해 발생한 문제에 대해 회사는 책임을 지지 않습니다.</li>
        </ul>
    
        <h2>제8조 (약관의 변경)</h2>
        <p>본 약관은 서비스 기능 개선, 관련 법령 개정 등에 따라 사전 고지 후 변경될 수 있습니다. 변경된 약관은 서비스 화면 또는 홈페이지를 통해 고지하며, 변경 이후에도 서비스를 계속 사용할 경우 변경에 동의한 것으로 간주합니다.</p>
    
        <h2>제9조 (문의)</h2>
        <p>서비스 이용 중 궁금한 점이나 불편 사항은 아래로 문의 주시기 바랍니다.</p>
        <p>이메일: <a href="mailto:developer@jojoserver.com">developer@jojoserver.com</a></p>
    
        <p><strong>시행일자:</strong> 2025년 5월 30일</p>
    </body>
    </html>
    """
    return render_template_string(html)
