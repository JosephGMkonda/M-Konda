const usernameField = document.querySelector("#usernameField")
const feedbackField = document.querySelector(".invalid-feedback")
const showPasswordToggle = document.querySelector(".showPasswordToggle")
const passwordField = document.querySelector("#passwordField")
const submitBtn = document.queryCommandValue(".submit-btn")


const handleToggleInput = (e) => {
    if(showPasswordToggle.textContent==="SHOW"){
        showPasswordToggle.textContent="HIDE"
        passwordField.setAttribute("type","password")
    }else{
        showPasswordToggle.textContent="SHOW"
        passwordField.setAttribute("type","text")

    }
}



showPasswordToggle.addEventListener("click",handleToggleInput)



usernameField.addEventListener("keyup", (e) => {
    
    const usernameVal = e.target.value;
    usernameField.classList.remove("is-invalid");
    feedbackField.style.display="none"

    if(usernameVal.length>0){
        fetch('/authentication/username_validation',{
            body:JSON.stringify({username:usernameVal}),
            method:"POST"
        })
        .then((res)=>res.json())
        .then(data => {
            console.log(data)
            if(data.username_error){
                submitBtn.disabled=true
                usernameField.classList.add("is-invalid");
                feedbackField.style.display="block"
       
                feedbackField.innerHTML=`<p>${data.username_error}</P>`
            }else{
                submitBtn.removeAttribute('disabled')
            }
        })

    }
})