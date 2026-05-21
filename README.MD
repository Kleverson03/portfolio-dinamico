Portfólio Dinâmico (API) (EM DESENVOLVIMENTO)
Este projeto consiste em um portfólio dinâmico com um backend desenvolvido em Django, focado em servir dados de forma estruturada através de uma API.

Tecnologias utilizadas
Backend: Python com Django.

Controle de Versão: Git/GitHub.

Banco de Dados: SQLite (padrão em desenvolvimento).

Funcionalidades
Gerenciamento de projetos via API.

Estrutura de habilidades e experiências profissionais.


Como rodar o projeto localmente
Clone o repositório:

Bash
git clone https://github.com/Kleverson03/portfolio-dinamico.git
Crie um ambiente virtual (recomendado):

Bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

Bash
pip install -r backend/requirements.txt
Aplique as migrações e rode o servidor:

Bash
cd backend
python manage.py migrate
python manage.py runserver