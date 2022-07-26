$(document).ready(function () {
    var modal = $('.modal');
    var modalBtn = $('[data-toggle=modal]');
    var closeBtn = $('.modal__close');

    modalBtn.on('click', function () {
        modal.toggleClass('modal--visible');
    });
    closeBtn.on('click', function () {
        modal.toggleClass('modal--visible');
    });
});