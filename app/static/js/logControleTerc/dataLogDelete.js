var dadosLogControlTercDel = []

$.ajax({
    url: '/lista-logs-controle-terceiros',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       acao: "DELETE"
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-terceiro/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-terceiro/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            terc: resp.data[x].movTerc.terceiro.nome.substring(0, 15),
            motivo: resp.data[x].movTerc.motivo.substring(0, 15),
            visualizar: gridjs.html(visu)
           }
           dadosLogControlTercDel.push(dataresp)
        }
    }
});


var colunasLogControlTercDel = [
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
        id: 'terc',
        name: "Visitante"
    },
    {
        id: 'motivo',
        name: "Motivo"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]