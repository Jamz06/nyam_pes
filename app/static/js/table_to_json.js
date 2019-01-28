
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
    //myObj.myrows = myRows;


    //console.log(JSON.stringify(myObj));

    return myRows
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
    var customer = customer_data();
    var order_data = send_order();

    $.ajax({
        dataType: "json",
        type: "POST",
        async: true,
        contentType: "application/json",
        url: "/order",
        data: JSON.stringify({
            customer: customer,
            order_data: order_data
        }),
        beforeSend: function() {
            
        },
        success: function (data) {            
            
            console.log('JSON has come!');
        },
        error: function () {
            alert('Ой Что-то пошло не так, попробуйте позднее');
            console.log('Json has not come (');
        },
        complete: function () {
            console.log("Complete");
        }
    });
};


function show_contact_form() {
    var tek_form = document.getElementById('show_order');
    var next_form = document.getElementById('contact_div');
    
    var focus_field = document.getElementById('name');
    console.log(next_form);
    tek_form.classList.add("hidden");
    
    next_form.removeAttribute("hidden");
    
    window.scrollTo(0,document.body.scrollHeight);
    
    focus_field.focus();

    // Показать следующую форму
    send_order();
};