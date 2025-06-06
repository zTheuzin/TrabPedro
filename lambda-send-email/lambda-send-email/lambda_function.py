import boto3
import json

ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    try:
       
        nome = event.get('nome', 'Guerra')
        mensagem = event.get('mensagem', 'faz o L')

        response = ses.send_email(
            Source='matheushenriquecarneiro4@gmail.com', 
            Destination={
                'ToAddresses': ['matheushenriquecarneiro4@gmail.com']  
            },
            Message={
                'Subject': {'Data': 'Confirmação Recebida'},
                'Body': {
                    'Text': {
                        'Data': f"Olá {nome},\n\nRecebemos sua mensagem:\n\n{mensagem}\n\nObrigado!"
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('E-mail enviado com sucesso para você mesmo!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao enviar e-mail: {str(e)}')
        }
