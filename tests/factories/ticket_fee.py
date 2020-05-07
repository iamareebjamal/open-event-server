import factory

import tests.factories.common as common
from app.models.ticket_fee import TicketFees, db


class TicketFeesFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = TicketFees
        sqlalchemy_session = db.session

    currency = common.currency_
    service_fee = common.fee_
    maximum_fee = common.fee_
