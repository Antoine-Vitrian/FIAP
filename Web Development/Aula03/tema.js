// Obter referências ao botão e à página
const botaoClaro = document.getElementById("temaClaro");
const botaoEscuro = document.getElementById( "temaEscuro");
const body = document.body;

//  Define uma chave para armazenar a preferência de tema nO LocalSotorage
const chaveTema = "preferênciaTema";

// Função para escolher o tema específico
function aplicarTema(tema){
    body.classList.remove('temaClaro','temaEscuro');
    body.classList.add(`tema-${tema}`);

    // salva a preferência do tema no LocalStorage
    localStorage.setItem(chaveTema, tema);
}

// Verificar se já tem uma preferência de tema salva no LocalSorage ao carregar a página
const temaSalvo = localStorage.getItem(chaveTema);

if(temaSalvo){
    aplicarTema(temaSalvo);
}
else {
    aplicarTema('claro')
}

// adiciona um evento de click ao botão
botaoClaro.addEventListener('click', ()=>{
    // quando o botao for clicado, chama a função que ele escolheu
    aplicarTema('claro')
});

botaoEscuro.addEventListener('click', ()=>{
    // quando o botao for clicado, chama a função que ele escolheu
    aplicarTema('escuro')
});
