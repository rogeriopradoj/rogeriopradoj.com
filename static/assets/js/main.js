
(function() {
    acelayablog.initHighlightjs();
})();

$(document).ready(function() {
    acelayablog.initSearchForm();
    acelayablog.initShareButtons();
    acelayablog.initSearch();
    acelayablog.initToTopButton();

    $('.post-reading').show();
    // Calculates Reading Time
    $('.post-content').readingTime({
        readingTimeTarget: '.post-reading-time',
        wordCountTarget: '.post-word-count',
        lessThanAMinuteString: 'Menos de um minuto'
    });
});