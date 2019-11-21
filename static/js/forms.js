$(document).ready(function(){
    $("#job-title").autocomplete({
        source: autocomplete_title_source,
        minLength: 1,
        delay: 100,
    });

    var placesAutocomplete = places({
        appId: ALGOLIA_PUBLIC_APP_ID,
        apiKey: ALGOLIA_PUBLIC_KEY,
        container: document.querySelector('#address-input')
    });
})