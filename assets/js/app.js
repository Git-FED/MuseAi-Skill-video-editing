/* FED-OS Muse Skills — small, progressive-enhancement interactions. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.add("js-ready");

  function initMenu() {
    var button = document.querySelector(".nav-toggle");
    var nav = document.getElementById("primary-nav");
    if (!button || !nav) return;
    function setOpen(open) {
      button.setAttribute("aria-expanded", String(open));
      button.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
      nav.classList.toggle("is-open", open);
    }
    button.addEventListener("click", function () {
      setOpen(button.getAttribute("aria-expanded") !== "true");
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setOpen(false);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 760) setOpen(false);
    });
  }

  function initReveal() {
    var targets = document.querySelectorAll("[data-reveal]");
    if (!targets.length) return;
    if (reduceMotion || !("IntersectionObserver" in window)) {
      targets.forEach(function (element) { element.classList.add("is-revealed"); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });
    targets.forEach(function (element) { observer.observe(element); });
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var field = document.createElement("textarea");
      field.value = text;
      field.setAttribute("readonly", "");
      field.style.position = "fixed";
      field.style.opacity = "0";
      document.body.appendChild(field);
      field.select();
      try {
        if (document.execCommand("copy")) resolve();
        else reject(new Error("Copy was not available"));
      } catch (error) { reject(error); }
      field.remove();
    });
  }

  function initCopyButtons() {
    document.querySelectorAll("[data-copy]").forEach(function (button) {
      button.addEventListener("click", function () {
        var target = document.getElementById(button.getAttribute("data-copy"));
        if (!target) return;
        var original = button.textContent;
        copyText(target.innerText.trim()).then(function () {
          button.textContent = "Copied";
          button.setAttribute("aria-live", "polite");
          window.setTimeout(function () { button.textContent = original; }, 1800);
        }).catch(function () {
          button.textContent = "Select text";
          window.setTimeout(function () { button.textContent = original; }, 1800);
        });
      });
    });
  }

  function initYear() {
    var year = String(new Date().getFullYear());
    document.querySelectorAll("[data-year]").forEach(function (element) { element.textContent = year; });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initMenu();
    initReveal();
    initCopyButtons();
    initYear();
  });
})();
