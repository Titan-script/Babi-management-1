from typing import Optional

from app.toolbox import AssetBackgroundMixin, AssetLogoMixin, BaseSchema

# from ..models.theme import OrgTheme
# OrgThemeRead,OrgThemeResponse,OrgThemeUpdate


# ==================== THEME & SETTINGS SCHEMAS ====================
class logo(AssetBackgroundMixin, AssetLogoMixin):
    pass


class OrgThemeBase(logo):
    primary_color: str
    secondary_color: str
    button_style: str
    card_style: str
    navigation_type: str


class OrgThemeRead(OrgThemeBase, BaseSchema):
    pass


class OrgThemeUpdate(BaseSchema, logo):
    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    button_style: Optional[str] = None
    card_style: Optional[str] = None
    navigation_type: Optional[str] = None


class OrgThemeNested(BaseSchema):
    primary_color: str
    secondary_color: str
