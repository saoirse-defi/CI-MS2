const ethAddress = document.getElementById('ethAddress');

async function init(){
    window.web3 = await Moralis.Web3.enable();
}

async function login() {
    let user = Moralis.User.current();

    if (!user) {
        user = await Moralis.Web3.authenticate(); //prompts user to sign transcation with Metamask
    }

    getAddress(user);

    userAddress = user['attributes'].accounts[0]; //location of ethereum address within the ParseUser object
    
    ethAddress.innerText = userAddress; //displays address to the user
}

async function getAddress(user){
    if (user) {
        const query = new Moralis.Query("EthTransactions"); //create a new eth transactions query using Moralis
        query.equalTo("from_address", user.get("ethAddress")); 

        const results = await query.find(); //results of query
        console.log("user transactions:", results);
    }
}


document.getElementById("btn-login").onclick = login;