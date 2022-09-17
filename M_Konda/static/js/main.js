$(document).ready(function(){
    $('.show-form').click(function(){
        $.ajax({
            url:'add-post',
            type: 'get',
            dataType:'json',
            beforeSend: function(){
                $('#Post').modal('show');
            },
            success: function(data){
                $('#Post .modal-content').html(data.html_form);
                console.log("Hello Joseph")
            }
        })
    })

    $('#Post').on('submit','.Create-form',function(){
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data){
                if(data.form_is_valid){
                    console.log('data is saved')
                }else{
                    $('#Post .modal-content').html(data.html_form)
                }
            }

        })

        return false;
    })
})