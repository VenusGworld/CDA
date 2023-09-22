var dadosLogControlTercUp = []

$.ajax({
    url: '/lista-logs-controle-terceiros',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
        tipo: "UPDATE"
    }),
    success: function(resp){
        if (resp.login == "ADM"){
            var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
        }else{
            var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
        }
        for(x in resp.data){
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            codigo: resp.data[x].movTerc.pessoaVisit.nome,
            chave: resp.data[x].movTerc.motivo.substring(0, 15),
            visualizar: gridjs.html(visu)
           }
           dadosLogControlTercUp.push(dataresp)
        }
    }
});


var colunasLogControlTercUp = [
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
        id: 'codigo',
        name: "Código"
    },
    {
        id: 'chave',
        name: "Chave"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]