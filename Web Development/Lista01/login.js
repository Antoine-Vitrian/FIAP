const login = "abcd";
const senha = 1234;

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question(`Digite o login -> `, (loginTent) => {
    readline.question(`Digite a senha -> `, (senhaTent) => {
        senhaInt = parseInt(senhaTent);
        if(login == loginTent && senha == senhaInt){
            console.log("Acesso Liberado!");
        }
        else{
            console.log("Credenciais inválidas!");
        }

        readline.close();
    })
})