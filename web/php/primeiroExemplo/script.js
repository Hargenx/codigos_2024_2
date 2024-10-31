function validar() {
    const nome = document.forms["formulario"]["nome"].value;
    const email = document.forms["formulario"]["email"].value;

    let nomeErro = document.getElementById("nomeErro");
    let emailErro = document.getElementById("emailErro");

    // Expressão regular para validar email
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

    nomeErro.innerHTML = "";
    emailErro.innerHTML = "";
    let valido = true;

    if (nome === "") {
        nomeErro.innerHTML = "Por favor, preencha o campo Nome.";
        valido = false;
    }

    if (!email.match(emailRegex)) {
        emailErro.innerHTML = "Por favor, insira um email válido.";
        valido = false;
    }
    return valido;
}
