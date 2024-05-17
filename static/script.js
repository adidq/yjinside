$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
    
    $('#toggleTheme').click(function() {
        var $htmlElement = $('html');
        var currentTheme = $htmlElement.attr('data-theme');

        if (currentTheme === 'light') {
            $htmlElement.attr('data-theme', 'dark');
            $('#currentTheme').text('dark');
        } else {
            $htmlElement.attr('data-theme', 'light');
            $('#currentTheme').text('light');
        }
    });
});