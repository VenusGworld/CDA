var dadosChaveRet = []

$.ajax({
    url: '/lista-chaves-retiradas',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp){
           dataresp = {
            chave: resp[x].nome,
            retirada: resp[x].retirada,
            responsavel: resp[x].responsavel,
            saida: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="DEVOLUCAO" data-bs-url="" data-bs-toggle="modal" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`,
           }
           dadosChaveRet.push(dataresp)
        }
    }
});


var colunasChaveRet = {
    "chave": "Chave",
    "retirada": "Retirada",
    "responsavel": "Responsavel",
    "saida": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Saída ?</span>",
}