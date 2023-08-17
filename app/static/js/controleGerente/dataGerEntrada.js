var dadosGerEntrada = []

$.ajax({
    url: '/lista-gerentes-entradas',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var strSaida = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-gerente/incluir-saida-modal/${resp.data[x].id}" class="btn btn-warning btn-sm" title="SAÍDA"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strSaida = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-warning btn-sm" title="SAÍDA" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="INCLUIR_SAI_GERENTE" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-gerente/incluir-saida-modal/${resp.data[x].id}"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            nome: resp.data[x].nome,
            entrada: resp.data[x].entrada,
            saida: gridjs.html(strSaida),
           }
           dadosGerEntrada.push(dataresp)
        }
    }
});


var colunasGerEntrada = [
    {
        id: 'nome',
        name: 'Nome'
    },
    {
        id: 'entrada',
        name: "Entrada"
    },
    {
        id: 'saida',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Saída ?</span>")
    }
]