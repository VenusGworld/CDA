var modalExcluir = document.getElementById('modalExcluir')
modalExcluir.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var recipient = button.getAttribute('data-bs-whatever')
    var recipient2 = button.getAttribute('data-bs')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    var msg = modalExcluir.querySelector('.msg')
    msg.textContent = "Deseja realmente excluir o(a) Funcionário(a) " + recipient + "?"

    var link = modalExcluir.querySelector('.btn-outline-danger')
    link.setAttribute("href", `/admin/funcionario/excluir-funcionario/${recipient2}`);
})



function verificaCrachaMaquina(){
    var div = document.getElementById("alert");
    var msg = document.getElementById("msg");
    var cracha = document.getElementById("cracha").value;
    var maquina = document.getElementById("maquina").value;
    var botao = document.getElementById("btnGravar").value;
    var respCracha = false;
    var respMaquina = true;

    if (botao != "Editar"){
        $.ajax({
            url: `/cracha-pesquisa/${cracha.trim()}/0`,
            type: 'GET',
            async: false,
            dataType: 'json',
            contentType: 'application/json',
            success: function(data){
                respCracha = data;
            }
        });
    
    }else{
        var idFunc = document.getElementById("id").value;
        
        $.ajax({
            url: `/cracha-pesquisa/${cracha.trim()}/${idFunc.trim()}`,
            type: 'GET',
            async: false,
            dataType: 'json',
            contentType: 'application/json',
            success: function(data){
                respCracha = data;
            }
        });
    }

    if (maquina.trim() != ""){
        $.ajax({
            url: `/maquina-pesquisa/${maquina.trim()}`,
            type: 'GET',
            async: false,
            dataType: 'json',
            contentType: 'application/json',
            success: function(data){
                respMaquina = data;
            }
        });
    }

    if (respCracha){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O crácha informado já existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    } else if (!respMaquina){
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O máquina informada não existe</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    }else{
        return true;
    }
}