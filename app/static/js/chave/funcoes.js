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