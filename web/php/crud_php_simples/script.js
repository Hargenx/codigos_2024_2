function validarFormulario() {
    const nome = document.getElementById('nome').value;
    const plataforma = document.getElementById('plataforma').value;
    const genero = document.getElementById('genero').value;

    if (nome === '' || plataforma === '' || genero === '') {
        mensagem = 'Por favor, preencha todos os campos.';
        return false && getElementById('resultado').mensagem;
    }
    return true;
}