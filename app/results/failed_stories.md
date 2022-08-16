## 687141e7-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: restaurante [oeste](localizacao) parte da cidade [romena](cozinha)
    - slot{"cozinha": "romena"}
    - slot{"localizacao": "oeste"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_price   <!-- predicted: utter_fallback -->
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 687141e8-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "oeste", "cozinha": "português", "pessoas": "8"}
    - slot{"cozinha": "português"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "8"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 687141eb-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: restaurante com preços [moderado](preco) na parte [norte](localizacao) da cidade
    - slot{"localizacao": "norte"}
    - slot{"preco": "moderado"}
    - utter_ask_cuisine
* informar: um [chinesa](cozinha)
    - slot{"cozinha": "chinesa"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 687141ec-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "paris", "preco": "moderado", "cozinha": "europeu"}
    - slot{"cozinha": "europeu"}
    - slot{"localizacao": "paris"}
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: ok obrigado adeus
    - utter_obrigado


## 687141ed-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: id como [barato](preco) com preços [britânica](cozinha) comida
    - slot{"cozinha": "britânica"}
    - slot{"preco": "barato"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_location
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 687141f0-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: /informar{"preco": "moderado", "pessoas": "2", "cozinha": "asiático oriental"}
    - slot{"cozinha": "asiático oriental"}
    - slot{"pessoas": "2"}
    - slot{"preco": "moderado"}
    - utter_ask_location
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 68714189-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para [4](pessoas) pessoas com cozinha [coreana](cozinha) em [sul](localizacao)
    - slot{"cozinha": "coreana"}
    - slot{"localizacao": "sul"}
    - slot{"pessoas": "4"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 687141f1-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: eu quero um restaurante com preço [moderado](preco) na parte [oeste](localizacao) da cidade
    - slot{"localizacao": "oeste"}
    - slot{"preco": "moderado"}
    - utter_ask_cuisine
* informar: [britânica](cozinha)
    - slot{"cozinha": "britânica"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 687141f2-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: /informar{"preco": "barata", "localizacao": "sul", "cozinha": "gastropub"}
    - slot{"cozinha": "gastropub"}
    - slot{"localizacao": "sul"}
    - slot{"preco": "barata"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: logo adeus paz
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 687141fc-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: [gastropub](cozinha)
    - slot{"cozinha": "gastropub"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 687141fd-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - utter_ask_cuisine   <!-- predicted: utter_ask_numpeople -->
* informar: comida [jamaicana](cozinha)
    - slot{"cozinha": "jamaicana"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 687141fe-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: [oeste](localizacao) estou procurando um restaurante na parte da cidade
    - slot{"localizacao": "oeste"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_cuisine
* informar: um [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 687141ff-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_cuisine   <!-- predicted: utter_fallback -->
* informar: um [gastropub](cozinha)
    - slot{"cozinha": "gastropub"}
    - action_more_updates
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: ok obrigado
    - utter_obrigado


## 68714201-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [londres](localizacao) em uma [barato](preco) faixa de preço com cozinha [frutos do mar](cozinha) para [5](pessoas)
    - slot{"cozinha": "frutos do mar"}
    - slot{"localizacao": "londres"}
    - slot{"pessoas": "5"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 68714202-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [corsica](cozinha) em [londres](localizacao) para [9](pessoas) pessoas   <!-- predicted: informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [corsica](cozinha) em [londres](localizacao) para 9 pessoas -->
    - slot{"cozinha": "corsica"}
    - slot{"localizacao": "londres"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 68714203-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para [9](pessoas) pessoas com cozinha [gastropub](cozinha) em [leste](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para 9 pessoas com cozinha [gastropub](cozinha) em [leste](localizacao) -->
    - slot{"cozinha": "gastropub"}
    - slot{"localizacao": "leste"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: obrigado e adeus
    - utter_obrigado


## 68714206-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [madri](localizacao) em uma [moderado](preco) faixa de preço com cozinha [italiana](cozinha) para [7](pessoas)
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "madri"}
    - slot{"pessoas": "7"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: e isso é tudo obrigado e adeus
    - utter_obrigado


## 6871418b-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [corsica](cozinha) em [oeste](localizacao) para [3](pessoas) pessoas
    - slot{"cozinha": "corsica"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "3"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 6871420b-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [oeste](localizacao) com comida [frutos do mar](cozinha) para [9](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [oeste](localizacao) com comida [frutos do mar](cozinha) para 9 -->
    - slot{"cozinha": "frutos do mar"}
    - slot{"localizacao": "oeste"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 6871420c-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para [9](pessoas) pessoas com cozinha [romena](cozinha) em [londres](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para 9 pessoas com cozinha [romena](cozinha) em [londres](localizacao) -->
    - slot{"cozinha": "romena"}
    - slot{"localizacao": "londres"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: ok obrigado
    - utter_obrigado


## 6871420d-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [londres](localizacao) com comida [italiana](cozinha) para [8](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [londres](localizacao) com comida [italiana](cozinha) para 8 -->
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "londres"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 6871420e-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [moderado](preco) em [madri](localizacao) com comida [jamaicana](cozinha) para [7](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [moderado](preco) em [madri](localizacao) com comida [jamaicana](cozinha) para 7 -->
    - slot{"cozinha": "jamaicana"}
    - slot{"localizacao": "madri"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 68714210-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [londres](localizacao) em uma [moderado](preco) faixa de preço com cozinha [frutos do mar](cozinha) para [9](pessoas)
    - slot{"cozinha": "frutos do mar"}
    - slot{"localizacao": "londres"}
    - slot{"pessoas": "9"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: você é demais
    - utter_obrigado


## 68714211-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [barato](preco) com comida [chinesa](cozinha) em [norte](localizacao) para [4](pessoas) pessoas
    - slot{"cozinha": "chinesa"}
    - slot{"localizacao": "norte"}
    - slot{"pessoas": "4"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 6871418c-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [leste](localizacao) em uma [caro](preco) faixa de preço com cozinha [corsica](cozinha) para [5](pessoas)
    - slot{"cozinha": "corsica"}
    - slot{"localizacao": "leste"}
    - slot{"pessoas": "5"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 68714216-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [londres](localizacao) com comida [asiático oriental](cozinha) para [1](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [londres](localizacao) com comida [asiático oriental](cozinha) para 1 -->
    - slot{"cozinha": "asiático oriental"}
    - slot{"localizacao": "londres"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: obrigado e adeus
    - utter_obrigado


## 68714217-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [caro](preco) com comida [corsica](cozinha) em [oeste](localizacao) para [6](pessoas) pessoas
    - slot{"cozinha": "corsica"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "6"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 6871421a-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: restaurante [oeste](localizacao) parte da cidade [canapes](cozinha)
    - slot{"cozinha": "canapes"}
    - slot{"localizacao": "oeste"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 6871421b-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "indiana", "localizacao": "madri", "pessoas": "1"}
    - slot{"cozinha": "indiana"}
    - slot{"localizacao": "madri"}
    - slot{"pessoas": "1"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: e isso é tudo obrigado e adeus
    - utter_obrigado


## 6871421c-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: procurando um restaurante [barato](preco) que serve comida [corsica](cozinha)
    - slot{"cozinha": "corsica"}
    - slot{"preco": "barato"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_location
* informar: [oeste](localizacao) estou procurando um restaurante na parte da cidade
    - slot{"localizacao": "oeste"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: e isso é tudo obrigado e adeus
    - utter_obrigado


## 68714224-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: restaurante [norte](localizacao) parte da cidade [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - slot{"localizacao": "norte"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim certo
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 68714225-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "oeste", "cozinha": "português", "pessoas": "8"}
    - slot{"cozinha": "português"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "8"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 68714226-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "leste", "pessoas": "6"}
    - slot{"localizacao": "leste"}
    - slot{"pessoas": "6"}
    - utter_ask_cuisine
* informar: comida [jamaicana](cozinha)
    - slot{"cozinha": "jamaicana"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 6871418e-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para [7](pessoas) pessoas com cozinha [asiático oriental](cozinha) em [sul](localizacao)
    - slot{"cozinha": "asiático oriental"}
    - slot{"localizacao": "sul"}
    - slot{"pessoas": "7"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: ah obrigado adeus
    - utter_obrigado


## 68714227-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "leste", "pessoas": "1", "cozinha": "europeu"}
    - slot{"cozinha": "europeu"}
    - slot{"localizacao": "leste"}
    - slot{"pessoas": "1"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: ah obrigado adeus
    - utter_obrigado


## 68714228-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: eu quero um restaurante com preço [moderado](preco) na parte [norte](localizacao) da cidade
    - slot{"localizacao": "norte"}
    - slot{"preco": "moderado"}
    - utter_ask_cuisine
* informar: [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 68714229-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "paris", "preco": "moderado", "cozinha": "europeu"}
    - slot{"cozinha": "europeu"}
    - slot{"localizacao": "paris"}
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: ok obrigado
    - utter_obrigado


## 6871422a-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: procurando um restaurante [caro](preco) que serve comida [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - slot{"preco": "caro"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 6871422d-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: /informar{"preco": "moderado", "pessoas": "2", "cozinha": "asiático oriental"}
    - slot{"cozinha": "asiático oriental"}
    - slot{"pessoas": "2"}
    - slot{"preco": "moderado"}
    - utter_ask_location
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 6871422e-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: restaurante com preços [moderado](preco) na parte [norte](localizacao) da cidade
    - slot{"localizacao": "norte"}
    - slot{"preco": "moderado"}
    - utter_ask_cuisine
* informar: [chinesa](cozinha)
    - slot{"cozinha": "chinesa"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 6871422f-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: /informar{"preco": "barata", "localizacao": "sul", "cozinha": "gastropub"}
    - slot{"cozinha": "gastropub"}
    - slot{"localizacao": "sul"}
    - slot{"preco": "barata"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 68714193-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [irlandesa](cozinha) em [sul](localizacao) para [5](pessoas) pessoas
    - slot{"cozinha": "irlandesa"}
    - slot{"localizacao": "sul"}
    - slot{"pessoas": "5"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 68714195-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [madri](localizacao) com comida [asiático oriental](cozinha) para [7](pessoas)
    - slot{"cozinha": "asiático oriental"}
    - slot{"localizacao": "madri"}
    - slot{"pessoas": "7"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 68714198-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [barato](preco) para [7](pessoas) pessoas com cozinha [coreana](cozinha) em [norte](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [barato](preco) para 7 pessoas com cozinha [coreana](cozinha) em [norte](localizacao) -->
    - slot{"cozinha": "coreana"}
    - slot{"localizacao": "norte"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 68714199-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [britânica](cozinha) em [oeste](localizacao) para [8](pessoas) pessoas   <!-- predicted: informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [britânica](cozinha) em [oeste](localizacao) para 8 pessoas -->
    - slot{"cozinha": "britânica"}
    - slot{"localizacao": "oeste"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 6871419a-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para [9](pessoas) pessoas com cozinha [indiana](cozinha) em [londres](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para 9 pessoas com cozinha [indiana](cozinha) em [londres](localizacao) -->
    - slot{"cozinha": "indiana"}
    - slot{"localizacao": "londres"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 6871419b-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [barato](preco) com comida [jamaicana](cozinha) em [oeste](localizacao) para [3](pessoas) pessoas
    - slot{"cozinha": "jamaicana"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "3"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim certo
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 6871419c-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [madri](localizacao) com comida [britânica](cozinha) para [8](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [madri](localizacao) com comida [britânica](cozinha) para 8 -->
    - slot{"cozinha": "britânica"}
    - slot{"localizacao": "madri"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: logo adeus paz
    - utter_ack_makereservation
* obrigado: ok ok obrigado adeus
    - utter_obrigado


## 6871419d-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [leste](localizacao) em uma [caro](preco) faixa de preço com cozinha [romena](cozinha) para [6](pessoas)
    - slot{"cozinha": "romena"}
    - slot{"localizacao": "leste"}
    - slot{"pessoas": "6"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 6871419e-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "francesa", "pessoas": "2"}
    - slot{"cozinha": "francesa"}
    - slot{"pessoas": "2"}
    - utter_ask_location
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: ah obrigado adeus
    - utter_obrigado


## 6871419f-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "frutos do mar", "pessoas": "5", "localizacao": "londres"}
    - slot{"cozinha": "frutos do mar"}
    - slot{"localizacao": "londres"}
    - slot{"pessoas": "5"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 687141a0-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: restaurante [londres](localizacao) parte da cidade [coreana](cozinha)
    - slot{"cozinha": "coreana"}
    - slot{"localizacao": "londres"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: ok ok obrigado adeus
    - utter_obrigado


## 687141a1-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "indiana", "localizacao": "madri", "pessoas": "1"}
    - slot{"cozinha": "indiana"}
    - slot{"localizacao": "madri"}
    - slot{"pessoas": "1"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 687141a2-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: procurando um restaurante [caro](preco) que serve comida [afegã](cozinha)
    - slot{"cozinha": "afegã"}
    - slot{"preco": "caro"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_location
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - action_more_updates
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: logo adeus paz
    - utter_ack_makereservation
* obrigado: e isso é tudo obrigado e adeus
    - utter_obrigado


## 687141a4-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "6", "cozinha": "português"}
    - slot{"cozinha": "português"}
    - slot{"pessoas": "6"}
    - utter_ask_location
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 687141a5-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "5", "cozinha": "alemão", "localizacao": "londres"}
    - slot{"cozinha": "alemão"}
    - slot{"localizacao": "londres"}
    - slot{"pessoas": "5"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim certo
    - utter_ack_makereservation
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 687141a6-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "2", "localizacao": "norte"}
    - slot{"localizacao": "norte"}
    - slot{"pessoas": "2"}
    - utter_ask_cuisine
* informar: um [italiana](cozinha)
    - slot{"cozinha": "italiana"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: ah obrigado adeus
    - utter_obrigado


## 68714182-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: [indiana](cozinha)
    - slot{"cozinha": "indiana"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 687141a7-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "2", "localizacao": "paris", "cozinha": "alemão"}
    - slot{"cozinha": "alemão"}
    - slot{"localizacao": "paris"}
    - slot{"pessoas": "2"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 687141aa-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: restaurante [sul](localizacao) parte da cidade [italiana](cozinha)
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "sul"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: obrigado e adeus
    - utter_obrigado


## 687141ae-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: restaurante com preços [moderado](preco) na parte [norte](localizacao) da cidade
    - slot{"localizacao": "norte"}
    - slot{"preco": "moderado"}
    - utter_ask_cuisine
* informar: estou procurando comida [gastropub](cozinha)
    - slot{"cozinha": "gastropub"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - action_more_updates
* negar: nenhuma nova seleção
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: obrigado e adeus
    - utter_obrigado


## 687141af-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: /informar{"localizacao": "paris", "preco": "moderado", "cozinha": "europeu"}
    - slot{"cozinha": "europeu"}
    - slot{"localizacao": "paris"}
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: ah obrigado adeus
    - utter_obrigado


## 687141b0-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: id como [barato](preco) com preços [britânica](cozinha) comida
    - slot{"cozinha": "britânica"}
    - slot{"preco": "barato"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: certo
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 68714183-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_price   <!-- predicted: utter_fallback -->
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - utter_ask_cuisine   <!-- predicted: utter_ask_numpeople -->
* informar: estou procurando comida [gastropub](cozinha)
    - slot{"cozinha": "gastropub"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: ok obrigado
    - utter_obrigado


## 687141b3-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: /informar{"preco": "moderado", "pessoas": "2", "cozinha": "asiático oriental"}
    - slot{"cozinha": "asiático oriental"}
    - slot{"pessoas": "2"}
    - slot{"preco": "moderado"}
    - utter_ask_location
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: logo adeus paz
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 687141b4-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: restaurante com preços [caro](preco) na parte [oeste](localizacao) da cidade
    - slot{"localizacao": "oeste"}
    - slot{"preco": "caro"}
    - utter_ask_cuisine
* informar: [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: ah obrigado adeus
    - utter_obrigado


## 687141b5-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: /informar{"preco": "barata", "localizacao": "sul", "cozinha": "gastropub"}
    - slot{"cozinha": "gastropub"}
    - slot{"localizacao": "sul"}
    - slot{"preco": "barata"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 68714184-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: [oeste](localizacao) estou procurando um restaurante na parte da cidade
    - slot{"localizacao": "oeste"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_cuisine
* informar: um [italiana](cozinha)
    - slot{"cozinha": "italiana"}
    - action_more_updates
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 687141bf-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: [chinesa](cozinha)
    - slot{"cozinha": "chinesa"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 687141c0-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - utter_ask_cuisine   <!-- predicted: utter_ask_numpeople -->
* informar: comida [frutos do mar](cozinha)
    - slot{"cozinha": "frutos do mar"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 687141c1-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: poderia ser para [9](pessoas)   <!-- predicted: informar: poderia ser para 9 -->
    - utter_ask_cuisine
* informar: um [britânica](cozinha)
    - slot{"cozinha": "britânica"}
    - action_more_updates
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 687141c2-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_cuisine   <!-- predicted: utter_fallback -->
* informar: um [irlandesa](cozinha)
    - slot{"cozinha": "irlandesa"}
    - action_more_updates
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: hum obrigado adeus
    - utter_obrigado


## 687141c3-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [londres](localizacao) em uma [moderado](preco) faixa de preço com cozinha [italiana](cozinha) para [9](pessoas)
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "londres"}
    - slot{"pessoas": "9"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: hum sim
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 687141c6-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para [2](pessoas) pessoas com cozinha [irlandesa](cozinha) em [oeste](localizacao)
    - slot{"cozinha": "irlandesa"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "2"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim certo
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 68714185-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_cuisine
* informar: [coreana](cozinha)
    - slot{"cozinha": "coreana"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: eu amo isso
    - utter_ack_makereservation
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 687141cb-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [barato](preco) para [4](pessoas) pessoas com cozinha [italiana](cozinha) em [norte](localizacao)
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "norte"}
    - slot{"pessoas": "4"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 687141cc-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para [8](pessoas) pessoas com cozinha [asiático oriental](cozinha) em [oeste](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [moderado](preco) para 8 pessoas com cozinha [asiático oriental](cozinha) em [oeste](localizacao) -->
    - slot{"cozinha": "asiático oriental"}
    - slot{"localizacao": "oeste"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: obrigado e adeus
    - utter_obrigado


## 687141cf-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [barato](preco) com comida [espanhola](cozinha) em [oeste](localizacao) para [6](pessoas) pessoas
    - slot{"cozinha": "espanhola"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "6"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: correto
    - utter_ack_makereservation
* obrigado: você é demais
    - utter_obrigado


## 687141d1-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para [4](pessoas) pessoas com cozinha [britânica](cozinha) em [leste](localizacao)
    - slot{"cozinha": "britânica"}
    - slot{"localizacao": "leste"}
    - slot{"pessoas": "4"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 687141d2-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [moderado](preco) em [madri](localizacao) com comida [coreana](cozinha) para [1](pessoas)   <!-- predicted: informar: você pode fazer uma reserva em um intervalo de preços [moderado](preco) em [madri](localizacao) com comida [coreana](cozinha) para 1 -->
    - slot{"cozinha": "coreana"}
    - slot{"localizacao": "madri"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim certo
    - utter_ack_makereservation
* obrigado: ok obrigado adeus
    - utter_obrigado


## 68714186-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [frutos do mar](cozinha) em [sul](localizacao) para [8](pessoas) pessoas   <!-- predicted: informar: posso ter uma mesa com uma faixa de preço [moderado](preco) com comida [frutos do mar](cozinha) em [sul](localizacao) para 8 pessoas -->
    - slot{"cozinha": "frutos do mar"}
    - slot{"localizacao": "sul"}
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: obrigado tchau
    - utter_obrigado


## 687141d4-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: hey bot
    - utter_ask_howcanhelp
* informar: você pode reservar uma mesa em [oeste](localizacao) em uma [barato](preco) faixa de preço com cozinha [indiana](cozinha) para [4](pessoas)
    - slot{"cozinha": "indiana"}
    - slot{"localizacao": "oeste"}
    - slot{"pessoas": "4"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim posso ter
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 687141d7-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa noite
    - utter_ask_howcanhelp
* informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para [8](pessoas) pessoas com cozinha [francesa](cozinha) em [sul](localizacao)   <!-- predicted: informar: eu gostaria de reservar uma mesa em uma faixa de preço [caro](preco) para 8 pessoas com cozinha [francesa](cozinha) em [sul](localizacao) -->
    - slot{"cozinha": "francesa"}
    - slot{"localizacao": "sul"}
    - slot{"preco": "caro"}
    - action_more_updates
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: e isso é tudo obrigado e adeus
    - utter_obrigado


## 687141d9-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: você pode fazer uma reserva em um intervalo de preços [barato](preco) em [sul](localizacao) com comida [irlandesa](cozinha) para [1](pessoas)
    - slot{"cozinha": "irlandesa"}
    - slot{"localizacao": "sul"}
    - slot{"pessoas": "1"}
    - slot{"preco": "barato"}
    - action_more_updates
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: hum obrigado adeus
    - utter_obrigado


## 687141db-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Olá
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "francesa", "pessoas": "2"}
    - slot{"cozinha": "francesa"}
    - slot{"pessoas": "2"}
    - utter_ask_location
* informar: [oeste](localizacao) estou procurando um restaurante na parte da cidade
    - slot{"localizacao": "oeste"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: não, obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: ok legal uh adeus obrigado
    - utter_obrigado


## 687141dd-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: restaurante [oeste](localizacao) parte da cidade [italiana](cozinha)
    - slot{"cozinha": "italiana"}
    - slot{"localizacao": "oeste"}
    - utter_ask_numpeople
* informar: na verdade eu preferiria [5](pessoas)   <!-- predicted: informar: na verdade eu preferiria 5 -->
    - utter_ask_price
* informar: [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates
* negar: não obrigado
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim obrigado adeus
    - utter_ack_makereservation
* obrigado: obrigado adeus
    - utter_obrigado


## 687141de-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: bom Dia
    - utter_ask_howcanhelp
* informar: /informar{"cozinha": "indiana", "localizacao": "madri", "pessoas": "1"}
    - slot{"cozinha": "indiana"}
    - slot{"localizacao": "madri"}
    - slot{"pessoas": "1"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: você tem outra coisa
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: vamos fazer isso
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


## 687141df-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Ei
    - utter_ask_howcanhelp
* informar: id como [moderado](preco) com preços [britânica](cozinha) comida
    - slot{"cozinha": "britânica"}
    - slot{"preco": "moderado"}
    - utter_ask_numpeople
* informar: seremos [3](pessoas)   <!-- predicted: affirm: seremos 3 -->
    - utter_ask_location   <!-- predicted: utter_fallback -->
* informar: [norte](localizacao)
    - slot{"localizacao": "norte"}
    - action_more_updates   <!-- predicted: utter_ask_numpeople -->
* negar: não, obrigado adeus
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim, eu preciso encontrar   <!-- predicted: consultar_saldo_da_conta: sim, eu preciso encontrar -->
    - utter_ack_makereservation   <!-- predicted: utter_fallback -->
* obrigado: ok ok obrigado adeus
    - utter_obrigado


## 687141e3-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: manhã
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "2", "localizacao": "norte"}
    - slot{"localizacao": "norte"}
    - slot{"pessoas": "2"}
    - utter_ask_cuisine
* informar: que tal [jamaicana](cozinha)
    - slot{"cozinha": "jamaicana"}
    - utter_ask_price
* informar: sim, estou procurando um restaurante realmente [moderado](preco)
    - slot{"preco": "moderado"}
    - action_more_updates   <!-- predicted: utter_fallback -->
* negar: Oh não
    - utter_ack_do__search
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: desculpe pelos meus erros obrigado adeus
    - utter_obrigado


## 687141e5-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: Oi
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "4", "preco": "cara"}
    - slot{"pessoas": "4"}
    - slot{"preco": "cara"}
    - utter_ask_cuisine
* informar: e a comida [indiana](cozinha)
    - slot{"cozinha": "indiana"}
    - utter_ask_location
* informar: parte [londres](localizacao)
    - slot{"localizacao": "londres"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim
    - utter_ack_makereservation
* obrigado: hum ok obrigado adeus
    - utter_obrigado


## 687141e6-e24a-11ea-941b-5cea1dcfa5ff (/tmp/tmpd8n1mws1/d46c6f3d485246df9f23c07d0c660111_conversation_tests.md)
* greet: boa tarde
    - utter_ask_howcanhelp
* informar: /informar{"pessoas": "6", "preco": "barata", "cozinha": "frutos do mar"}
    - slot{"cozinha": "frutos do mar"}
    - slot{"pessoas": "6"}
    - slot{"preco": "barata"}
    - utter_ask_location
* informar: [londres](localizacao) parte da cidade
    - slot{"localizacao": "londres"}
    - action_more_updates
* negar: não, isso não funciona para mim
    - utter_ack_do__search   <!-- predicted: utter_fallback -->
    - action_search_restaurantes
* affirm: sim Sim
    - utter_ack_makereservation
* obrigado: obrigado
    - utter_obrigado


