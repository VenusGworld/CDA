var dadosLogUserInsert = []

$.ajax({
    url: '/lista-logs-usuario-insert',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp){
           dataresp = {
            acao: resp[x].acao,
            data: resp[x].dataHora,
            resp: resp[x].resp,
            usuario: resp[x].usuario.us_usuario,
            visualizar: `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp[x].id}" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a></div>`
           }
           dadosLogUserInsert.push(dataresp)
        }
    }
});


var colunasLogUserInsert = {
    "acao": "Ação",
    "data": "Data",
    "resp": "Responsável",
    "usuario": "Usuário",
    "visualizar": "<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>"
}