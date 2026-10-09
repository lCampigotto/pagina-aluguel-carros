> Sistema de Login e Registro de Veículos - AlugAgora!

> Sobre o projeto

> Tema: Aluguel de carros

Objetivo: Sistema web de login, cadastro de usuários e registro de
veículos para o AlugAgora!, uma plataforma de aluguel de carros. A tela
de login/cadastro é o ponto de entrada do sistema, validando usuários
através de um backend em Python (Flask) conectado a uma base de dados
em CSV. O registro de veículos é salvo em um banco PostgreSQL.

Público-alvo: Gerentes da empresa, este site serve para cadastros no
banco de dados.

Observação: as senhas e usuários não são armazenados em texto puro no
CSV. Antes de salvar ou verificar, os dados passam por funções de
codificação (uma cifra de deslocamento, similar à Cifra de César,
aplicada a letras e números separadamente) (Este sistema ja estava
pronto no meu GitHub --- link [https://github.com/lCampigotto/Codificador-de-Registro]).

> Estrutura do projeto

- `pag_login.html` — página de login
- `pag_cadastro.html` — página de cadastro
- `landpage.html` — página principal
- `reg_carros.html` — página de registro de veículos (integrada ao PostgreSQL)
- `reg_pessoas.html` — página de cadastro de funcionários e clientes (ainda ilustrativa)
- `login.js` — script da página de login (envia usuário/senha para `/login`)
- `cadastro.js` — script da página de cadastro (envia usuário/senha para `/cadastro`)
- `veiculo.js` — script da página de veículos (envia placa, marca/modelo e tipo para `/veiculos`)
- `estilo.css` — estilização das páginas
- `sistema.py` — backend em Flask, com as rotas `/login`, `/cadastro` e `/veiculos`
- `dados.csv` — arquivo onde os usuários cadastrados são salvos

  --- Novo ---
- `reg_contratos` - página de registro de contratos

> Como rodar

Requisitos: Python 3.14+ e PostgreSQL rodando na máquina, com a tabela
`veiculos` já criada (scripts do projeto de aluguel de carros).

1. Instale as dependências (roda no terminal):
```
pip install flask flask-cors psycopg2-binary
```
2. No `sistema.py`, ajuste a função `conectar_banco()` com os dados do
   seu banco (nome, usuário, senha, host e porta).
3. Rode o servidor:
```
python sistema.py
```
4. Abra o `pag_login.html` no navegador.

> Fluxo do sistema

- Login: os dados digitados são codificados e comparados linha a linha
  com o `dados.csv`. Se baterem, o acesso é liberado.
- Cadastro: os dados digitados são codificados e adicionados como uma
  nova linha no `dados.csv`.
- Veículos: a placa e o tipo digitados são ajustados (placa em
  maiúsculo, tipo em minúsculo) e inseridos na tabela `veiculos` do
  PostgreSQL. A página avisa se o registro deu certo ou não.

> Regras do banco (tabela veiculos)

- Placa: 3 letras + 4 números (ex: ABC1234) e não pode repetir
- Tipo: apenas `carro` ou `moto`
- Marca/Modelo: até 50 caracteres

> Limitações

- Sobre codificar a senha : O programa apenas codifica os números contidos na senha. Exemplo: senha1234 - Codificada: senha4567
- A placa só aceita o formato antigo (ABC1234), o padrão Mercosul (ABC1D23) é recusado pelo banco
- A mensagem de erro do registro de veículos é genérica (não diz se o problema foi placa repetida, formato ou tipo)
- A senha do banco está escrita direto no código, não subir o `sistema.py` com ela pro GitHub
- Por enquanto só o registro de veículos está integrado ao PostgreSQL, a página `reg_pessoas.html` ainda é ilustrativa

> Autor
Lucas Campigotto - [@lCampigotto]

Muito obrigado! Se tiver alguma dica de algo que posso melhorar neste projeto me envie por e-mail - [campigotto.lucas@proton.me]
