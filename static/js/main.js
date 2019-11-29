$(document).ready(function () {

    // breadcrumb for users to go back to their previous page when viewing a job post details
    $("#back-btn").click(function () {
        window.history.back();
    });

    // AJAX request to the database every 5 seconds to see if the credit has been updated
    // Displays to the user that their credit has been updated
    function request_credit_score() {

        $.ajax({
            url: credit_amount_url
        }).done(function (data) {
            $('#credit-num').text(data.credit_amount);
            setTimeout(function(){
                request_credit_score();
            }, 5000);
        });

    };

    request_credit_score();
});
