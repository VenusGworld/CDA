var dadosChaveRet = []

$.ajax({
    url: '/lista-chaves-retiradas',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao-modal/${resp.data[x].id}" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="INCLUIR_DEV_CHAVE" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-chave/incluir-devolucao-modal/${resp.data[x].id}"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            chave: resp.data[x].nome,
            retirada: resp.data[x].retirada,
            responsavel: resp.data[x].responsavel,
            devolucao: gridjs.html(strDev),
           }
           dadosChaveRet.push(dataresp)
        }
    }
});


var colunasChaveRet = [
    {
        id: 'chave',
        name: 'Chave'
    },
    {
        id: 'retirada',
        name: 'Retirada'
    },
    {
        id: 'responsavel',
        name: "Responsável"
    },
    {
        id: 'devolucao',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Devolução ?</span>")
    }
]