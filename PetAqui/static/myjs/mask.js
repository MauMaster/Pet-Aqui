$(document).ready(function(){
    $('.cpf').mask('999.999.999-99').on("keydown", function(e){
       
       var key = e.key; // pega o valor da tecla
       var keycode = e.keyCode || e.which; // pega o código da tecla
       var teclas = [
          8,    // backspace
          16,   // shift
          17,   // ctrl
          35,   // end
          36,   // home
          37,   // ←
          39,   // →
          46,   // delete
          13,    // enter
          9
       ];
       if(isNaN(key) && !~teclas.indexOf(keycode)){
          return false;
       }
    });
 });
 $(document).ready(function(){
    $('.phone_with_ddd').mask('(99) 99999-9999').on("keydown", function(e){
       
       var key = e.key; // pega o valor da tecla
       var keycode = e.keyCode || e.which; // pega o código da tecla
       var teclas = [
          8,    // backspace
          16,   // shift
          17,   // ctrl
          35,   // end
          36,   // home
          37,   // ←
          39,   // →
          46,   // delete
          13,    // enter
          9
       ];
       if(isNaN(key) && !~teclas.indexOf(keycode)){
          return false;
       }
    });
 });
 $(document).ready(function(){
    $('.cep').mask('99999-999').on("keydown", function(e){
       
       var key = e.key; // pega o valor da tecla
       var keycode = e.keyCode || e.which; // pega o código da tecla
       var teclas = [
          8,    // backspace
          16,   // shift
          17,   // ctrl
          35,   // end
          36,   // home
          37,   // ←
          39,   // →
          46,   // delete
          13,    // enter
          9
       ];
       if(isNaN(key) && !~teclas.indexOf(keycode)){
          return false;
       }
    });
 });
 $(document).ready(function(){
    $('.data').mask('99/99/9999').on("keydown", function(e){
       
       var key = e.key; // pega o valor da tecla
       var keycode = e.keyCode || e.which; // pega o código da tecla
       var teclas = [
          8,    // backspace
          16,   // shift
          17,   // ctrl
          35,   // end
          36,   // home
          37,   // ←
          39,   // →
          46,   // delete
          13,    // enter
          9
       ];
       if(isNaN(key) && !~teclas.indexOf(keycode)){
          return false;
       }
    });
 });
 $(document).ready(function(){
    $('.numero').mask('00000').on("keydown", function(e){
       
       var key = e.key; // pega o valor da tecla
       var keycode = e.keyCode || e.which; // pega o código da tecla
       var teclas = [
          8,    // backspace
          16,   // shift
          17,   // ctrl
          35,   // end
          36,   // home
          37,   // ←
          39,   // →
          46,   // delete
          13,    // enter
          9
       ];
       if(isNaN(key) && !~teclas.indexOf(keycode)){
          return false;
       }
    });
 });

