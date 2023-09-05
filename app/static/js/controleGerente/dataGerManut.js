var dadosGerManut = []

$.ajax({
    url: '/lista-gerentes-manutencao',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var editar = `<a href="/admin/controle-gerente/manutencao-gerente/edicao-controle-gerente/${resp.data[x].id}" title="EDITAR" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>`
                var excluir = `<a href="/admin/controle-gerente/manutencao-gerente/modal-exlusao-controle-gerente/${resp.data[x].id}" title="EXCLUIR" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>`
            }else{
                var editar = `<a class="btn btn-warning btn-sm" title="EDITAR" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EDITAR_CONTROLE_GERENTE" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-gerente/manutencao-gerente/edicao-controle-gerente/${resp.data[x].id}"><i class="fa-regular fa-pen-to-square"></i></a>`
                var excluir = `<a class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EXCLUIR_CONTROLE_GERENTE" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-gerente/manutencao-gerente/modal-exlusao-controle-gerente/${resp.data[x].id}"><i class="fa-solid fa-trash-can"></i></a>`
            }
           dataresp = {
            gerente: resp.data[x].nome,
            entrada: resp.data[x].entrada,
            saida: resp.data[x].saida,
            acoes: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">`
            + editar
            + excluir
            + `</div>`)
           }
           dadosGerManut.push(dataresp)
        }
    }
});


var colunasGerManut =[
    {
        id: 'gerente',
        name: 'Gerente'
    },
    {
        id: 'entrada',
        name: "Entrada"
    },
    {
        id: 'saida',
        name: "Saída"
    },
    {
        id: 'acoes',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Ações</span>")
    }
]