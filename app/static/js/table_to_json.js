
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
    console.log($rows);
    // Let's put this in the object like you want and convert to JSON (Note: jQuery will also do this for you on the Ajax request)
    var myObj = {};
    myObj.myrows = myRows;
    console.log(JSON.stringify(myObj));
};