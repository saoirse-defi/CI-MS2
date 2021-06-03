const ethAddress = document.getElementById('ethAddress');
let user;
let userAddress;

Moralis.initialize("ODLoFKUVQy2afCMmNL784vXb2DgVvjxntguF4x3c");
Moralis.serverURL = "https://btjfheuh8ncx.moralis.io:2053/server";

async function init(){
    window.web3 = await Moralis.Web3.enable();
    login();
}

async function login(){
    try{
        user = Moralis.User.current();
        if (!user) {
            user = await Moralis.Web3.authenticate(); //prompts user to sign transcation with Metamask
        }
        getAddress(user);

        userAddress = user['attributes'].accounts[0]; //location of ethereum address within the ParseUser object
    
        ethAddress.innerText = userAddress; //displays address to the user

        document.getElementById("btn-login").style.display = "none";

        console.log("Button Pressed!");
    }catch(error){
        console.log(error)
    }
}

/*async function login() {
    
    if (!user) {
        user = await Moralis.Web3.authenticate(); //prompts user to sign transcation with Metamask
    }

    getAddress(user);

    userAddress = user['attributes'].accounts[0]; //location of ethereum address within the ParseUser object
    
    ethAddress.innerText = userAddress; //displays address to the user

    document.getElementById("btn-login").style.display = "none";

    console.log("Button Pressed!");
}*/

 async function getAddress(user){
    if (user) {
        const query = new Moralis.Query("EthTransactions"); //create a new eth transactions query using Moralis
        query.equalTo("from_address", user.get("ethAddress")); 
        console.log(query);

        const results = await query.find(); //results of query
        console.log("user transactions:", results);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    init();
    $('#ethTable').DataTable({
        searching: false,
        ordering: false
    });
    $('td').tooltip(); //bootstrap tooltip 
});

document.getElementById("btn-login").onclick = login();