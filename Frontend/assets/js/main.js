// var apigClient = apigClientFactory.newClient();

// define the callAPI function that takes a first name and last name as parameters
var callAPI = (searchLabels, searchType)=>{
    // instantiate a headers object
    var myHeaders = new Headers();
    // add content type header to object
    myHeaders.append("Content-Type", "application/json");
    // using built in JSON utility package turn object to string and store in a variable
    var raw = JSON.stringify({"searchLabels":searchLabels, "searchIndex": searchType});
    // create a JSON object with parameters for API call and store in a variable
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
   fetch("https://m2bf6kgtl6.execute-api.us-east-1.amazonaws.com/v1/getstock/", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('InStock').innerHTML = JSON.parse(result).body)
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
        types += `<input class="Type" type="image" src="` + element.URL + `" onclick="callAPI('` + element.Type + `', 'TYPE')" />`;        
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
/*
    console.log(response);
    console.log(answer);
    

    if(answer != "") {
        console.log(response);
    }
*/


    //document.getElementById('InStock').innerHTML =

    //document.getElementById('Categories').innerHTML = `<input type="image" src="./images/barbellbutton.png" onclick="callAPI('BARBELL', 'TYPE')"/><input type="image" src="./images/rackbutton.png" onclick="callAPI('RACK', 'TYPE')"/><input type="image" src="./images/benchbutton.png" onclick="callAPI('BENCH', 'TYPE')"/><input type="image" src="./images/platebutton.png" onclick="callAPI('PLATES', 'TYPE')"/>`;
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
    .then(result => answer = JSON.parse(result).body)
    .catch(error => console.log('error', error));

    if(answer != "") {
        console.log(response);
    }

//    //document.getElementById('Manufacturers').innerHTML = `<a href="./images/rogue.html"><img src="./images/roguebutton.png"></a><a href="./pages/rep.html"><img src="./images/repbutton.png"></a><a href="./pages/titan.html"><img src="./images/titanbutton.png"></a>`;
}

$(document).ready(function() {
    loadTypes();
    loadManufacturers();
});






/*

     <!-- <label>Type Company :</label> -->
     <!-- <input type="text" id="searchLabels"> -->
     <!-- <button type="button" onclick="callAPI(document.getElementById('searchLabels').value)">Search Stock</button> -->


    <!-- <button type="button" onclick="callAPI('ROGUE', 'COMPANY')">ROGUE</button> -->
*/

