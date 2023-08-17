var dadosFunc = []

$.ajax({
    url: '/lista-funcionarios',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp){
           dataresp = {
            cracha: resp[x].cracha,
            nome: resp[x].nome,
            maquina: resp[x].maquina,
            gerente: resp[x].gerente,
            editar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/funcionario/editar-funcionario/${resp[x].id}" class="btn btn-warning btn-sm" title="EDITAR"><i class="fa-regular fa-pen-to-square"></i></a></div>`),
            excluir: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-danger btn-sm" title="EXCLUIR" data-bs-toggle="modal" data-bs-target="#modalExcluir" data-bs-whatever="${resp[x].nome}" data-bs=${resp[x].id}><i class="fa-solid fa-trash-can"></i></a></div>`)
           }
           dadosFunc.push(dataresp)
        }
    }
});


var colunasFunc = [
    {
        id: 'cracha',
        name: 'Crachá'
    },
    {
        id: 'nome',
        name: 'Nome'
    },
    {
        id: 'maquina',
        name: "Máquina"
    },
    {
        id: 'gerente',
        name: "Gerente"
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

