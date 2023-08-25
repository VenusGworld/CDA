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
    msg.textContent = "Deseja realmente excluir o usuário " + recipient + "?"

    var link = modalExcluir.querySelector('.btn-outline-danger')
    link.setAttribute("href", `/admin/usuario/excluir-usuario/${recipient2}`);
})


function validarUsuarioeSenha(campo1, campo2){
    /*
    # Função que valida se usuário já existe e se as senha que foram informadas estão iguais.
    
    # PARAMETROS:
    #   campo1 = Senha digitada no input de senha;
    #   campo2 = Senha digitada no input de confirme a senha.
    
    # RETORNOS:
    #   return true = Retorna true caso esteja tudo certo;
    #   return false = Retorna flase com mesnagem do erro.
    */

    var senha1 = document.getElementById(campo1).value;
    var senha2 = document.getElementById(campo2).value;
    var div = document.getElementById("alert");
    var msg = document.getElementById("msg");

    if (senha1 != "" && senha2 != "" && senha1 === senha2){
        if (!verificaUsuario()){
            return false;
        }else{
            return true;
        }   
    }else{
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>As senhas não coincidem!</h6>";
        document.getElementById(campo1).focus(); //Exibe mensagem de erro
        setTimeout(() =>{
            div.classList.add('none');
        }, 5000);
        return false;
    }
}


function mostrarSenha(button){
    var inputSenha = document.getElementById("senha");
    var inputConfirm = document.getElementById("senhaConfirm");

    if (inputSenha.type == "password"){
        inputSenha.type = "text";
        inputConfirm.type = "text";
        button.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
    }else{
        inputSenha.type = "password";
        inputConfirm.type = "password";
        button.innerHTML = '<i class="fa-solid fa-eye"></i>';
    }
}


function verificaUsuario(){
    var div = document.getElementById("alert");
    var msg = document.getElementById("msg");
    var usuario = document.getElementById("usuario").value;
    var botao = document.getElementById("btnGravar").value;
    var respUsuario = false;

    if (botao != "Editar"){
        $.ajax({
            url: `/usuario-pesquisa/${usuario.trim()}/0`,
            type: 'GET',
            async: false,
            dataType: 'json',
            contentType: 'application/json',
            success: function(data){
                respUsuario = data;
            }
        });

        if (respUsuario){
            div.classList.remove('none');
            msg.innerHTML = "";
            msg.innerHTML = "<h6 class='msg-alert'>O usuário informado já existe</h6>";
            setTimeout(() =>{
                div.classList.add('none');
            }, 6000);
            return false;
        }else{
            return true
        }
    }else{
        var idUsuario = document.getElementById("id").value;
        
        $.ajax({
            url: `/usuario-pesquisa/${usuario.trim()}/${idUsuario.trim()}`,
            type: 'GET',
            async: false,
            dataType: 'json',
            contentType: 'application/json',
            success: function(data){
                respUsuario = data;
            }
        });

        if (respUsuario){
            div.classList.remove('none');
            msg.innerHTML = "";
            msg.innerHTML = "<h6 class='msg-alert'>O usuário informado já existe</h6>";
            setTimeout(() =>{
                div.classList.add('none');
            }, 6000);
            return false;
        }else{
            return true
        }
    }
}