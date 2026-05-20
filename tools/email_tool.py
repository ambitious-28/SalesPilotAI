import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

def send_email(to_email, subject, body):

    try:

        params = {
            "from": "onboarding@resend.dev",
            "to": [to_email],
            "subject": subject,
            "html": f"<p>{body}</p>"
        }

        email = resend.Emails.send(params)

        return "Email sent successfully"

    except Exception as e:
        return f"Error: {str(e)}"