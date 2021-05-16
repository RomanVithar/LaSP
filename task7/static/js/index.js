/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
$('.test').next().hide();
var dropdown = $('.dropdown-btn');
/*dropdown.bind( 'click', function(){
  $(this).toggleClass('active');
  var dropdownContainer = $(this).next();
  dropdownContainer.slideToggle();
});*/
dropdown.click(function(){
  $(this).toggleClass('active');
  var dropdownContainer = $(this).next();
  dropdownContainer.slideToggle();
});