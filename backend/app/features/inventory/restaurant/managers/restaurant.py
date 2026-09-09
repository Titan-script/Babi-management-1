from ..models.restaurant import Order
from ..schemas.restaurant import OrderCreate
from ...catalog.models.catalog import Variant
from ..models.restaurant import OrderItem


class OrderManager:
    
    def __init__(self):
        from app.features.account.identity.user.models.infos import UserInfos
        from app.toolbox.crud.base import BaseCrud

        # Initialisation des sous-CRUD spécifiques si nécessaire
        self.order_crud = BaseCrud(model=Order)
        self.variant_crud = BaseCrud(model=Variant)
        self.order_item_crud = BaseCrud(model=OrderItem)

    async def create_order(self, db, data: OrderCreate) -> Order:
        # 1. Créer l'objet Order principal
        order = self.order_crud.add(
            location_reference=data.location_reference,
            status="PENDING",
            preparation_status="PENDING",
            total_amount=0.0,
        )
       
        # 2. Parcourir les articles commandés et les rattacher
        for item_data in data.items:
            variant = self.variant_crud.get_or_404(item_data.variant_id,self.variant_crud.variant_id)

        unit_price = variant.selling_price
        line_total = unit_price * item_data.quantity
        total_amount += line_total

        item = self.order.items.add(
            order_id=order.id,
            variant_id=item_data.variant_id,
            quantity=item_data.quantity,
            unit_price=unit_price,
            notes=item_data.notes
        )

        # 3. Mettre à jour le montant total de la commande
        order=self.order_crud.add(total_amount=total_amount) 
        return order
