AWS Lambda - Envio de E-mail com Amazon SES

Objetivo
Esta função AWS Lambda tem como objetivo enviar e-mails de forma automática utilizando o Amazon Simple Email Service (SES). A função é útil para confirmações de cadastro, notificações ou testes acadêmicos.

---

Funcionamento

A função recebe como entrada um objeto JSON com os seguintes campos:

```json
{
  "nome": "Guerra",
  "mensagem": "faz o L"
}
