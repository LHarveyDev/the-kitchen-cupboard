$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});

$('.dropdown-trigger').dropdown();

//Textarea auto resize
$('#textarea1').val('New Text');
M.textareaAutoResize($('#textarea1'));