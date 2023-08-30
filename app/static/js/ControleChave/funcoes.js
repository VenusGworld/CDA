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


function verificaDataEObservacao(dtRet, hrRet, dtDev, hrDev, obs){
    let dataRet = new Date(dtRet.value);
    let dataDev = new Date(dtDev.value);
    let horaRet = hrRet.value;
    let horaDev = hrDev.value;
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");

    if ( obs.value.length < 15){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>Observação precisa ter mais que 15 caracteres.!</h6>";
        window.scrollTo({
            top: 0,
            behavior: "smooth"
          });
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false
    } else if ( dataDev.getTime() < dataRet.getTime()){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>Data de devolução menor que a data de retirada!</h6>";
        window.scrollTo({
            top: 0,
            behavior: "smooth"
          });
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false
    } else if (dataDev.getTime() === dataRet.getTime() && horaDev < horaRet ){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>Hora de devolução menor que a hora de retirada!</h6>";
        window.scrollTo({
            top: 0,
            behavior: "smooth"
          });
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false
    } else{
        return true
    }
}