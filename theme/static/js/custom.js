$(function () {
    console.log('run');
    $('table').each(function () {
        $(this).addClass('table table-sm table-hover');
        $(this).wrap('<div class="table-responsive"></div>');
    });
});
