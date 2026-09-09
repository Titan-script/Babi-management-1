from app.common import Session, event

from .context import current_org_id, current_user_id


@event.listens_for(Session, "before_flush")
def receive_before_flush(session, flush_context, instances_to_flush):
    user_id = current_user_id.get()
    org_id = current_org_id.get()

    for obj in session.new:
        if hasattr(obj, "created_by") and user_id and user_id != 0:
            obj.created_by = user_id
        if hasattr(obj, "org_id") and org_id and org_id != 0:
            obj.org_id = org_id

    for obj in session.dirty:
        if hasattr(obj, "updated_by") and user_id and user_id != 0:
            obj.updated_by = user_id
