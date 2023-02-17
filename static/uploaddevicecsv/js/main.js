// BODY REDUCTION ON EXPANDING OF SIDEBAR EFFECT STARTS HERE
let mainbody = document.querySelector('.mainsectionregister')
// .navshow

outarrow.addEventListener('click', () => {
    mainbody.style.width= '90%'
    mainbody.style.marginLeft = '10%'
})

hidesidebar.addEventListener('click', () =>{
    mainbody.style.width= '100%'
    mainbody.style.marginLeft = '0%'
    
})
// BODY REDUCTION ON EXPANDING OF SIDEBAR EFFECT ENDS HERE


// MODAL EXTRANCE AND REMOVAL EFFECTS STARTS HERE
let registerdeviceformmodal = document.querySelector('.registerdeviceformmodal')
let activateuploadform = document.querySelector('.activateuploadform')
let activateuploadform2 = document.querySelector('.activateuploadform2')
let closemodal = document.querySelector('.closemodal')
let shadow = document.querySelector('.shadow')
let devicetypehere = document.querySelector('.devicetypehere span')
let typeofdevicevalue = document.querySelector('#typeofdevicevalue')

activateuploadform.addEventListener('click', () => {
    registerdeviceformmodal.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    registerdeviceformmodal.style.display = 'block';

})
activateuploadform2.addEventListener('click', () => {
    registerdeviceformmodal.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    registerdeviceformmodal.style.display = 'block';

})

closemodal.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
})

// MODAL EXTRANCE AND REMOVAL EFFECTS ENDS HERE