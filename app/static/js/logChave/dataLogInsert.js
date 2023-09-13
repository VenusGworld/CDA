var dadosLogChaveInsert = []

$.ajax({
    url: '/lista-logs-chaves',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
        tipo: "INSERT"
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-manter-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-manter-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }

           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            codigo: resp.data[x].chave.codigo,
            chave: resp.data[x].chave.nome.substring(0, 15),
            visualizar: gridjs.html(visu)
           }
           dadosLogChaveInsert.push(dataresp)
        }
    }
});


var colunasLogChaveInsert = [
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