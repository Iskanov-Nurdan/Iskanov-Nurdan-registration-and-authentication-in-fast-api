from email.message import EmailMessage
import aiosmtplib

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "iskanovnurdan9@gmail.com"
SMTP_PASS = "amhv kwyw baxp xarf" 

async def send_welcome_email(to_email: str, username: str):
    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = to_email
    message["Subject"] = "Добро пожаловать!"
    message.set_content(f"Привет, {username}!\n\nСпасибо за регистрацию на нашем сайте!")

    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASS
        )
    except aiosmtplib.SMTPException as e:
        print(f"Ошибка при отправке письма: {e}")
