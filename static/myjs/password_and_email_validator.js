$(function(){
    // declaro variáveis de controle
    var  val_senha, val_senha2;
    
    function valida(){
       
       $('#validator')
       .prop('disabled', val_senha && val_senha2 ? false : true);
       
    }

    function validarSenha(){
       var senha = $("#password1").val();
       var senha2 = $("#password2").val();
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
   
   
    $('#password1, #password2').on('keyup', validarSenha);
 });