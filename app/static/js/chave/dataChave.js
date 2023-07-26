var dadosChave = []

$.ajax({
    url: '/lista-chaves',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp[1]){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp[0].login === "ADM"){
                var excluir = `<a href="/admin/chave/excluir-chave-modal/${resp[1][x].id}" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>`
                var editar = `<a href="/admin/chave/editar-chave-modal/${resp[1][x].id}" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>`
            }else{
                var excluir = `<a class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EXCLUIR_CHAVE" data-bs-id=${resp[1][x].id} data-bs-url="/vig/chave/excluir-chave-modal/${resp[1][x].id}" data-bs-toggle="modal"><i class="fa-solid fa-trash-can"></i></a>`
                var editar = `<a class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="EDITAR_CHAVE" data-bs-id=${resp[1][x].id} data-bs-url="/vig/chave/editar-chave-modal/${resp[1][x].id}" data-bs-toggle="modal"><i class="fa-regular fa-pen-to-square"></i></a>`
            }
           dataresp = {
            codigo: resp[1][x].codigo,
            nome: resp[1][x].nome,
            acoes: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">`+
                        editar +
                        excluir +
                    `</div>`
           }
           dadosChave.push(dataresp)
        }
    }
});


var colunasChave = {
    "codigo": "Código",
    "nome": "Nome",
    "acoes": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Ações</span>"
}