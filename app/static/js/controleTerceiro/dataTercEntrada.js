var dadosTercEntrada = []

$.ajax({
    url: '/lista-terceiros-entradas',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var strSaid = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-terceiro/incluir-saida-modal/${resp.data[x].id}" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strSaid = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="INCLUIR_SAID_TERC" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" data-bs-url="/vig/controle-terceiro/incluir-saida-modal/${resp.data[x].id}"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            nomeTerc: resp.data[x].nomeTerc,
            entrada: resp.data[x].entrada,
            visitado: resp.data[x].visitado,
            empresa: resp.data[x].empresa,
            saida: strSaid,
           }
           dadosTercEntrada.push(dataresp)
        }
    }
});


var colunasTercEntrada = [
    {
        id: 'nomeTerc',
        name: 'Visitante'
    },
    {
        id: 'entrada',
        name: 'Entrada'
    },
    {
        id: 'visitado',
        name: "Visitado"
    },
    {
        id: 'empresa',
        name: "Empresa"
    },
    {
        id: 'excluir',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Saída ?</span>")
    }
]