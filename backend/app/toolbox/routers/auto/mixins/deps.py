from app.common import Depends


class DepsMixin:
    def _get_deps(self, action: str):
        from app.core import get_auth_context, get_role_for, require_access

        deps = [Depends(get_auth_context)]
        target_role = get_role_for(self.resource, action)
        target_feature = self.required_feature or self.resource

        deps.append(
            Depends(
                require_access(
                    role=target_role, feature=target_feature, resource=self.resource, action=action
                )
            )
        )
        return deps
