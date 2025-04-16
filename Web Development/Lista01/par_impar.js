// cria um input, interação no console
const readline = require("readline").createInterface({
    input: process.stdin, // define a entrada de dados padrão
    output: process.stdout // define a saída de dados padrão
});

// Exiba uma pergunta no terminal
readline.question(`Digite um número -> `, (num) => {
    numero = parseInt(num);
    if(isNaN(numero)){
        console.log("A entrada não é um número inteiro")
    }
    else{
        if(numero%2 == 1) {
            console.log("Este número é ímpar");
        }
        else{
            console.log("Este Número é par");
        }
    }
    readline.close();
});

// Fechando a interface

