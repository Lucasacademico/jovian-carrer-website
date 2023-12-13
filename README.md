# jovian-carrer-website

## Links úteis que foram utilizados nesse projeto:
- https://www.youtube.com/watch?v=yBDHkveJUf4 - Link da aula
- https://excalidraw.com/ - Link de prototipação simples com desenho
- https://www.htmldog.com/ - Link tutorial de html usado pelo curso
- https://unsplash.com/pt-br - Site de imagens grátis pra uso
- https://fonts.google.com/ - Fontes para importar do google
- https://getbootstrap.com/ - Site Bootstrap
- https://replit.com/ - Ambiente virtual online para desenvolvimento
- https://render.com/ - Site simples para deploy de sites

## Realizando o Deploy com Render

Criando a conta:
- Acessar o site render.com
- Criar conta gratuita

Após criada a conta e logado:
- Clicar no botão New +
- Vamos selecionar 'Web Service' neste caso
- Selecionar "Build and deploy from a git repository"
- Conectaremos o github (sera aberta janela)

Na janela de autorização do Github:
- Selecionar conta Github 
- Selecionar somente a conexão de UM repositório específico
- Clicar em instalar e confirmar com a senha

Antes de prosseguirmos vamos criar um arquivo requirements em formato txt na pasta do projeto:
- O nome do arquivo deve ser: requirements.txt
- no arquivo deve apenas estar escrito:
Flask
gunicorn
- O gunicorn funciona como um intermediário entre a aplicação web Python e o servidor web, permitindo que a aplicação Python seja executada de forma eficiente e escalável.
- Salvar, e realizar push deste arquivo para o repositório

Após carregar o repositório no Render:
- Clicar em connect
- Name: Jovia Carrers Website
- Region: Oregon (é a melhor aqui pro BR)
- Comando para iniciar: gunicorn app:app
- Selecione o modo gratis (que não tamo com essa grana toda)
- Selecione instalar no final
- APós isso o ambiente será preparado

Após finalizado a preparação do ambiente:
- Clicar no link da instancia criada, e acessar o site que já está pronto para acesso!

Documentação deploy Render para flask:
- https://render.com/docs/deploy-flask


