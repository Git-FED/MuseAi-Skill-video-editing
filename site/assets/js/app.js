/* FED-OS Muse Skills — landing behaviour
   No framework. No credentials. Funding surfaces are resolved from
   window.FEDOS_CONFIG (see config.example.js). If config is absent, the
   static markup in index.html is used as-is. */

(function () {
  "use strict";

  var reduceMotion = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Funding buttons ----------------------------------------------
     The plan references platforms by canonical handle. We never embed a
     client ID, publishable key, buy-button ID, or merchant ID here. */
  var FUNDING = [
    { id: "sponsors", label: "GitHub Sponsors", handle: "github:Git-FED", url: "https://github.com/sponsors/Git-FED" },
    { id: "patreon",  label: "Patreon",         handle: "patreon:fedpromptly", url: "https://www.patreon.com/c/FEDpromptly" },
    { id: "kofi",     label: "Ko-fi",           handle: "ko-fi:fedpromptly", url: "https://ko-fi.com/fedpromptly" },
    { id: "bmc",      label: "Buy Me a Coffee", handle: "bmc:fedpromptly", url: "https://www.buymeacoffee.com/fedpromptly" }
  ];

  function renderFunding() {
    var mount = document.getElementById("funding-grid");
    if (!mount) return;

    FUNDING.forEach(function (f) {
      var el = document.createElement("div");
      el.className = "glass fund";
      el.innerHTML =
        '<strong>' + f.label + '</strong>' +
        '<small><code>' + f.handle + '</code></small>' +
        '<a class="btn btn-ghost" rel="noopener noreferrer" href="' + f.url + '">Support</a>';
      mount.appendChild(el);
    });
  }

  /* ---- Reveal-on-scroll (motion-safe) ------------------------------- */
  function initReveal() {
    var targets = document.querySelectorAll("[data-reveal]");
    if (!targets.length) return;

    if (reduceMotion || !("IntersectionObserver" in window)) {
      targets.forEach(function (t) { t.style.opacity = "1"; });
      return;
    }

    targets.forEach(function (t) { t.style.opacity = "0"; t.style.transition = "opacity .5s ease, transform .5s ease"; t.style.transform = "translateY(12px)"; });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.opacity = "1";
          e.target.style.transform = "none";
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });

    targets.forEach(function (t) { io.observe(t); });
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderFunding();
    initReveal();
  });
})();
