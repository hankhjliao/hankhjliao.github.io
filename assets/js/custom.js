$(function () {
    Footnotes.setup();
});

var Footnotes = {
    footnotetimeout: false,

    setup: function () {
        var footnotelinks = $("a[class='footnote-ref']")

        footnotelinks.unbind('mouseover', Footnotes.footnoteover);
        footnotelinks.unbind('mouseout', Footnotes.footnoteoout);

        footnotelinks.bind('mouseover', Footnotes.footnoteover);
        footnotelinks.bind('mouseout', Footnotes.footnoteoout);
    },

    footnoteover: function () {
        clearTimeout(Footnotes.footnotetimeout);

        $('#footnote-div').stop();
        $('#footnote-div').remove();

        var id = $(this).attr('href').substr(1);
        var el = document.getElementById(id);
        var position = $(this).offset();

        var div = $(document.createElement('div'));
        div.attr('id', 'footnote-div');
        div.bind('mouseover', Footnotes.divover);
        div.bind('mouseout', Footnotes.footnoteoout);
        div.html($(el).html());
        div.find("a[class='footnote-backref']").remove();
        div.css({ position: 'absolute' });
        div.addClass('footnote-hover');
        $(document.body).append(div);

        var left = position.left;
        if (left + 420 > $(window).width() + $(window).scrollLeft())
            left = $(window).width() - 420 + $(window).scrollLeft();
        var top = position.top + 20;
        if (top + div.height() > $(window).height() + $(window).scrollTop())
            top = position.top - div.height() - 15;

        div.css({
            left: left,
            top: top
        });
    },

    footnoteoout: function () {
        Footnotes.footnotetimeout = setTimeout(function () {
            $('#footnote-div').remove();
        }, 100);
    },

    divover: function () {
        clearTimeout(Footnotes.footnotetimeout);
        $('#footnote-div').stop();
    }
}

$('.post-content img').click(function () {
    var src = $(this).attr('src');
    var modal;

    function removeModal() {
        modal.remove();
        $(document.body).off('keyup.modal-close');
    }

    modal = $('<div>').css({
        background: 'rgba(0,0,0,.75) no-repeat center / 80% url(' + src + ')',
        position: 'fixed',
        zIndex: '9999',
        top: '0',
        left: '0',
        right: '0',
        bottom: '0',
        cursor: 'zoom-out'
    }).click(function () {
        removeModal();
    }).appendTo(document.body);

    $(document.body).on('keyup.modal-close', function (e) {
        if (e.key === 'Escape') {
            removeModal();
        }
    });
});