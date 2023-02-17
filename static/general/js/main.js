console.log('working')
let nav = document.querySelector('.nav')
let outarrow = document.querySelector('.outsidebar')
let navimages = document.querySelector('.navimages')
let navlogo = document.querySelector('.navlogo')
let outsidebar = document.querySelector('.outsidebar')
let navlogout = document.querySelector('.navlogout')
let topbar = document.querySelector('.topbar')
// let mainbody = document.querySelector('.onboardbox')
// mainbody.style.display = 'none'
//
let main = document.querySelector('.main')
let hidesidebar = document.querySelector('.hidearrow')
// .navshow

outarrow.addEventListener('click', () => {
    navimages.style.display = 'none'
    outsidebar.style.display = 'none'
    navlogo.style.display = 'none'
    navlogout.style.display = 'none'
    nav.classList.toggle('navhide')
    // topbar.style.display = 'none'
    topbar.style.marginLeft = '15%'
    topbar.style.width = '85%'
    // 
    main.classList.toggle('navshow')
    main.style.display = 'block'
})

hidesidebar.addEventListener('click', () =>{
    navimages.style.display = 'block'
    outsidebar.style.display = 'block'
    navlogo.style.display = 'block'
    navlogout.style.display = 'block'
    nav.classList.toggle('navhide')
    topbar.style.marginLeft = '5%'
    topbar.style.width = '95%'
    // 
    main.classList.toggle('navshow')
    setTimeout(() => {
        main.style.display = 'none'
    }, 00)
})

// MODILE TOP BAR DISPLAYA ND HIDE SETUP

let downarrow = document.querySelector('.downarrow')
let uparrow = document.querySelector('.uparrow')
let searchandtools = document.querySelector('.searchandtools')

downarrow.addEventListener('click', () => {
    topbar.style.height = '200px'
    downarrow.style.display='none'
    uparrow.style.display='block'
    setTimeout(() => {
        searchandtools.style.display = 'block'
    }, 500)
})
uparrow.addEventListener('click', () => {
    topbar.style.height = '60px'
    downarrow.style.display='block'
    uparrow.style.display='none'
    setTimeout(() => {
        searchandtools.style.display = 'none'
    }, 0)
})