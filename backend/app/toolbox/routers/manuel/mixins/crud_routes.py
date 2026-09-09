from app.common import (
    STATUS,
    Any,
    Optional,
    Type,
)

from ...decorators import (
    action_wrapper,
    auto_transaction,
)
from .wrapped import WrappedEndpointMixin


class CrudRoutersMixin:
    def add(
        self,
        path: str,
        method: str,
        action_name: str,
        status_code: int = None,
        response_model: Optional[Type[Any]] = None,
    ):
        """Enregistre une route personnalisée avec injection de session, gestion dynamique et schéma de réponse."""
        method_upper = method.upper()

        if status_code is None:
            if method_upper == "POST":
                status_code = STATUS.CREATED
            elif method_upper == "DELETE":
                status_code = STATUS.NOT_FOUND
            else:
                status_code = STATUS.OK

        method_crud = ["POST", "PATCH", "PUT", "DELETE"]
        safe_func = action_wrapper(self.resource, action_name)(
            WrappedEndpointMixin.wrapped_endpoint
        )
        endpoint = auto_transaction(safe_func) if method_upper in method_crud else safe_func

        # On passe le response_model à add_api_route pour corriger définitivement le Swagger
        self.router.add_api_route(
            path=path,
            endpoint=endpoint,
            methods=[method_upper],
            dependencies=self._get_deps(action_name),
            status_code=status_code,
            response_model=response_model,
        )
