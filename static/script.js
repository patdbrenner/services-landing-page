$('#confirm-modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var recipient = button.data('service-title');

    var modal = $(this)
    modal.find('.modal-body').text('Did you want to delete "' + recipient + '"?')
});

$('#confirm-modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var id = button.data('service-id');

    var confirm = document.getElementById('modal-confirm')
    confirm.href="delete/" + id
});