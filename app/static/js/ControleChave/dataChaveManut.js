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
                var visu = `<a href="/admin/controle-chave/manutencao-chave/modal-visualizacao-controle-chave/${resp.data[x].id}" title="VISUALIZAR" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a>`
                var editar = `<a href="/admin/controle-chave/manutencao-chave/edicao-controle-chave/${resp.data[x].id}" title="EDITAR" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>`
                var excluir = `<a href="/admin/controle-chave/manutencao-chave/modal-exlusao-controle-chave/${resp.data[x].id}" title="EXCLUIR" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>`
            }else{
                var visu = `<a href="/vig/controle-chave/manutencao-chave/modal-visualizacao-controle-chave/${resp.data[x].id}" title="VISUALIZAR" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a>`
                var editar = `<a class="btn btn-warning btn-sm" title="EXCLUIR" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EXCLUIR_CHAVE" data-bs-id=${resp.data[x].id} data-bs-url="/vig/controle-chave/manutencao-chave/edicao-controle-chave/${resp.data[x].id}" data-bs-toggle="modal"><i class="fa-regular fa-pen-to-square"></i></a>`
                var excluir = `<a class="btn btn-danger btn-sm" title="EXCLUIR" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EXCLUIR_CONTROLE_CHAVE" data-bs-id=${resp.data[x].id} data-bs-url="/vig/controle-chave/manutencao-chave/modal-exlusao-controle-chave/${resp.data[x].id}" data-bs-toggle="modal"><i class="fa-solid fa-trash-can"></i></a>`
            }
           dataresp = {
            chave: resp.data[x].nome,
            retirada: resp.data[x].retirada,
            devolucao: resp.data[x].devolucao,
            respRet: resp.data[x].respRet,
            acoes: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">`
            + visu
            + editar
            + excluir
            + `</div>`)
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