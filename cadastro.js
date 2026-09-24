document.getElementById('formCadastro').addEventListener('submit', function(evento) {
    evento.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;

    fetch('http://127.0.0.1:5000/cadastro', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario: usuario, senha: senha })
    })
    .then(function(resposta) {
        return resposta.json();
    })
    .then(function(dados) {
        console.log(dados);
        if (dados.sucesso) {
            window.location.href = 'pag_login.html';
        } else {
            alert(dados.mensagem);
        }
    });
});