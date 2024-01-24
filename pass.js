function generatePassword() {
    const length = document.getElementById("length").value;
    const useLetters = document.getElementById("letters").checked;
    const useNumbers = document.getElementById("numbers").checked;
    const useSymbols = document.getElementById("symbols").checked;

    const characters = (
        (useLetters ? 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' : '') +
        (useNumbers ? '0123456789' : '') +
        (useSymbols ? '!@#$%^&*()_+[]{}|;:,.<>?/~`' : '')
    );

    if (!characters) {
        alert("Error: You must choose at least one character type.");
        return;
    }else if(length==="" || length>=15){
        alert("Please Give The Proper Length of Password!");
        return;
    }


    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters.charAt(randomIndex);
        
    }

    let passwordOutput=document.getElementById("password-output");
    passwordOutput.textContent = "Generated Password=> " + password;
    passwordOutput.classList.add("password-output");

}
 