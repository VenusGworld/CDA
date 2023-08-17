var dadosChaveManut = []

$.ajax({
    url: '/lista-chaves-manutencao',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp.data[x].id}" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="DEVOLUCAO" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            chave: resp.data[x].nome,
            retirada: resp.data[x].retirada,
            devolucao: resp.data[x].devolucao,
            respRet: resp.data[x].respRet,
            acoes: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">
            <a href="/admin/controle-chave/incluir-devolucao/" title="VISUALIZAR" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a>
            <a href="/admin/controle-chave/incluir-devolucao/" title="EDITAR" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>
            <a href="/admin/controle-chave/incluir-devolucao/" title="EXCLUIR" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>
            </div>`)
           }
           dadosChaveManut.push(dataresp)
        }
    }
});


var colunasChaveManut = [
    {
        id: 'chave',
        name: 'Chave'
    },
    {
        id: 'retirada',
        name: 'Retirada'
    },
    {
        id: 'devolucao',
        name: "Devolução"
    },
    {
        id: 'respRet',
        name: "Responsável Ret."
    },
    {
        id: 'acoes',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Ações</span>")
    }
]