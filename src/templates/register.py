
def template_register(user, password):
    template = f"""
    <html>
        <body>
            <h1> Welcome {user} ! </h1>
            <p > We are excited to have you on board. Your account has been successfully created. Below are your temporary login credentials:</p>
            <p> <strong> Username: </strong> {user} </p>
            <p> <strong> Password: </strong> {password} </p>
            <p> We recommend changing your password as soon as you log in for the first time. </p>
            <p> If you have any questions or need assistance, feel free to contact our support team.</p>
            <p> Thank you for joining us! </p>
        </body>
    </html >
"""
    return template


def template_password(reset_link):
    template = f"""
    <html>
        <body>
            <h2>Hello</h2>
            <p>We have received a request to reset the password for your account. If you did not make this request, you can safely ignore this email.</ p>
            <p>To reset your password, simply click on the following link or copy and paste the URL into your browser:</p>
            <p><a href="{reset_link}">{reset_link}</a></p>
            <p>If you have any questions or need further assistance, please feel free to contact us.</p>
            <p>Thank you,</p>
        </body>
    </html>
"""
    return template
