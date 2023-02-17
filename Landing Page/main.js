let noexpandeffect = document.querySelector('.noexpandeffect')
let noexpandeffect2 = document.querySelector('.noexpandeffect2')
let noexpandeffect3 = document.querySelector('.noexpandeffect3')
let midbox1 = document.querySelector('.midbox1')
let midbox2 = document.querySelector('.midbox2')
let midbox3 = document.querySelector('.midbox3')
let p1 = document.querySelector('.midbox1 p')
let p2 = document.querySelector('.midbox2 p')
let p3 = document.querySelector('.midbox3 p')

// MIDBOX ONE EFFECT STARTS HERE
midbox1.addEventListener('mouseenter', function () {
    noexpandeffect.classList.add('expandeffect')
    p1.style.display = 'block'
})
midbox1.addEventListener('mouseleave', function () {
    noexpandeffect.classList.remove('expandeffect')
    p1.style.display = 'none'
})
// MIDBOX ONE EFFECT ENDS HERE


// MIDBOX TWO EFFECT ENDS HERE
midbox2.addEventListener('mouseenter', function () {
    noexpandeffect2.classList.add('expandeffect2')
    p2.style.display = 'block'
})
midbox2.addEventListener('mouseleave', function () {
    noexpandeffect2.classList.remove('expandeffect2')
    p2.style.display = 'none'
})
// MIDBOX TWO EFFECT ENDS HERE


// MIDBOX THREE EFFECT STARTS HERE
midbox3.addEventListener('mouseenter', function () {
    noexpandeffect3.classList.add('expandeffect')
    p3.style.display = 'block'
})
midbox3.addEventListener('mouseleave', function () {
    noexpandeffect3.classList.remove('expandeffect')
    p3.style.display = 'none'
})
// MIDBOX THREE EFFECT ENDS HERE

// HAMBURGER SECTION
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

//  ! For The Navigation Bar

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
});

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  })
);
