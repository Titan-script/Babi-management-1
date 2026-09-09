ROLE_MAP = {"stocks": {"get": "Staff", "create": "Manager", "update": "Manager", "delete": "Admin"}}


def get_role_for(resource: str, action: str) -> str:
    """
    Traduit une ressource et une action en un rôle requis.
    Ex: resource="stock", action="create" -> retourne "Manager"
    """
    # Si la ressource n'est pas définie, on exige Admin par défaut (sécurité max)
    resource_roles = ROLE_MAP.get(resource, {})
    return resource_roles.get(action, "Admin")
