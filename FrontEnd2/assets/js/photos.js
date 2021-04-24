$(document).ready(function() {

});
/*
function getBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            let encoded = reader.result.replace(/^data:(.*;base64,)?/, '');
            if ((encoded.length % 4) > 0) {
                encoded += '='.repeat(4 - (encoded.length % 4));
            }
            resolve(encoded);
        };
        reader.onerror = error => reject(error);
    });
}

function upload() {
    var files = document.getElementById("myPath").files;
    if (!files.length) {
        return alert("Please choose a file to upload first.");
    }
    var file = files[0];
    const reader = new FileReader();

    var file_data;
    var labels = document.getElementById("customLabels").value;

    var encoded_image = getBase64(file).then(
        data => {
            console.log(data)
            var apigClient = apigClientFactory.newClient({
                apiKey: 'e0vtIuAt6c2f1aIY1UGj38nugkq8BzXe413pdqPb'
            });
            var file_type = file.type + ";base64"
            var body = data;
            var params = {'Content-Type' : file.type, 'x-amz-meta-customLabels' : labels, 'objectKey' : file.name, "x-api-key" : 'e0vtIuAt6c2f1aIY1UGj38nugkq8BzXe413pdqPb'};
            var additionalParams = {};
            apigClient.uploadPut(params, body , additionalParams).then(function(response){
                if (response.status == 200)
                    document.getElementById("uploadAnswer").innerHTML = "Uploaded";
            })
        }
    );
}
*/

function search() {
    if (!document.getElementById("transcript").value) {
        $(".searchAnswer").append(`<p style="padding-top: 10px;">No images match these terms. Please ask for some type of image.</p>`);
        return;
    }        
    
    var apigClient = apigClientFactory.newClient({
        apiKey: "e0vtIuAt6c2f1aIY1UGj38nugkq8BzXe413pdqPb"
    });

    $(".images").empty('');
    $(".searchAnswer").empty('');
    apigClient.searchGet({'q': document.getElementById('transcript').value }, {}).then((result) => {
        console.log(result);        
        if(result.data.indexOf("Sorry") == 0 || result.data.length == 0) {
            $(".searchAnswer").append(`<p style="padding-top: 10px;">No images match these terms.</p>`);
            $(".searchAnswer").append(`<p style="padding-top: 10px;">${result['data']}</p>`);
        } else {
            document.getElementById('transcript').value = "";
            result['data'].forEach((element) => {
                $(".images").append(`
                    <img src='https://ccbda2-photos-b2.s3.amazonaws.com/${element}' class='image'>
                `);
            });
        }
    }).catch(function(x){});
}



function httpReq(method, url, data, successCB, errorCB) {
    var xhr = new XMLHttpRequest();
    xhr.addEventListener('load', function () {
        $(".uploadAnswer").empty('');
        if (xhr.status == 200) {
            successCB(xhr.response);            
            $(".uploadAnswer").append(`<p style="padding-top: 10px;">Image Uploaded!</p>`);
        } else {
            errorCB({status: xhr.status, response: xhr.response});
            $(".uploadAnswer").append(`<p style="padding-top: 10px;">Failed to upload!</p>`);
        }
    });

    xhr.open(method, url, true);
    // give access to bucket owner full control
    xhr.setRequestHeader("x-amz-acl", "bucket-owner-full-control");
    xhr.setRequestHeader("x-amz-meta-customLabels", document.getElementById('customLabels').value);
    
    console.log(data);
    
    xhr.send(data);
}

function uploadPhoto3() {
    var files = document.getElementById("myPath").files;
    if (!files.length) {
        return alert("Please choose a file to upload first.");
    }
    var file = files[0];
    var fileName = file.name;
    console.log(file.name);    
    httpReq('PUT', 'https://ccbda2-photos-b2.s3.amazonaws.com/' + fileName.toString(), file, function (response) {
        console.log('Upload Successful', response);
        document.getElementById("customLabels").value = "";
        document.getElementById("myPath").value = "";
        
    }, function (error) {
        console.error(error);
    });
}
