function verificaObservacao(observacao){
    var alert = document.getElementById("alert-excluir");

    if (observacao.value.trim().length < 15){
        alert.classList.remove("none");
        setTimeout(() =>{
            alert.classList.add("none");
        }, 5000);
        return false
    }else{
        return true
    }
    
}

function verificaData(dtRet, hrRet, dtDev, hrDev){
    let dataRet = new Date(dtRet.value);
    let dataDev = new Date(dtDev.value);
    let horaRet = hrRet.value;
    let horaDev = hrDev.value;
    let div = document.getElementById("alert");
    let msg = document.querySelector(".msg-alert");
    let tipoMsg = dtRet.getAttribute('data-bs');
    let msgH6 = "";

    if ( dataDev.getTime() < dataRet.getTime()){
        div.classList.remove('none');
        msg.innerHTML = "";
        if (tipoMsg === "RET"){
            msgH6 = "<h6 class='msg-alert'>Data de devolução menor que a data de retirada!</h6>";
        }else{
            msgH6 = "<h6 class='msg-alert'>Data de entrada menor que a data de saída!</h6>";
        }
        msg.innerHTML = msgH6;
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
        if (tipoMsg === "RET"){
            msgH6 = "<h6 class='msg-alert'>Hora de devolução menor que a hora de retirada!</h6>";
        }else{
            msgH6 = "<h6 class='msg-alert'>Hora de entrada menor que a hora de saída!</h6>";
        }
        msg.innerHTML = msgH6;
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


function verificaDataEObservacao(dtRet, hrRet, dtDev, hrDev, obs){
    let dataRet = new Date(dtRet.value);
    let dataDev = new Date(dtDev.value);
    let horaRet = hrRet.value;
    let horaDev = hrDev.value;
    let div = document.getElementById("alert");
    let msg = document.querySelector(".msg-alert");
    let tipoMsg = dtRet.getAttribute('data-bs');
    let msgH6 = "";

    if ( obs.value.trim().length < 15){
        div.classList.remove('none');
        msg.innerHTML = "";
        msgH6 = "<h6 class='msg-alert'>Observação precisa ter mais que 15 caracteres!</h6>";
        msg.innerHTML = msgH6;
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
        if (tipoMsg === "RET"){
            msgH6 = "<h6 class='msg-alert'>Data de devolução menor que a data de retirada!</h6>";
        }else{
            msgH6 = "<h6 class='msg-alert'>Data de entrada menor que a data de saída!</h6>";
        }
        msg.innerHTML = msgH6;
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
        if (tipoMsg === "RET"){
            msgH6 = "<h6 class='msg-alert'>Hora de devolução menor que a hora de retirada!</h6>";
        }else{
            msgH6 = "<h6 class='msg-alert'>Hora de entrada menor que a hora de saída!</h6>";
        }
        msg.innerHTML = msgH6;
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