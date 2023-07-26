var dadosChaveRet = []

$.ajax({
    url: '/lista-chaves-retiradas',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp[1]){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp[0].login === "ADM"){
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp[1][x].id}" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="INCLUIR_DEV_CHAVE" data-bs-id=${resp[1][x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-chave/incluir-devolucao/${resp[1][x].id}"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            chave: resp[1][x].nome,
            retirada: resp[1][x].retirada,
            responsavel: resp[1][x].responsavel,
            devolucao: strDev,
           }
           dadosChaveRet.push(dataresp)
        }
    }
});


var colunasChaveRet = {
    "chave": "Chave",
    "retirada": "Retirada",
    "responsavel": "Responsavel",
    "devolucao": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Devolução ?</span>",
}