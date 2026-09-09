from app.common import Field, SQLModel, datetime, timezone


class LocationLiveMixin(SQLModel):
    latitude: float
    longitude: float
    altitude: float | None = Field(default=0.0)  # En mètres
    speed: float | None = Field(default=0.0)  # En km/h
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
