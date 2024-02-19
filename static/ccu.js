function initCCU(app_id, element_id){
    console.log("Concurrent Users API by Reuben Schiopu Initialized! GitHub: https://github.com/MangoCoder360/ccu-api");

    var uniqueUserID = Math.floor(Math.random() * 10000000000000000);
    uniqueUserID = uniqueUserID.toString();

    setInterval(() => {
        fetch('https://ccu-api.reuben.zip/api/'+app_id+'/'+uniqueUserID).then(response => response.json()).then(data => {
            document.getElementById(element_id).innerHTML = data.ccu;
        });
    }, 2000);
}