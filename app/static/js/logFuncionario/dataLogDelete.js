var dadosLogFuncDelete = []

$.ajax({
    url: '/lista-logs-funcionarios',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       acao: "DELETE"
    }),
    success: function(resp){
        for(x in resp){
           dataresp = {
            acao: resp[x].acao,
            data: resp[x].dataHora,
            resp: resp[x].resp,
            cracha: resp[x].func.cracha,
            func: resp[x].func.nome.substring(0, 15),
            visualizar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-manter-funcionario/${resp[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`)
           }
           dadosLogFuncDelete.push(dataresp)
        }
    }
});


var colunasLogFuncDelete = [
    {
        id: 'acao',
        name: 'Ação',
        width: '120px'
    },
    {
        id: 'data',
        name: 'Data'
    },
    {
        id: 'resp',
        name: "Responsável"
    },
    {
        id: 'cracha',
        name: "Crachá"
    },
    {
        id: 'func',
        name: "Funcionário"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]