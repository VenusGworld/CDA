var dadosGerManut = []

$.ajax({
    url: '/lista-gerentes-manutencao',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    success: function(resp){
        for(x in resp.data){
            //Verifica se o usuário que está logado é do grupo ADM
            if (resp.login === "ADM"){
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp.data[x].id}" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }else{
                var strDev = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-acao="DEVOLUCAO" data-bs-id=${resp.data[x].id} data-bs-toggle="modal" class="btn btn-warning btn-sm"><i class="fa-solid fa-person-walking-arrow-right"></i></a></div>`
            }
           dataresp = {
            gerente: resp.data[x].nome,
            entrada: resp.data[x].entrada,
            saida: resp.data[x].saida,
            acoes: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: space-evenly;">
            <a href="/admin/controle-chave/incluir-devolucao/" class="btn btn-warning btn-sm"><i class="fa-regular fa-pen-to-square"></i></a>
            <a href="/admin/controle-chave/incluir-devolucao/" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash-can"></i></a>
            </div>`)
           }
           dadosGerManut.push(dataresp)
        }
    }
});


var colunasGerManut =[
    {
        id: 'gerente',
        name: 'Gerente'
    },
    {
        id: 'entrada',
        name: "Entrada"
    },
    {
        id: 'saida',
        name: "Saída"
    },
    {
        id: 'acoes',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Ações</span>")
    }
]