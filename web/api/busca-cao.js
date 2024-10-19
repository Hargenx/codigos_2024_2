//https://dog.ceo/dog-api/documentation/
function obterImagnsAleatoriasAuAu() {
    const auAu = document.getElementById("resultado-canis");
    const xhr = new XMLHttpRequest();
    const endpoint = "https://dog.ceo/api/breeds/image/random";
    xhr.open("GET", endpoint, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const dados = JSON.parse(xhr.responseText);
            const imagemUrl = dados.message;
            auAu.innerHTML = `<img src="${imagemUrl}" alt="Imagem de um cachorro">`;
        } else {
            auAu.innerHTML = "Não foi possível obter uma imagem de cachorro.";
        }
    };
    xhr.send();
}
