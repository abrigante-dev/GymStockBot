// var apigClient = apigClientFactory.newClient();

var User = {'UserName': '','Email': '','Phone': '','NotificationFrequency': 0};

var lastSearch = {"SearchType": "", "SearchKey": ""};

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function populateInStock(result){
    var answer = "";
    result.forEach(element => answer += element);
    answer = answer.replace("<table>", '<table class="InStockTable">');
    if(answer.indexOf("<td>") > 0){
        answer = answer.replace("<th></th>", '<th>In-Stock Products (ordered by popularity)</th>');
    } else {
        answer = answer.replace("<th></th>", '<th>There are no such items currently in-stock.<BR>Subscribe to get them first!</th>');
    }
    return answer;
}

function populateAllStock(result){
    var answer = "";
    result.forEach(element => answer += element);
    answer = answer.replace("<table>", '<table class="AllStockTable">');
    answer = answer.replace("<th></th>", '<th>All Products (ordered by popularity)</th>');
    return answer;
}

var callAPI = (SearchKey, SearchType, Delay)=>{
    // Save search for refreshing
    lastSearch = {"SearchType": SearchType, "SearchKey": SearchKey};
    
    document.getElementById('InStock').innerHTML = "";
    document.getElementById('AllStock').innerHTML = "";
    //console.log(JSON.stringify(lastSearch));
    
    if(Delay) {sleep(2000);}
    
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

function submitUser(){
    if (document.getElementById('UserName').value == "") {
        alert("You must enter a User Name to keep track of your choises!");
        return;
    } 
    
    if (document.getElementById('Email').value == "" && document.getElementById('Phone').value == "") {
        alert("Please enter an email address or phone number to be notified!");
        return;
    }
    
    User = {'UserName': document.getElementById('UserName').value,
            'Email': document.getElementById('Email').value,
            'Phone': document.getElementById('Phone').value,
            'NotificationFrequency': $('input[name=frequency]:checked').val()
            };

    document.getElementById('Subscribe').innerHTML = "<h3>We received your information.<BR>Just click on a Subscribe button to get<BR>notified when that product gets in stock.<BR>If you'd like to modify your information</h3><input type='submit' class='subscribeButton' onclick='showSubscribe()' value='Click here'>";
    
    if(lastSearch.SearchType != "") {callAPI(lastSearch.SearchKey, lastSearch.SearchType, false);}
}

function showSubscribe(){
    User = {'UserName': '','Email': '','Phone': '','NotificationFrequency': '0'};

    var answer = "";
    answer = "<h3>Please enter your information:</h3>";
    answer += "<table class='SubscribeTable'>";
    answer += "<tr><td>User Name</td><td><input id='UserName' class='userInput' type='text'></td></tr>";
    answer += "<tr><td>Phone Number</td><td><input id='Phone' class='userInput' type='text'></td></tr>";
    answer += "<tr><td>Email address</td><td><input id='Email' class='userInput' type='text'></td></tr>";
    answer += "<tr><td>Notify me</td><td>"
    answer += "<input type='radio' id='once' name='frequency' checked value='0'><label class='notifyLabel' for='once'>Once</label><br>"
    answer += "<input type='radio' id='hourly' name='frequency' value='1'><label class='notifyLabel' for='hourly'>Hourly</label><br>"
    answer += "<input type='radio' id='daily' name='frequency' value='24'><label class='notifyLabel' for='daily'>Daily</label><br>"
    answer += "<input type='radio' id='weekly' name='frequency' value='168'><label class='notifyLabel' for='weekly'>Weekly</label><br>"
    answer += "</td></tr>";
    answer += "<tr><td><input type='submit' class='subscribeButton' onclick='loadSubscribe()' value='Cancel'></td><td class='subscribeTd'><input type='submit' class='subscribeButton' onclick='submitUser()' value='Submit'></td></tr>";
    answer += "</table>";

    document.getElementById('Subscribe').innerHTML = answer;
}

function loadSubscribe() {
    if(User.UserName == "") {
        document.getElementById('Subscribe').innerHTML = "<h3>If you'd like to subscribe and be notified when a product becomes available</h3><input type='submit' class='subscribeButton' onclick='showSubscribe()' value='Click here'>";
        if(lastSearch.SearchType != "") {callAPI(lastSearch.SearchKey, lastSearch.SearchType, false);} 
    }
}

function productSubscribe(productID) {
    // Subscribe
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");    
    var current_time = (new Date().toISOString()).toString();
    current_time = current_time.replace("T", " ");
    current_time = current_time.substr(0, 19);
    var raw = JSON.stringify({"Subscribe": "True", "UserName": User.UserName, "ProductID": productID, "Email": User.Email, "Phone": User.Phone, "Frequency": User.NotificationFrequency, "Time": current_time});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    
    // make API call with parameters and use promises to get response
   fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/subscribe/", requestOptions)
    .then(response => response.text())
    .then(result => console.log('result', result))
    .catch(error => console.log('error', error));    

    if(lastSearch.SearchType != "") {callAPI(lastSearch.SearchKey, lastSearch.SearchType, true);}
}

function productUnsubscribe(productID) {
    // Unsubscribe
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");    
    var raw = JSON.stringify({"Subscribe": "False", "UserName": User.UserName, "ProductID": productID});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    
    // make API call with parameters and use promises to get response
   fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/subscribe/", requestOptions)
    .then(response => response.text())
    .then(result => console.log('result', result))
    .catch(error => console.log('error', error));    

    if(lastSearch.SearchType != "") {callAPI(lastSearch.SearchKey, lastSearch.SearchType, true);}    
}

$(document).ready(function() {
    loadTypes();
    loadManufacturers();
    loadSubscribe();
});

