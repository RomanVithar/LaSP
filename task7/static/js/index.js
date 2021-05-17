/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
$('.test').next().hide();
var dropdown = $('.dropdown-btn');
/*dropdown.bind( 'click', function(){
  $(this).toggleClass('active');
  var dropdownContainer = $(this).next();
  dropdownContainer.slideToggle();
});*/
dropdown.click(function () {
  $(this).toggleClass('active');
  var dropdownContainer = $(this).next();
  dropdownContainer.slideToggle();
});

// обработка главной формы
function ds(f, current, current_table) {
  var e = document.getElementById(f);
  if (!e) return false;
  // Создать временную форму 
  var tmp_form = document.createElement("form");
  tmp_form.method = 'POST';
  if (current_table == '') {
    if (f == 'delete') {
      tmp_form.action = '/delete_base'; // Адрес скрипта-обработчика формы 
    } else {
      tmp_form.action = '/get_tables'; // Адрес скрипта-обработчика формы 
    }
  } else {
    tmp_form.action = '/show_table'; // Адрес скрипта-обработчика формы 
  }
  tmp_form.style.display = 'none';
  document.getElementsByTagName('body')[0].appendChild(tmp_form);

  // определить какой врапер и в зависимости от этого добавить нужную таблицу или базу
  if (f == 'wrapper1') {
    var tmp_el = document.createElement("input");
    tmp_el.name = 'btnGetTables';
    tmp_el.type = 'hidden';
    tmp_el.value = current;
    tmp_form.appendChild(tmp_el);
  } else if (f == 'delete') {
    var tmp_el = document.createElement("input");
    tmp_el.name = 'base';
    tmp_el.type = 'hidden';
    tmp_el.value = current;
    tmp_form.appendChild(tmp_el);
  } else {
    var tmp_el = document.createElement("input");
    tmp_el.name = 'btnGetTables';
    tmp_el.type = 'hidden';
    tmp_el.value = current;
    tmp_form.appendChild(tmp_el);
    var tmp_el2 = document.createElement("input");
    tmp_el2.name = 'submitTable';
    tmp_el2.type = 'hidden';
    tmp_el2.value = current_table;
    tmp_form.appendChild(tmp_el2);
  }
  // Отправить созданную форму 
  tmp_form.submit();
}