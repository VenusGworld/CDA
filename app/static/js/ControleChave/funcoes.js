function verificaChavRespDev(){
    
    var chave = document.getElementById("chave").value.split(" ");
    var resp = document.getElementById("responsavel").value.split(" ");
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    var respChave = false;
    var respResp = false;
    var respRet = false;

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

    $.ajax({
        url: `/funcionario-pesquisa-mov/${resp[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respResp = data;
        }
    });

    $.ajax({
        url: `/chaveRet-pesquisa-mov/${chave[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respRet = data;
        }
    });

    if (!respChave){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>A chave informada não existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    } else if (!respResp){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O responsavel informado não existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    } else if (!respRet){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>A chave informada não foi devolvida</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    }else{
        return true;
    }

}
