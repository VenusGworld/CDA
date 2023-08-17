function verificaSaidaGerente(){
    var gerente = document.getElementById("gerente").value.split(" ");
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    var respGer = false;

    $.ajax({
        url: `/gerenteSai-pesquisa-mov/${gerente[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respGer = data;
        }
    });

    if (!respGer){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O gerente informado ainda não saiu</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    }else{
        return true;
    }


}