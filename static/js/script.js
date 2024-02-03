$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});

$(document).ready(function(){
    $('select').formSelect();
  });

//Textarea auto resize
$('#textarea1').val('New Text');
M.textareaAutoResize($('#textarea1'));

$('.tooltipped').tooltip();