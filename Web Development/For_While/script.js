// For (onde começa; onde termina; incremento ou decremento)
for(let i = 0; i < 5; i++) {
    console.log(`${i}: Alexander Albon 23`);
    
}

// While
let contador = 0;
while(contador < 3){
    console.log(`${contador}: Logan Sargeant 2`);
    contador++;
}

// for in
const pessoa = {
    nome: 'Victor',
    idade: 18,
    cidade: 'São Paulo'
}

for(const propriedade in pessoa){
    console.log(`${propriedade}: ${pessoa[propriedade]}`)
}

// for of
const cores = ['vermelho', 'azul', 'preto'];

for(const cor of cores){
    console.log(cor);
}

// 
const resultadoDiv = document.getElementById('resultado');

const carro = {
    marca: "Ford",
    modelo: "Fusion",
    ano: 2007,
    cor: "azul",
    ligar: function(){
        console.log("O carro vestá ligado");
        exibirMensagemNoNavegador("O carro está ligado!!!!")
    },
    obterDetalhes: function() {
        return `${this.marca} ${this.modelo} ${this.ano}`;
    }
    // this se refere ao objeto 'carro' dentro de seus métodos
}

console.log(".......Objeto Literal");
console.log(`Marca: ${carro.marca}`); // notação de ponto
console.log(`Modelo: ${carro ["modelo"]}`); // notação de colchetes
carro.ligar();

const DetalhesCarro = carro.obterDetalhes();
console.log(`Detalhes Carro: ${DetalhesCarro}`);

// Outra forma de exibir um objeto("Converte o bojeto para uma srting JSON")
const carroJson = JSON.stringify(carro);
console.log(`Objeto carro com json: ${carroJson}`)

function exibirMensagemNoNavegador(){
    const paragrafo = document.createElement('p'); // cria um parágrafo
    paragrafo.textContent = "aeeeeeeeeeeeee"; // Define o texto
    resultadoDiv.appendChild(paragrafo); // adiciona o parágrafo elmento 'resultado' no html
}

function pessoa(nome,idade,profissao){
    this.nome = nome;
    this.idade = idade;
    this.profissao = profissao;
}


