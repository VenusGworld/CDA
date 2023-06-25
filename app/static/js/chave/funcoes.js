var exampleModal = document.getElementById('modalLogin')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var recipient = button.getAttribute('data-bs-url');
    var recipient2 = button.getAttribute('data-bs-acao');
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    //var msg = exampleModal.querySelector('.msg')
    //msg.textContent = "Deseja realmente excluir o usuário " + recipient + "?"

    var url = exampleModal.querySelector('.url');
    url.value = recipient
    var acao = exampleModal.querySelector('.acao');
    acao.value = recipient2
})

function validaDevolucao(){
    
}