$(document).ready(function(){
    $('.post-form').click(function(){
        $.ajax({
            url:'add-post',
            type: 'get',
            dataType:'json',
            beforeSend: function(){
                $('#Post').modal('show');
            },
            success: function(data){
                $('#Post .modal-content').html(data.html_form);
            }
        })
    })
})