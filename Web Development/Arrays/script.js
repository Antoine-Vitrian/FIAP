
// arrays
// podem conter:
const array01 = [1,"abc",null,undefined,true, {chave: "valor"}];

const cores = new Array("preto", "azul", "verde");

const vazio = [];

// Chamando primeiro elemento
const linguagens = ["Python", "Java", "Javascript", "C#"];
const primeira = linguagens[0];
console.log(primeira);

// chamando último elemento
const ultima = linguagens[linguagens.length-1];
console.log(ultima)

// adicionar 
let palmeiras = ["Piquerez", "Vitor Roque", "Flaco López"];
palmeiras[palmeiras.length] = "Raphael Veiga"
console.log(palmeiras);

// Adiconar elementos ao final da array
// Push()
let planetas = ["Terra", "Marte"];
planetas.push("Saturno", "Urano");
console.log(planetas);
// Remove o último elemento: pop()
// Remove o primeiro elemento: shift()
planetas.pop();
console.log(planetas);

// indexOf(): Retorna o primeiro indice encontraqdo pela array
const index = planetas.indexOf("Terra");
console.log(index);

// join() - juntar
const joinTeste = planetas.join("\n");
console.log(joinTeste);

// trim(): remove os espaços em branco


// let pilotos = [];
// function adicionarTeste() {
//     const form = document.getElementById("dados").value;
//     pilotos.push(form);
//     let h1Create = document.createElement("h1");
//     h1Create.textContent = `${pilotos}`;


// }

