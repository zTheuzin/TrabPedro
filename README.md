# Lambda - Envio de E-mail com Amazon SES

## 📌 Objetivo
Esta função Lambda envia e-mails personalizados usando o Amazon Simple Email Service (SES), com remetente e destinatário sendo o mesmo e-mail verificado, ideal para testes e demonstração.

---

## 🚀 Como Funciona

A função espera um evento JSON com os seguintes campos:

```json
{
  "nome": "Guerra",
  "mensagem": "faz o L"
}
