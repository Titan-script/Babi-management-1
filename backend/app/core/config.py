from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    HOST: str = "127.0.0.1"
    PORT: int = 9000
    SENTRY_DSN: str | None = None

    # 1. Config Application & Sécurité

    TITLE_API: str = "Babi Management API"
    VERSION_API: str
    DESCRIPTION_API: str = "API officielle de Babi Management"
    API_V1: str = "/api/v1"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # 2. Base de Données (Celle-ci reste obligatoire)
    DATABASE_URL: str

    # 3. Email (Optionnel pour l'instant)
    MAIL_USERNAME: str | None = None
    MAIL_PASSWORD: str | None = None
    MAIL_FROM: str | None = None
    MAIL_PORT: int = 587
    MAIL_SERVER: str | None = None

    # 4. Paiements & Cloud (Optionnel)
    CINETPAY_API_KEY: str | None = None
    STRIPE_SECRET_KEY: str | None = None

    CLOUDINARY_CLOUD_NAME: str | None = None
    CLOUDINARY_API_KEY: str | None = None
    CLOUDINARY_API_SECRET: str | None = None

    # 5. Notifications (Optionnel)
    SMS_API_KEY: str | None = None
    SMS_API_URL: str | None = None
    SMS_SENDER_NAME: str | None = None

    WHATSAPP_API_URL: str | None = None
    WHATSAPP_API_TOKEN: str | None = None

    TELEGRAM_BOT_TOKEN: str | None = None

    FIREBASE_CREDENTIALS_P: str | None = None

    # 6. Cache & Workers (Redis)
    REDIS_URL: str = "redis://localhost:6379/0"


settings = Settings()
