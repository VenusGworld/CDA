var dadosTerceiro = []

$.ajax({
    url: '/lista-terceiros',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var excluir = `<a href="/admin/terceiro/excluir-terceiro-modal/${resp.data[x].id}" title="EXCLUIR" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>`
                var editar = `<a href="/admin/terceiro/editar-terceiro-modal/${resp.data[x].id}" title="EDITAR" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>`
            }else{
                var excluir = `<a class="btn btn-danger btn-sm" data-bs-toggle="modal" title="EXCLLUIR" data-bs-target="#modalLogin" data-bs-acao="EXCLUIR_TERCEIRO" data-bs-id=${resp.data[x].id} data-bs-url="/vig/terceiro/excluir-terceiro-modal/${resp.data[x].id}" data-bs-toggle="modal"><i class="fa-solid fa-trash-can"></i></a>`
                var editar = `<a class="btn btn-warning btn-sm" data-bs-toggle="modal" title="EDITAR" data-bs-target="#modalLogin" data-bs-acao="EDITAR_TERCEIRO" data-bs-id=${resp.data[x].id} data-bs-url="/vig/terceiro/editar-terceiro-modal/${resp.data[x].id}" data-bs-toggle="modal"><i class="fa-regular fa-pen-to-square"></i></a>`
            }
           dataresp = {
            codigo: resp.data[x].codigo,
            nome: resp.data[x].nome,
            cpf: resp.data[x].cpf,
            editar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">`+
                        editar +
                    `</div>`),
            excluir: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">`+
                    excluir +
                `</div>`)
           }
           dadosTerceiro.push(dataresp)
        }
    }
});


var colunasTerceiro = [
    {
        id: 'codigo',
        name: 'Código'
    },
    {
        id: 'nome',
        name: 'Nome'
    },
    {
        id: 'cpf',
        name: "CPF"
    },
    {
        id: 'editar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Editar</span>")
    },
    {
        id: 'excluir',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Excluir</span>")
    }
]