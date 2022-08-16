from rasa.core.tracker_store import InMemoryTrackerStore
from rasa.core.domain import Domain
from rasa.core.brokers.broker import EventBroker
from typing import Optional

# TODO Implementar trackerstore customizado inserindo e recuperando mensagens e eventos do ElasticSearch
class InMemoryTrackerStore(InMemoryTrackerStore):

    def __init__(
        self, domain: Domain, event_broker: Optional[EventBroker] = None
    ) -> None:
        self.store = {}
        super().__init__(domain, event_broker)