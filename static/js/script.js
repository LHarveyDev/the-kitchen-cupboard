//Collapsible sidenav bar
$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});

//Dropdown on difficulty level input field on form
$(document).ready(function(){
    $('select').formSelect();
  });

//Textarea auto resize
$('#textarea1').val('New Text');
M.textareaAutoResize($('#textarea1'));

//Tooltip on image url input field on add_recipe form
$('.tooltipped').tooltip();

//Recipe detail modal
$(document).ready(function(){
    $('.modal').modal();
});