console.log('dashboard working')
let mainbody = document.querySelector('.mainbody')
// .navshow

outarrow.addEventListener('click', () => {
    mainbody.style.width= '90%'
    mainbody.style.marginLeft = '10%'
})

hidesidebar.addEventListener('click', () =>{
    mainbody.style.width= '100%'
    mainbody.style.marginLeft = '0%'
    
})

// MODAL EXTRANCE AND REMOVAL EFFECTS STARTS HERE
let registerdeviceformmodal = document.querySelector('.registerdeviceformmodal')
let registerstaff = document.querySelector('.registerstaff')
let closemodal = document.querySelector('.closemodal')
let shadow = document.querySelector('.shadow')

registerstaff.addEventListener('click', () => {
    registerdeviceformmodal.classList.add('registerdeviceformmodalShow')
    shadow.style.display = 'block'
    registerdeviceformmodal.style.display = 'block';
    
})

let closemodalsign = document.querySelector('.closemodalsign')
closemodalsign.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
})

closemodal.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
    scannetworkmmodal.style.display = 'none';
})

// MODAL EXTRANCE AND REMOVAL EFFECTS ENDS HERE

// MODAL FOR SCANNING NETWORK PROCEDURE STARTS HERE
let scanfordevices = document.querySelector('.scanfordevices')
let scannetworkmmodal = document.querySelector('.scannetworkmmodal')

scanfordevices.addEventListener('click', () => {
    scannetworkmmodal.classList.add('scannetworkmmodalShow')
    shadow.style.display = 'block'
    scannetworkmmodal.style.display = 'block';
})

let closemodalsignforscannet = document.querySelector('.closemodalsignforscannet')
closemodalsignforscannet.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
    scannetworkmmodal.style.display = 'none';
})

let closemodalforscannet = document.querySelector('.closemodalforscannet')
closemodalforscannet.addEventListener('click', () => {
    shadow.style.display = 'none'
    registerdeviceformmodal.style.display = 'none';
    scannetworkmmodal.style.display = 'none';
})

// MODAL FOR SCANNING NETWORK PROCEDURE ENDS HERE

// CAL DEVICE DEPRECIATION RATE STARTS HERE
// let depreciationrate = document.querySelector('.depreciationrate')
// let depreRate2;
// if (depreciationrate === 1){
//     depreRate2 = '75%';
// }
// else if (depreciationrate === 2){
//     depreRate2 = '50%';
// }
// else if (depreciationrate === 3){
//     depreRate2 = '25%'
// }
// else if (depreciationrate >= 4){
//     depreRate2 = '0%'
// }
// depreciationrate.innerHTML = depreRate2
// console.log(depreciationrate)
// CAL DEVICE DEPRECIATION RATE ENDS HERE



