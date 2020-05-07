import factory

import tests.factories.common as common
from app.models.panel_permission import PanelPermission, db


class PanelPermissionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = PanelPermission
        sqlalchemy_session = db.session

    panel_name = common.string_
    can_access = True
