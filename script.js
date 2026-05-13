const header = document.querySelector("[data-header]");
const nav = document.querySelector("[data-nav]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navLinks = [...document.querySelectorAll(".site-nav a")];
const filterButtons = [...document.querySelectorAll("[data-filter]")];
const projectCards = [...document.querySelectorAll(".project-card")];
const lightbox = document.querySelector("[data-lightbox]");
const lightboxImage = document.querySelector("[data-lightbox-image]");
const lightboxTitle = document.querySelector("[data-lightbox-title]");
const lightboxClose = document.querySelector("[data-lightbox-close]");
const stepButtons = [...document.querySelectorAll("[data-step]")];
const stepPanel = document.querySelector("[data-step-panel]");
const estimateForm = document.querySelector("[data-estimate-form]");
const formStatus = document.querySelector("[data-form-status]");

const processCopy = {
  1: {
    title: "Start with the room, goals, timing, and budget.",
    body:
      "Share the project basics and schedule a free estimate. The first conversation sets expectations around feasibility, trade coordination, and next steps.",
  },
  2: {
    title: "Turn the idea into a clear scope of work.",
    body:
      "The project is broken into materials, sequence, access, protection, and the finish details that matter before work begins.",
  },
  3: {
    title: "Keep the jobsite moving with steady communication.",
    body:
      "The crew handles demolition, construction, carpentry, tile, fixtures, and finish work while keeping the homeowner informed.",
  },
  4: {
    title: "Walk the finished work and close the details.",
    body:
      "Final touchups, cleanup, and punch-list items are reviewed so the completed space is ready for daily use.",
  },
};

function setHeaderState() {
  header.classList.toggle("scrolled", window.scrollY > 24);
}

function closeNav() {
  nav.classList.remove("open");
  navToggle.setAttribute("aria-expanded", "false");
  document.body.classList.remove("nav-open");
}

function openLightbox(card) {
  lightboxImage.src = card.dataset.image;
  lightboxImage.alt = card.querySelector("img").alt;
  lightboxTitle.textContent = card.dataset.title;
  lightbox.classList.add("open");
  lightbox.setAttribute("aria-hidden", "false");
  document.body.classList.add("lightbox-open");
  lightboxClose.focus();
}

function closeLightbox() {
  lightbox.classList.remove("open");
  lightbox.setAttribute("aria-hidden", "true");
  document.body.classList.remove("lightbox-open");
  lightboxImage.src = "";
}

function setActiveNav() {
  const offset = window.innerHeight * 0.35;
  const current = navLinks
    .map((link) => {
      const section = document.querySelector(link.getAttribute("href"));
      return section ? { link, top: section.getBoundingClientRect().top } : null;
    })
    .filter(Boolean)
    .reverse()
    .find((item) => item.top <= offset);

  navLinks.forEach((link) => link.classList.toggle("active", current?.link === link));
}

setHeaderState();
setActiveNav();

window.addEventListener("scroll", () => {
  setHeaderState();
  setActiveNav();
});

navToggle.addEventListener("click", () => {
  const isOpen = nav.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
  document.body.classList.toggle("nav-open", isOpen);
});

navLinks.forEach((link) => {
  link.addEventListener("click", closeNav);
});

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;

    filterButtons.forEach((item) => item.classList.toggle("active", item === button));
    projectCards.forEach((card) => {
      card.hidden = filter !== "all" && card.dataset.category !== filter;
    });
  });
});

projectCards.forEach((card) => {
  card.addEventListener("click", () => openLightbox(card));
});

lightboxClose.addEventListener("click", closeLightbox);

lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) {
    closeLightbox();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeNav();
    if (lightbox.classList.contains("open")) {
      closeLightbox();
    }
  }
});

stepButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const step = button.dataset.step;
    const copy = processCopy[step];

    stepButtons.forEach((item) => item.classList.toggle("active", item === button));
    stepPanel.innerHTML = `<h3>${copy.title}</h3><p>${copy.body}</p>`;
  });
});

estimateForm.addEventListener("submit", (event) => {
  event.preventDefault();

  if (!estimateForm.checkValidity()) {
    estimateForm.reportValidity();
    return;
  }

  const formData = new FormData(estimateForm);
  const name = formData.get("name").trim();
  const phone = formData.get("phone").trim();
  const project = formData.get("project");
  const details = formData.get("details").trim();
  const subject = encodeURIComponent(`Estimate request from ${name}`);
  const body = encodeURIComponent(
    `Name: ${name}\nPhone: ${phone}\nProject type: ${project}\nDetails: ${details || "Not provided"}`
  );

  formStatus.textContent = "Estimate request prepared. Your email app will open with the project details.";
  window.location.href = `mailto:?subject=${subject}&body=${body}`;
  estimateForm.reset();
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.18 }
);

document.querySelectorAll(".reveal").forEach((item) => observer.observe(item));
