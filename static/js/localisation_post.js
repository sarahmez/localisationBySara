        $(document).ready(()=>{
          //
          $('#msform').submit(function(event){
            //
            event.preventDefault();
            //
            var matrix=''
            var cout=''
            //
            var element = $('#element').val()
            var ensemble = $('#ensemble').val()
            //
            for(let i=0;i< ensemble;i++){
             //
                //
                matrix=matrix+$(`#ens-${i}`).val()+'-'
                //
                }
            //
            cout=$(`#couts`).val()
            //
            var data = {
                element:element,
                ensemble:ensemble,
                matrix:matrix,
                cout:cout
                }
            console.log(data)
            $.ajax({
                //
                type:'POST',
                url:'/localisation',
                data:data,
                success:function(response){
                    document.write(response);
                }
                //
                })
          })
          //
        })