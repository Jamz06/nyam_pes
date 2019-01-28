
function send_order() {

    console.log('Запуск функции');
    // Loop through grabbing everything
    var myRows = [];
    var $headers = $("th");
    var $rows = $("tbody tr").each(function(index) {
        $cells = $(this).find("td");
        myRows[index] = {};
        $cells.each(function(cellIndex) {
            myRows[index][$($headers[cellIndex]).html()] = $(this).html();
        });    
    });
    
    // Let's put this in the object like you want and convert to JSON (Note: jQuery will also do this for you on the Ajax request)
    var myObj = {};
    myObj.myrows = myRows;


    console.log(JSON.stringify(myObj));

    return muObj
};

function customer_data() {
    var client_name = document.getElementById('name');
    var email = document.getElementById('email');
    var phone = document.getElementById('phone');

    // Создать JSON
    var customer = {
        'name': client_name.value,
        'email': email.value,
        'phone': phone.value
        };
    return customer
};


function send_data(){

};


function show_contact_form() {
    var tek_form = document.getElementById('show_order');
    var next_form = document.getElementById('contact_div');
    console.log(next_form);
    tek_form.classList.add("hidden");
    
    next_form.removeAttribute("hidden");
    // Показать следующую форму
    send_order();
};