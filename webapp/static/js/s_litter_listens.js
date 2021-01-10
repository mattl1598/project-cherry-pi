var xmlhttp = new XMLHttpRequest();
var url = "https://larby.dev/listens/litterpicker";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
    var myArr = JSON.parse(this.responseText);
    myFunction(myArr);
    }
};

xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(arr) {
    var out = arr["listens"];
    document.getElementById("no_of_listens").innerHTML = out;
}