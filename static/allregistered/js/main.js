// BODY REDUCTION ON EXPANDING OF SIDEBAR EFFECT STARTS HERE
console.log('all registerdevice js working')
let mainbody = document.querySelector('.mainsectionallregistered')
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
let showdevicedetails = document.querySelector('.showdevicedetails')
let showDetails = document.querySelector('.showDetails')
let closemodal = document.querySelector('.closemodal')
let shadow = document.querySelector('.shadow')
let devicetypehere = document.querySelector('.devicetypehere span')
let typeofdevicevalue = document.querySelector('#typeofdevicevalue')

showDetails.addEventListener('click', () => {
    showdevicedetails.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    showdevicedetails.style.display = 'block';

})

let closemodalsign = document.querySelector('.closemodalsign')
closemodalsign.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
})

closemodal.addEventListener('click', () => {
    shadow.style.display = 'none'
    showdevicedetails.style.display = 'none';
})

// MODAL EXTRANCE AND REMOVAL EFFECTS ENDS HERE