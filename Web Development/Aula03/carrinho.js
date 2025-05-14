const inputNovoItem = document.getElementById('novo-item');
const botaoAdicionar = document.getElementById('adicionar-ao-carrinho')
const listaItems = document.getElementById('lista-items');

const chaveCarrinho = 'itensCarrinho';

function obterCarrinho(){
    const carrinhoSalvo = sessionStorage.getItem(chaveCarrinho);
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
}

let carrinho = obterCarrinho();
exibirCarrinho();

function exibirCarrinho(){
    listaItems.innerHTML = '';

    carrinho.array.forEach(item => {
        const listaItem = document.createElement('li');
        listaItem.textContent = item;
        listaItems.appendChild(listaItem);
    });
}

botaoAdicionar.addEventListener('click', ()=>{
    const novoItem = inputNovoItem.ariaValueMax.trim();

    if(novoItem != ''){
        carrinho.push(novoItem);
        sessionStorage.setItem(chaveCarrinho, JSON.stringify(carrinho));
        inputNovoItem.value = '';
        exibirCarrinho();
    }
})