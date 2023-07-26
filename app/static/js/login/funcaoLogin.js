var modalLogin = document.getElementById('modalLogin')
modalLogin.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var recipient = button.getAttribute('data-bs-url');
    var recipient2 = button.getAttribute('data-bs-acao');
    var recipient3 = button.getAttribute('data-bs-id');

    var url = document.getElementById('urlDest');
    url.value = recipient;
    var acao = document.getElementById('acao');
    acao.value = recipient2;
    var id = document.getElementById("idModalLogin");
    id.value = recipient3;
})