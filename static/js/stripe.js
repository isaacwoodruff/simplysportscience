let elements = stripe.elements();

$('document').ready(function () {
    stripe.redirectToCheckout({
        sessionId: sessionId
    });
});