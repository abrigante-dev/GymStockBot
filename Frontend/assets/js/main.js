// var apigClient = apigClientFactory.newClient();

var User = {'UserName': '','Email': '','Phone': '','NotificationFrequency': 0};


function populateInStock(result){
    var answer = "";
    result.forEach(element => answer += element);
    answer = answer.replace("<table>", '<table class="InStockTable">');
    answer = answer.replace("<th></th>", '<th>In-Stock Products</th>');
    return answer;
}

function populateAllStock(result){
    var answer = "";
    result.forEach(element => answer += element);
    answer = answer.replace("<table>", '<table class="AllStockTable">');
    answer = answer.replace("<th></th>", '<th>All Products</th>');
    return answer;
}

var callAPI = (SearchKey, SearchType)=>{
    // In Stock Products
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({"SearchType": SearchType, "SearchKey": SearchKey, "SearchScope": "InStock", "UserName": User.UserName});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
   fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/getstock/", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('InStock').innerHTML = populateInStock(JSON.parse(result)))
    .catch(error => console.log('error', error));


    // All Stock
    var raw = JSON.stringify({"SearchType": SearchType, "SearchKey": SearchKey, "SearchScope": "", "UserName": User.UserName});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
   fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/getstock/", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('AllStock').innerHTML = populateAllStock(JSON.parse(result)))
    .catch(error => console.log('error', error));

}

function populateTypes(result){
    var types = "";
    var answer = JSON.parse(result);
    answer = answer.replace("[","");
    answer = answer.replace("]","");
    answer = answer.replaceAll("},","}},");
    answer = answer.split("},");
    for(var index = 0; index < answer.length; index++){
        var element = JSON.parse(answer[index]);
        types += `<input class="Type" type="image" src="` + element.URL + `" onclick="callAPI('` + element.Type + `', 'Type')" />`;
    }
    return types;
}

function loadTypes(){
    answer = "";
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify({"list":"Type"}),
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
    fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/getlist/", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('Categories').innerHTML = populateTypes(result))
    .catch(error => console.log('error', error));
}

function populateManufacturers(result){
    var manufacturers = "";
    var answer = JSON.parse(result);
    answer = answer.replace("[","");
    answer = answer.replace("]","");
    answer = answer.replaceAll("},","}},");
    answer = answer.split("},");
    for(var index = 0; index < answer.length; index++){
        var element = JSON.parse(answer[index]);
        manufacturers += `<input class="Manufacturer" type="image" src="` + element.URL + `" onclick="callAPI('` + element.Manufacturer + `', 'Manufacturer')" />`;
    }
    return manufacturers;
}

function loadManufacturers(){
    answer = "";
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify({"list":"Manufacturer"}),
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
    fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/getlist/", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('Manufacturers').innerHTML = populateManufacturers(result))
    .catch(error => console.log('error', error));
}


$(document).ready(function() {
    loadTypes();
    loadManufacturers();
});

