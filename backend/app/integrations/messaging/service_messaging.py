from .tasks.messaging_tasks import task_send_alert, task_send_otp


class MessagingService:
    @staticmethod
    def send_welcome_email(email: str, username: str):
        """Déclenche l'envoi d'un email de bienvenue en arrière-plan."""
        subject = "Bienvenue sur Babi Management !"
        body = f"Bonjour {username}, votre compte a été créé avec succès."
        task_send_alert.delay(email_to=email, subject=subject, body=body)

    @staticmethod
    def send_otp_code(destination: str, code: str):
        """Déclenche l'envoi du code OTP en arrière-plan."""
        task_send_otp.delay(phone_or_email=destination, otp_code=code)
