function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}// Verify the inputs

const verifyInputs = (username, email, message)=>{
    let valid = true
    
    if(username.length<1){
        valid = false
        
        document.getElementById('name-error').innerText = 'This is a required field.'
    }
    if(!validateEmail(email)){
        valid=false
        document.getElementById('email-error').innerText = 'Please enter a valid email address'
    }
    if(email.length<1){
        valid = false
        document.getElementById('email-error').innerText = 'This is a required field.'
    }
    if(message.length<1){
        valid = false
        document.getElementById('message-error').innerText = 'This is a required field.'
    }
    
    return valid
}

const send_mail = (username, email, message)=>{
    console.log(username,email,message)
    let data = {
        'name': username,
        'email': email,
        'message':message
    }

    fetch('/send_mail', {method:'POST', body:JSON.stringify(data)})
    .then(response=>console.log(response))
}


form = document.getElementsByTagName('form')[0]
form.addEventListener('submit',(e)=>{
    e.preventDefault()
    let username = document.getElementById('name')
    let email = document.getElementById('email')
    let message = document.getElementById('message')

    let formInputCheck = verifyInputs(username.value, email.value, message.value)
    if(formInputCheck){
        send_mail(username.value, email.value, message.value)
        document.getElementById('name').value = ''
        document.getElementById('email').value = ''
        document.getElementById('message').value = ''
    }
})



