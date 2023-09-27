function verificaChav(){
    var chave = document.getElementById("chave").value.split(" ");
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    var respChave = false;

    $.ajax({
        url: `/chave-pesquisa-mov/${chave[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respChave = data;
        }
    });

    if (!respChave && chave[0].trim().length > 0){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>A chave informada não existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    } else{
        return true;
    }

}


function verificaGerente(){
    var gerente = document.getElementById("gerente").value.split(" ");
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    var respGer = false;

    $.ajax({
        url: `/funcionario-pesquisa-mov/${gerente[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respGer = data;
        }
    });

    if (!respGer && gerente[0].trim().length > 0){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O gerente informado não existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    }else{
        return true;
    }

}
