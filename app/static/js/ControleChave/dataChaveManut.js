var dadosChaveManut = []

$.ajax({
    url: '/lista-chaves-manutencao',
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
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="DEVOLUCAO" data-bs-id=${resp[1][x].id} data-bs-toggle="modal" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            chave: resp[1][x].nome,
            retirada: resp[1][x].retirada,
            devolucao: resp[1][x].devolucao,
            respRet: resp[1][x].respRet,
            acoes: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">
            <a href="/admin/controle-chave/incluir-devolucao/" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a>
            <a href="/admin/controle-chave/incluir-devolucao/" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>
            <a href="/admin/controle-chave/incluir-devolucao/" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>
            </div>`
           }
           dadosChaveManut.push(dataresp)
        }
    }
});


var colunasChaveManut = {
    "chave": "Chave",
    "retirada": "Retirada",
    "devolucao": "Devolução",
    "respRet": "Responsavel Ret.",
    "acoes": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Ações</span>"
}