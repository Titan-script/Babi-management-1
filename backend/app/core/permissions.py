from fastapi import Depends, HTTPException, status


def require_access(role: str = None, feature: str = None, resource: str = None, action: str = None):
    from .deps import get_auth_context
    from .roles import get_role_for

    """
    Dépendance universelle de contrôle d'accès :
    - Vérifie si l'organisation est bloquée ou expirée.
    - Vérifie le rôle (soit explicitement fourni, soit déduit via resource/action).
    - Vérifie si la feature est incluse dans l'abonnement SaaS.
    """

    def dependency(auth: dict = Depends(get_auth_context)):
        user = auth["user"]
        org = auth["organisation"]

        # 1. Vérification blocage global de l'organisation
        if getattr(org, "is_blocked", False) or getattr(org, "subscription_expired", False):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Accès suspendu : Organisation bloquée ou abonnement expiré.",
            )

        # 2. Détermination du rôle requis
        target_role = role
        if not target_role and resource and action:
            target_role = get_role_for(resource, action)

        # 3. Vérification Rôle (RBAC)
        if target_role and user.role.name != "Admin" and user.role.name != target_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Accès refusé : Rôle '{target_role}' requis.",
            )

        # 4. Vérification Feature (Abonnement SaaS)
        target_feature = feature or resource  # Par défaut, la ressource peut être la feature
        if target_feature:
            features_list = getattr(org.plan, "features_list", []) if org.plan else []
            if hasattr(org, "has_feature"):
                has_feat = org.has_feature(target_feature)
            else:
                has_feat = target_feature in features_list

            if not has_feat:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Module '{target_feature}' non inclus dans votre abonnement.",
                )

        return auth

    return dependency
