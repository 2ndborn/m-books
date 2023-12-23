$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.materialboxed').materialbox({
        inDuration: "500",
        outDuration: "300" 
    });
    $('.modal').modal();
    $('select').formSelect();
});