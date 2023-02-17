// BODY REDUCTION ON EXPANDING OF SIDEBAR EFFECT STARTS HERE
console.log('registerdevice js working')
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
let laptop = document.querySelector('.laptop')
let desktop = document.querySelector('.desktop')
let closemodal = document.querySelector('.closemodal')
let shadow = document.querySelector('.shadow')
let devicetypehere = document.querySelector('.devicetypehere span')
let typeofdevicevalue = document.querySelector('#typeofdevicevalue')

laptop.addEventListener('click', () => {
    devicetypehere.innerHTML = 'Laptop'
    typeofdevicevalue.value = 'Laptop';
    registerdeviceformmodal.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    registerdeviceformmodal.style.display = 'block';

})

let closemodalsign = document.querySelector('.closemodalsign')
closemodalsign.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
})

desktop.addEventListener('click', () => {
    devicetypehere.innerHTML = 'Desktop'
    typeofdevicevalue.value = 'Desktop';
    registerdeviceformmodal.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    registerdeviceformmodal.style.display = 'block';

})

closemodal.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
})

// MODAL EXTRANCE AND REMOVAL EFFECTS ENDS HERE