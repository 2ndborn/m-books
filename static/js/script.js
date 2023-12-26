$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".materialboxed").materialbox({
        inDuration: "500",
        outDuration: "300"
    });
    $(".modal").modal();
    $("select").formSelect();
    $("#title_year").on("input", function () {
        if ($(this).val().length > 4) {
            $(this).val($(this).val().slice(0, 4));
        }
    });
});