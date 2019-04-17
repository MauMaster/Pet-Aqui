$(function() {
    $('.pop2').on('click', function() {
       $(this).closest(".imagemodal").next(".delete").modal('show');   
    });     
 });