class Prefix:
    API = "/api/v1"

    ORG_IDENTITY = "/org/identity"
    ORG_CUSTOM = "/org/custom"
    ORG_SUBSCRIPTION = "/org/subscription"

    ACCOUNT_ACCESS = "/account/access"
    ACCOUNT_CUSTOM = "/account/custom"
    ACCOUNT_IDENTITY = "/account/identity"

    INVENTORY = "/inventory"


PREFIX = Prefix()

__all__ = ["PREFIX"]
