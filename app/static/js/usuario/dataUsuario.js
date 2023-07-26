var dadosUser = []

$.ajax({
    url: '/lista-usuarios',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp){
           dataresp = {
            nome: resp[x].nome,
            usuario: resp[x].usuario,
            grupo: resp[x].grupo,
            editar: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/usuario/editar-usuario/${resp[x].id}" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a></div>`,
            excluir: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modalExcluir" data-bs-whatever="${resp[x].usuario}" data-bs=${resp[x].id}><i class="fa-solid fa-trash-can"></i></a></div>`
           }
           dadosUser.push(dataresp)
        }
    }
});


var colunasUser = {
    "nome": "Nome",
    "usuario": "Usuário",
    "grupo": "Grupo",
    "editar": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Editar</span>",
    "excluir": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Excluir</span>"
}