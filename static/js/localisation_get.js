$(document).ready(function(){
   //
   $('#form_1').click(()=>{
      //
      var element = $('#element').val()
      var ensemble = $('#ensemble').val()
      //
      console.log('ensemble',ensemble)
      //
      $('#matrice').html('')
      //
      for(let i=0 ;i< ensemble;i++){
          //
          console.log(i)
          //
          $('#matrice').append(
          `
          <input id ='ens-${i}' type="text" placeholder="Ensemble ${i+1} .." class="btr">
          `
          )
          //
      }
      //
      $('#cout').html(
          `<input id='couts' type="text" placeholder="" class="btr">`
          )
      //
   })
   //
})