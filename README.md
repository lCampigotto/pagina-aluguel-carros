> Sistema de Login - AlugAgora!

> Sobre o projeto

> Tema: Aluguel de carros

Objetivo: Sistema web de login e cadastro e cadastros no banco de dados (sobre o banco de dados: é meramente ilustrativo) para o AlugAgora! 
uma plataforma de aluguel de carros. A tela de login/cadastro é o ponto de entrada do sistema 
validando usuários através de um backend em Python (Flask) conectado a uma base de dados em CSV.

Público-alvo: Gerentes da empresa, este site serve para cadastros no banco de dados.

Observação: as senhas e usuários não são armazenados em texto puro no
CSV antes de salvar ou verificar, os dados passam por funções de
codificação (uma cifra de deslocamento, similar à Cifra de César,
aplicada a letras e números separadamente) (Este sistema ja estava pronto no meu GitHub --- link [https://github.com/lCampigotto/Codificador-de-Registro]).

> Estrutura do projeto

- `pag_login.html` — página de login
- `pag_cadastro.html` — página de cadastro
- `landpage.html` — página principal
- `reg_carros.html` — página de cadastro de veículos
- `reg_pessoas.html` — página de cadastro de funcionários e clientes
- `login.js` — script da página de login (envia usuário/senha para `/login`)
- `cadastro.js` — script da página de cadastro (envia usuário/senha para `/cadastro`)
- `estilo.css` — estilização das páginas
- `sistema.py` — backend em Flask, com as rotas `/login` e `/cadastro`
- `dados.csv` — arquivo onde os usuários cadastrados são salvos

  --- Novo ---
- `reg_contratos` - página de registro de contratos

> Como rodar

1. Instale as dependências:
```
Instale Python 3.14+
pip install flask flask-cors (roda no terminal)
```
2. Rode o servidor:
```
python sistema.py (só executar)
```
3. Abra o `pag_login.html` no navegador.

> Fluxo do sistema

- Login: os dados digitados são codificados e comparados linha a linha
  com o `dados.csv`. Se baterem, o acesso é liberado.
- Cadastro: os dados digitados são codificados e adicionados como uma
  nova linha no `dados.csv`.
- SOBRE O BANCO DE DADOS : No momento o registro é meramente ilustrativo!

> Limitação

- Sobre codificar a senha : O programa apenas codifica os números contidos na senha. Exemplo: senha1234 - Codificada: senha4567

> Autor
Lucas Campigotto - [@lCampigotto]

Muito obrigado! Se tiver alguma dica de algo que posso melhorar neste projeto me envie por e-mail - [campigotto.lucas@proton.me]
