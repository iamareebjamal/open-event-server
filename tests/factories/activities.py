import factory

import tests.factories.common as common
from app.models.activity import Activity, db


class ActivityFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Activity
        sqlalchemy_session = db.session

    actor = common.string_
    action = common.string_
