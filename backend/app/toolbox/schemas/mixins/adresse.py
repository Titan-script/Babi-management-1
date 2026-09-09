from app.common import BaseModel, Field, Optional, datetime


class AddressSchemaMixin(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = Field(default="Côte d'Ivoire")


class GeolocSchemaMixin(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude GPS")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude GPS")
    altitude: float | None = Field(default=0.0, description="Altitude en mètres")
    speed: float | None = Field(default=0.0, ge=0.0, description="Vitesse en km/h")
    timestamp: datetime
