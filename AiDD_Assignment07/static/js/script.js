(function initMobileNav() {
  const navToggle = document.getElementById("navToggle");
  const navList = document.getElementById("primaryNav");

  if (!navToggle || !navList) return;

  function closeNav() {
    navToggle.setAttribute("aria-expanded", "false");
    navList.classList.remove("is-open");
  }

  navToggle.addEventListener("click", () => {
    const isExpanded = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isExpanded));
    navList.classList.toggle("is-open", !isExpanded);
  });

  document.addEventListener("click", (event) => {
    if (!navToggle.contains(event.target) && !navList.contains(event.target)) {
      closeNav();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeNav();
    }
  });
})();

(function initReveal() {
  const revealItems = document.querySelectorAll("[data-reveal]");

  if (!revealItems.length) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reducedMotion.matches || !("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  function playReveal(item) {
    if (item.classList.contains("is-visible")) return;

    item.classList.add("is-visible");
    item.animate(
      [
        { opacity: 0.58, transform: "translateY(18px)" },
        { opacity: 1, transform: "translateY(0)" },
      ],
      {
        duration: 520,
        easing: "cubic-bezier(0.2, 0.8, 0.2, 1)",
        fill: "both",
      }
    );
  }

  revealItems.forEach((item) => {
    const rect = item.getBoundingClientRect();
    if (rect.top <= window.innerHeight * 0.92) {
      playReveal(item);
    }
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          playReveal(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: "0px 0px -24px 0px",
    }
  );

  revealItems.forEach((item) => {
    if (!item.classList.contains("is-visible")) {
      observer.observe(item);
    }
  });
})();
