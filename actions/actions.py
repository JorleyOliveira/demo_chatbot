import logging
import datetime
import re
import ruamel.yaml
import pathlib
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, UserUtteranceReverted, EventType
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List

logger = logging.getLogger(__name__)

here = pathlib.Path(__file__).parent.absolute()
handoff_config = (
        ruamel.yaml.safe_load(open(f"{here}/handoff_config.yml", "r")) or {}
).get("handoff_hosts", {})


class ActionHandoffOptions(Action):
    def name(self) -> Text:
        return "action_handoff_options"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:

        if not any(
                [config.get("url") for bot, config in handoff_config.items()]
        ):
            dispatcher.utter_message(template="utter_no_handoff")
        else:
            buttons = [
                {
                    "title": config.get("title"),
                    "payload": f'/trigger_handoff{{"handoff_to":"{bot}"}}',
                }
                for bot, config in handoff_config.items()
            ]
            dispatcher.utter_message(
                text="I can't transfer you to a human, \
                      but I can transfer you to one of these bots",
                buttons=buttons,
            )
        return []


class ActionHandoff(Action):
    def name(self) -> Text:
        return "action_handoff"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:

        dispatcher.utter_message(template="utter_handoff")
        handoff_to = tracker.get_slot("handoff_to")

        handoff_bot = handoff_config.get(handoff_to, {})
        url = handoff_bot.get("url")

        if url:
            if tracker.get_latest_input_channel() == "rest":
                dispatcher.utter_message(
                    json_message={
                        "handoff_host": url,
                        "title": handoff_bot.get("title"),
                    }
                )
            else:
                dispatcher.utter_message(
                    template="utter_wouldve_handed_off", handoffhost=url
                )
        else:
            dispatcher.utter_message(template="utter_no_handoff")

        return []


class ActionConsultarCep(Action):
    def name(self):
        return "action_consultar_cep"

    def run(self, dispatcher, tracker, domain):
        try:
            cep = tracker.get_slot("cep")
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url=url, verify=False)
            if response.status_code == 200:
                data = response.json()
                return [SlotSet(key='UF', value=data.get("uf"))]
            else:
                dispatcher.utter_message("Cep inválido!")
            return []
        except Exception as e:
            logger.error(e)
            raise e


class ActionCriarTicket(Action):
    def name(self):
        return "action_more_updates"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        try:
            dispatcher.utter_message("se você quiser modificar mais alguma coisa, me diga o que é. É o que eu tenho atualmente: localização: {localizacao} preço: {preco} cozinha: {cozinha} para {pessoas} pessoas.")
            return []
        except Exception as e:
            logger.error(e)
            raise e


class ActionSessionStart(Action):
    def name(self):
        return "action_request_info"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        try:
            return []
        except Exception as e:
            logger.error(e)
            raise e


class ActionConsultarImagensDeCelular(Action):
    def name(self):
        return "action_search_restaurantes"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        try:
            dispatcher.utter_message("Este é o endereço do restaurante que você procura Rua Almeida no bairro Jubileu!")
            return []
        except Exception as e:
            logger.error(e)
            raise e

class ActionConsultarCliente(Action):
    def name(self):
        return "action_consultar_cliente"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        try:
            dispatcher.utter_message("Verifiquei que você não é nosso cliente ainda, que tals fazemos um cadastro rápido pra mim te oferecer nossas melhores opções?")
            return []
        except Exception as e:
            logger.error(e)
            raise e
