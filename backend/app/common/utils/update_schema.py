from typing import Any, Optional

from pydantic import create_model


def create_update_schema(base_schema: Any):
    """
    Transforme tous les champs d'un schéma en Optional.
    """
    fields = {
        name: (Optional[field.annotation], None) for name, field in base_schema.model_fields.items()
    }
    return create_model(f"{base_schema.__name__}Update", **fields)
