from typing import Optional

from sqlmodel import Relationship

from app.toolbox import BackgroundAssetMixin, BaseTenant, LogoAssetMixin


class OrgTheme(BaseTenant, LogoAssetMixin, BackgroundAssetMixin, table=True):
    __tablename__ = "org_themes"

    # Identité visuelle
    primary_color: str = "#2563eb"
    secondary_color: str = "#ffffff"

    # Styles UI
    button_style: str = "ROUNDED"  # "ROUNDED", "SQUARE", "PILL"
    card_style: str = "MODERN"  # "MODERN", "FLAT", "SHADOW"
    navigation_type: str = "BOTTOM_NAV"

    org: Optional["Organization"] = Relationship(back_populates="theme")
