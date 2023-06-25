var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var recipient = button.getAttribute('data-bs-whatever')
    var recipient2 = button.getAttribute('data-bs')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    var msg = exampleModal.querySelector('.msg')
    msg.textContent = "Deseja realmente excluir o(a) Funcionário(a) " + recipient + "?"

    var link = exampleModal.querySelector('.btn-outline-danger')
    link.setAttribute("href", `/adm/excluir-usuario/${recipient2}`);
})



function validarSenha(campo1, campo2){
    /*
    # Função que valida se as senha que foram informadas estão iguais.
    
    # PARAMETROS:
    #   campo1 = Senha digitada no input de senha;
    #   campo2 = Senha digitada no input de confirme a senha.
    
    # RETORNOS:
    #   return true = Retorna true caso esteja tudo certo;
    #   return false = Retorna flase com mesnagem do erro.
    */

    var senha1 = document.getElementById(campo1).value;
    var senha2 = document.getElementById(campo2).value;
    var div = document.getElementById("alert")

    if (senha1 != "" && senha2 != "" && senha1 === senha2){
        return true;
    }else{
        div.style.display = "block";
        document.getElementById(campo1).focus(); //Exibe mensagem de erro
        setTimeout(() =>{
            div.style.display = "none";
        }, 5000);
        return false;
    }
}

function mostarSenha(button){
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


function fechaAlert(){
    /*
    # Função que fecha o alert da função validarSenha(campo1, campo2).
    
    # PARAMETROS:
    #   Não tem parametro.
    
    # RETORNOS:
    #   Não tem retorno.
    */
    var div = document.getElementById("alert")
    div.style.display = "none"
}


    

