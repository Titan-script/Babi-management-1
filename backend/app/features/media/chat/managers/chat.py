from app.features.organization.custom.settings.models.settings import OrgSettings
from app.features.organization.custom.theme.models.theme import OrgTheme
from app.features.organization.identity.tenant.schemas.profil import OrgTenantCreate
from app.features.organization.subscription.billing.models.billing import OrgBilling
from app.features.organization.subscription.plan.models.plan import OrgPlanSubscription


class OrgTenantManager:
    async def register_full_organization(self, data: OrgTenantCreate):
        from app.features.account.identity.user.models.infos import UserInfos
        from app.toolbox.crud.base import BaseCrud

        # Initialisation des sous-CRUD spécifiques si nécessaire
        self.user_crud = BaseCrud(model=UserInfos)
        self.theme_crud = BaseCrud(model=OrgTheme)
        self.settings_crud = BaseCrud(model=OrgSettings)
        self.plan_crud = BaseCrud(model=OrgPlanSubscription)
        self.sub_crud = BaseCrud(model=OrgBilling)

        # 1. Création Organisation
        org = await self.crud.add(**data.org.model_dump())

        # 2. Création Admin (Injecte le rôle et l'org_id)
        admin_data = data.admin.model_dump()
        admin_data.update({"org_id": org.id, "role": "ADMIN"})
        await self.user_crud.add(**admin_data)

        # 3. Initialisation Thème et Settings
        await self.theme_crud.add(org_id=org.id)
        await self.settings_crud.add(org_id=org.id)

        # 4. Abonnement (avec calcul automatique de la date de fin selon le plan et le cycle)
        plan = await self.plan_crud.get_or_404(data.subscription.plan_id)
        sub = self.sub_crud(
            org_id=org.id,
            plan_id=data.subscription.plan_id,
            billing_cycle=data.subscription.billing_cycle,
        )
        sub.set_end_date_from_plan(plan)
        await self.sub_crud.add(sub)

        return org
