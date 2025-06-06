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
```
---
ampos:
Campo	      Tipo	  Obrigatório	                Descrição
nome	     string	      Não	          Nome do remetente da mensagem
mensagem	 string	      Não	          Mensagem a ser enviada por e-mail

Saída Esperada
A função retorna uma estrutura JSON com código de status e mensagem indicando sucesso ou erro.

```json
{
  "statusCode": 200,
  "body": "\"E-mail enviado com sucesso para você mesmo!\""
}
```

Exemplo de erro:
```json
{
  "statusCode": 500,
  "body": "\"Erro ao enviar e-mail: <mensagem do erro>\""
}
```
Dependências Externas
boto3 (biblioteca padrão da AWS para Python)

Amazon SES habilitado e com o e-mail verificado

Permissão AmazonSESFullAccess atribuída à função Lambda

A função utiliza serviços AWS, que podem gerar custos dependendo do uso.

Instruções para Execução

1 Acesse o console da AWS Lambda.

2 Crie uma nova função Lambda com runtime Python 3.8+.

3 Cole o código que tem no repositorio

4 Adicione a permissão AmazonSESFullAccess à role da função.

5 Verifique o e-mail usado no SES

Testar:
1 No console da Lambda, clique em Test.

2 Use este exemplo de evento:

```json
{
  "nome": "Guerra",
  "mensagem": "faz o L"
}
```
3 Clique em "Test". O e-mail será enviado para o mesmo endereço

Use os logs do CloudWatch para verificar mensagens de erro.

Erros comuns:

E-mail não verificado no SES

Permissões insuficientes na role da Lambda

Falta de região correta (us-east-1)

Autor
Matheus Henrique Carneiro
Função Lambda desenvolvida para fins academicos.
