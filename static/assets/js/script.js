var typed = new Typed('.typed', {
    strings: ["Designer", "Developer", "Freelancer", "Photographer"],
    typeSpeed: 100,
    backSpeed: 50,
    loop: true
});

document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('section');
  const navLi = document.querySelectorAll('nav ul li a');

  window.addEventListener('scroll', () => {
      let current = '';
      
      sections.forEach(section => {
          const sectionTop = section.offsetTop;
          if (pageYOffset >= sectionTop - 60) {
              current = section.getAttribute('id');
          }
      });

      navLi.forEach(li => {
          li.classList.remove('active');
          if (li.getAttribute('href') === '#' + current) {
              li.classList.add('active');
          }
      });
  });
});