// Lista de frases de notícias reais
const noticiasReais = [
    "Brasil ultrapassa 75% da população com vacinação completa contra a COVID-19.",
    "NASA confirma descoberta de água congelada em crateras da Lua.",
    "Inflação no Brasil desacelera e fecha abril com alta de 0,38%.",
    "Apple anuncia novos iPads com chip M4 e tela OLED.",
    "Amazônia registra queda de 40% no desmatamento nos primeiros meses de 2025.",
    "Morre o cartunista Ziraldo aos 91 anos no Rio de Janeiro.",
    "ONU alerta para aumento recorde de deslocados por conflitos em 2024.",
    "Governo federal antecipa pagamento do 13º para aposentados do INSS.",
    "Anvisa aprova novo medicamento nacional contra diabetes tipo 2.",
    "Tempestades causam alagamentos em São Paulo e afetam mais de 15 bairros."
  ];
  
  // Lista de frases de fake news
  const fakeNews = [
    "Vacina contra COVID-19 altera o DNA humano permanentemente.",
    "NASA confirma que o planeta Terra vai ficar 6 dias no escuro total.",
    "Beber água quente cura o coronavírus, segundo estudo chinês.",
    "Bill Gates planeja implantar chips de controle nas vacinas.",
    "Leite de vaca causa câncer, segundo novo estudo da OMS.",
    "Estudo comprova que usar máscara causa intoxicação por CO2.",
    "WhatsApp será desativado em todo o Brasil a partir do próximo mês.",
    "Lula vai fechar igrejas evangélicas até o fim do mandato.",
    "Coca-Cola muda fórmula e inclui substância viciante para aumentar vendas.",
    "China libera mosquito geneticamente modificado que transmite COVID-19."
  ];

  function verificar(){
    const resultado = document.getElementById("resposta");
    const noticia = document.getElementById("valor").value;
    
    if(noticiasReais.includes(noticia)){
        resultado.textContent = "😃Fato Verificado😃";
    }
    else if(fakeNews.includes(noticia)){
        resultado.textContent = "😡Fake News😡";
    }
    else{
        resultado.textContent = "😢Não foi possível fazer a verificação!😢";
    }
  };

  