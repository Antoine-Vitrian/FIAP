const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question(`Digite o preço do produto -> `, (preco) => {
    const precoInt = parseFloat(preco);
    const desconto = 0.1;
    console.log(`Você teve 10% desconto, sua compra ficou R$${precoInt - (precoInt*desconto)}`);

    readline.close();
});

