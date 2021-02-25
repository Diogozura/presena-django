$(document).ready(function() {
    var baseUrl = 'http://192.168.0.106/';
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter     = $('#filter');
});
    $(searchbtn).on ('click', function() {
    searchForm.submit();

    $(filter).change(function() {
        var filter = $(this).val(); 
        window.location.href = baseUrl + '?filter=' + filter;
    });
});