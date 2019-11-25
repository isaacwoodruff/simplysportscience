$(document).ready(function() {
    $('#submit-payment-btn').click(function() {
        stripe.redirectToCheckout({
            sessionId: session_id
        });
    });
});
