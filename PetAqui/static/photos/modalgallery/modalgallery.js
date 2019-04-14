$(function() {
    $('.pop').on('click', function() {
          $('.imagepreview').attr('src', $(this).attr('data-img-url'));
          $('#imagemodal').modal('show');   
    });		
});