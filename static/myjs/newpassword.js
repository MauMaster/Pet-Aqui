$(function(){
    // declaro variáveis de controle
    var val_email, val_email2, val_senha, val_senha2;
    
    function valida(){
       
       $('#validator')
       .prop('disabled', val_email && val_email2 && val_senha && val_senha2 ? false : true);
       
    }
    function isValidEmailAddress(emailAddress) {
       var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
       return pattern.test(emailAddress);
    }
    function validarEmail(){
   
       var email = $("#email").val().trim();
       var email2 = $("#email2").val().trim();
       // só irá verificar se os campos tiverem algo  
       if(email && email2){
          if(email != email2){
             $("#message")
             .html("Os emails não são idênticos")
             .css('color', 'red');
             val_email = false;
          }else{
             $("#message")
             .html("Os emails são idênticos")
             .css('color', 'green');
             val_email = true;
          }
          
          if(isValidEmailAddress(email)){
             $("#message2")
             .html("E-mail válido")
             .css('color', 'green');
             val_email2 = true;
          }else{
             $("#message2")
             .html("E-mail inválido")
             .css('color', 'red');
             val_email2 = false;
          }
          // chama a função de controle do botão
          valida();
       }
    }
    function validarSenha(){
       var senha = $("#id_new_password1").val();
       var senha2 = $("#id_new_password2").val();
       // só irá verificar se os campos tiverem algo
       if(senha && senha2){
     
          if(senha.length < 8 || senha.length > 16){
    
             $("#divCheckPassword2")
             .html("As senhas precisam ter no mínimo 8 caracteres e no máximo 16")
             .css('color', 'red');
             val_senha = false;
    
          }else{
    
             $("#divCheckPassword2")
             .html("")
             .css('color', 'green');
             val_senha = true;
    
          }
        
          if(senha != senha2){
    
             $("#divCheckPassword")
             .html("As senhas não são iguais")
             .css('color', 'red');
             val_senha2 = false;
    
          }else{
    
             $("#divCheckPassword").html("Senhas idênticas")
             .css('color', 'green');
             val_senha2 = true;
          }
          
          // chama a função de controle do botão
          valida();
       }
    }
   
    $('#email, #email2').on('keyup', validarEmail);
    $('#id_new_password1, #id_new_password2').on('keyup', validarSenha);
 });