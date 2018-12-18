$.ajaxSetup({
                beforeSend:function (xhr,settings) {
                    xhr.setRequestHeader('X-CSRFtoken',$.cookie('csrftoken'));

                }
            });
$('#book_event').click(function () {
        $('.book').removeClass("hide");
        $('.user').addClass("hide");

    });
    $('#user_event').click(function () {
        $('.book').addClass("hide");
        $('.user').removeClass("hide");

    });
    $('#list_1').click(function () {
        console.log('1');
        $('#2').addClass('hide');
        $('#3').addClass('hide');
        $('#4').addClass('hide');
        $('#1').removeClass("hide");
    });
    $('#list_2').click(function () {
        console.log('2');
        $('#1').addClass('hide');
        $('#4').addClass('hide');
        $('#3').addClass('hide');
        $('#2').removeClass("hide");
    });
    $('#list_3').click(function () {
        console.log('2');
        $('#1').addClass('hide');
        $('#2').addClass('hide');
        $('#4').addClass('hide');
        $('#3').removeClass("hide");
    });
    $('#list_4').click(function () {
        console.log('2');
        $('#1').addClass('hide');
        $('#2').addClass('hide');
        $('#3').addClass('hide');
        $('#4').removeClass("hide");
    });
    $(function () {
        $('#find').click(function () {
            $.ajax({
                url:'/manage',
                type:'get',
                data:{"book_name":$('#book_name').val(),
                      },
                success:function (data) {
                    // var obj = JSON.parse(data);
                    // $('#book_success').html(data)
                    $('#book_success').html(data)
                }
            });
        })
    });
    $(function () {
        $('#find_user').click(function () {
            $.ajax({
                url:'/manage',
                type:'get',
                data:{"username":$('#username').val(),
                      },
                success:function (data) {
                    console.log(data)
                    $('#user_success').html(data)
                }
            });
        })
    });