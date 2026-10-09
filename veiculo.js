document.getElementById('formVeiculo').addEventListener('submit', function(evento) {
    evento.preventDefault();

    const placa = document.getElementById('placa').value;
    const marcaModelo = document.getElementById('marcaModelo').value;
    const tipo = document.getElementById('tipo').value;

    fetch('http://127.0.0.1:5000/veiculos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ placa: placa, marcaModelo: marcaModelo, tipo: tipo })
    })
    .then(function(resposta) {
        return resposta.json();
    })
    .then(function(dados) {
        alert(dados.mensagem);
        if (dados.sucesso) {
            document.getElementById('formVeiculo').reset();
        }
    });
});