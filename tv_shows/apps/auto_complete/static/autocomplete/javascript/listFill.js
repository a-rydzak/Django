


// ----------------------------------------------------------------We want this to work but it returns html as the restonse.
// $('#starts_with').keyup(function() {
//     console.log('sending the following information', $('#myForm').serialize());
//         $.ajax({
//                  method: "POST",
//                  url: "/users/api",
//                  data: $('#myForm').serialize(),
//                  success: function(response) {
//                      console.log('received response:',  response);
//                      $('#placeholder').html(response)
//                  }
//               })
// });

// ----------------------------------------------------------------This currently works but it's messy
$.ajax({
        method: "POST",
        url: "/users/api/json2",
        data: $('#myForm').serialize()
    })
    .done(function(response) {
        var list = document.getElementById("demo")
        var i;
        $('#demo').empty();

        for (var i = 0; i <= response.users.length - 1; i++) {
            var x = document.getElementById("demo");
            var li = document.createElement("LI");
            li.innerHTML = response.users[i]['first_name']
            x.appendChild(li);
        }

    });
$('#starts_with').keyup(function() {
    $.ajax({
            method: "POST",
            url: "/users/api/json2",
            data: $('#myForm').serialize()
        })
        .done(function(response) {
            var list = document.getElementById("demo")
            var i;
            $('#demo').empty();

            for (var i = 0; i <= response.users.length - 1; i++) {
                var x = document.getElementById("demo");
                var li = document.createElement("LI");
                li.innerHTML = response.users[i]['first_name']
                x.appendChild(li);
            }

        });
});