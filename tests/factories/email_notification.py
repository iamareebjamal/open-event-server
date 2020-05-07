import factory

from tests.factories.event import EventFactoryBasic
from tests.factories.user import UserFactory
from app.models.email_notification import EmailNotification, db


class EmailNotificationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = EmailNotification
        sqlalchemy_session = db.session

    user = factory.RelatedFactory(UserFactory)
    event = factory.RelatedFactory(EventFactoryBasic)
    next_event = False
    new_paper = False
    session_accept_reject = False
    session_schedule = True
    after_ticket_purchase = True
    event_id = 1
    user_id = 2
