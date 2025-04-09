let  nome = "Victor";
console.log(nome);

// Tipos de variáveis
let texto = "Alex Albon";
let inteiro = parseInt(12);
let decimal = parseFloat(2.7);
let NumeroBooleano = true;

console.log(typeof(texto));
console.log(typeof(inteiro));
console.log(typeof(decimal));
console.log(typeof(NumeroBooleano));




// Operações

let a = 5;
let b = 6;

console.log("Adição ", a+b);
console.log("Subtração ", a-b);
console.log("Multiplicação ", a*b);
console.log("Divisão ", a/b);

 // Incrementa um no valor da variável
a++;

// Decrementa um no valor da variável
b--; 

// Document Object Module
console.log("Script externo rodando para o DOM");

const tituloElemento = document.getElementById("tituloEl");
tituloElemento.textContent = "Texto alterado";
tituloElemento.style.color = "green";

const botaoElemento = document.getElementById("meuBotao");
botaoElemento.addEventListener("click", function() {
    alert("Botão foi clicado!!!")
})

// teste
const textoTeste = document.getElementById("testando");
contador = 0;

function mudarTexto() {
    if(contador == 0){
        textoTeste.textContent = "Mudei o texto deu certo!";
        contador++;
    }
    else {
        textoTeste.textContent = "Voltei para o teste, respeita!";
        contador--;
    }
}

// Teste 2
function MaiorIdade(){
    const idade = document.getElementById("idade").value;
    const resposta = document.getElementById("resposta");
    if(!isNaN == idade){
        if(idade >= 18){
            resposta.textContent = "Você é maior de idade"
        }
        else {
            resposta.textContent = "Você é menor de idade"
        }
    }
    else {
        resposta.textContent = "Digite uma idade válida"
    }

}

