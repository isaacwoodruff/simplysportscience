$(document).ready(function () {
    // breadcrumb for users to go back to their previous page when viewing a job post details
    $("#back-btn").click(function () {
        window.history.back();
    });

    function request_credit_score() {

        req = $.ajax({
            url: '/update',
        });

        req.done(function (data) {
            $('#credit-num').text(data.credit_amount);
        });

        setTimeout(request_credit_score(), 5000);
    };

    request_credit_score();
});
