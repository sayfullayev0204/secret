window.addEventListener('DOMContentLoaded', function () {
    window.addEventListener('scroll', function() {
      const header = document.querySelector('header');
      header.classList.toggle('sticky', window.scrollY > 0)
    })
  
    const menuBtn = document.querySelector('.menu-btn')
    const navigation = document.querySelector('.navigation')
    const navigationItems = document.querySelectorAll('.navigation a')
  
    menuBtn.addEventListener('click', () => {
      menuBtn.classList.toggle('active')
      navigation.classList.toggle('active')
    })
  
    navigationItems.forEach(navItem => {
      navItem.addEventListener('click', () => {
        menuBtn.classList.remove('active')
        navigation.classList.remove('active')
      })
    })
  
    const scrollBtn = document.querySelector('.scrollToTop-btn')
    window.addEventListener('scroll', () => {
      scrollBtn.classList.toggle('active', window.scrollY > 500)
    })
    scrollBtn.addEventListener('click', () => {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    })
  
    window.addEventListener('scroll', () => {
      let reveals = document.querySelectorAll('.reveal')
  
      for(let i = 0; i< reveals.length; i++) {
        let windowHeight = window.innerHeight;
        let revealTop = reveals[i].getBoundingClientRect().top;
        let revealPoint = 50;
  
        if(revealTop < windowHeight - revealPoint) {
          reveals[i].classList.add('active')
        }
      }
    })
  })


// Login and register

const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});

// Login and register