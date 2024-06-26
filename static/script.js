$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
    
    $('#toggleTheme').click(function() {
        var $htmlElement = $('html');
        var currentTheme = $htmlElement.attr('data-theme');

        if (currentTheme === 'light') {
            $htmlElement.attr('data-theme', 'dark');
            $('#currentTheme').text('dark');
        } else {
            $htmlElement.attr('data-theme', 'light');
            $('#currentTheme').text('light');
        }
    });
});

//nprogress
/* NProgress, (c) 2013, 2014 Rico Sta. Cruz - http://ricostacruz.com/nprogress
 * @license MIT */
!function(e,n){"function"==typeof define&&define.amd?define(n):"object"==typeof exports?module.exports=n():e.NProgress=n()}(this,(function(){var e,n,t={version:"0.2.0"},r=t.settings={minimum:.08,easing:"ease",positionUsing:"",speed:200,trickle:!0,trickleRate:.02,trickleSpeed:800,showSpinner:!0,barSelector:'[role="bar"]',spinnerSelector:'[role="spinner"]',parent:"body",template:'<div class="bar" role="bar"><div class="peg"></div></div><div class="spinner" role="spinner"><div class="spinner-icon"></div></div>'};function i(e,n,t){return e<n?n:e>t?t:e}function s(e){return 100*(-1+e)}t.configure=function(e){var n,t;for(n in e)void 0!==(t=e[n])&&e.hasOwnProperty(n)&&(r[n]=t);return this},t.status=null,t.set=function(e){var n=t.isStarted();e=i(e,r.minimum,1),t.status=1===e?null:e;var u=t.render(!n),c=u.querySelector(r.barSelector),l=r.speed,f=r.easing;return u.offsetWidth,o((function(n){""===r.positionUsing&&(r.positionUsing=t.getPositioningCSS()),a(c,function(e,n,t){var i;i="translate3d"===r.positionUsing?{transform:"translate3d("+s(e)+"%,0,0)"}:"translate"===r.positionUsing?{transform:"translate("+s(e)+"%,0)"}:{"margin-left":s(e)+"%"};return i.transition="all "+n+"ms "+t,i}(e,l,f)),1===e?(a(u,{transition:"none",opacity:1}),u.offsetWidth,setTimeout((function(){a(u,{transition:"all "+l+"ms linear",opacity:0}),setTimeout((function(){t.remove(),n()}),l)}),l)):setTimeout(n,l)})),this},t.isStarted=function(){return"number"==typeof t.status},t.start=function(){t.status||t.set(0);var e=function(){setTimeout((function(){t.status&&(t.trickle(),e())}),r.trickleSpeed)};return r.trickle&&e(),this},t.done=function(e){return e||t.status?t.inc(.3+.5*Math.random()).set(1):this},t.inc=function(e){var n=t.status;return n?("number"!=typeof e&&(e=(1-n)*i(Math.random()*n,.1,.95)),n=i(n+e,0,.994),t.set(n)):t.start()},t.trickle=function(){return t.inc(Math.random()*r.trickleRate)},e=0,n=0,t.promise=function(r){return r&&"resolved"!==r.state()?(0===n&&t.start(),e++,n++,r.always((function(){0==--n?(e=0,t.done()):t.set((e-n)/e)})),this):this},t.render=function(e){if(t.isRendered())return document.getElementById("nprogress");c(document.documentElement,"nprogress-busy");var n=document.createElement("div");n.id="nprogress",n.innerHTML=r.template;var i,o=n.querySelector(r.barSelector),u=e?"-100":s(t.status||0),l=document.querySelector(r.parent);return a(o,{transition:"all 0 linear",transform:"translate3d("+u+"%,0,0)"}),r.showSpinner||(i=n.querySelector(r.spinnerSelector))&&d(i),l!=document.body&&c(l,"nprogress-custom-parent"),l.appendChild(n),n},t.remove=function(){l(document.documentElement,"nprogress-busy"),l(document.querySelector(r.parent),"nprogress-custom-parent");var e=document.getElementById("nprogress");e&&d(e)},t.isRendered=function(){return!!document.getElementById("nprogress")},t.getPositioningCSS=function(){var e=document.body.style,n="WebkitTransform"in e?"Webkit":"MozTransform"in e?"Moz":"msTransform"in e?"ms":"OTransform"in e?"O":"";return n+"Perspective"in e?"translate3d":n+"Transform"in e?"translate":"margin"};var o=function(){var e=[];function n(){var t=e.shift();t&&t(n)}return function(t){e.push(t),1==e.length&&n()}}(),a=function(){var e=["Webkit","O","Moz","ms"],n={};function t(t){return t=t.replace(/^-ms-/,"ms-").replace(/-([\da-z])/gi,(function(e,n){return n.toUpperCase()})),n[t]||(n[t]=function(n){var t=document.body.style;if(n in t)return n;for(var r,i=e.length,s=n.charAt(0).toUpperCase()+n.slice(1);i--;)if((r=e[i]+s)in t)return r;return n}(t))}function r(e,n,r){n=t(n),e.style[n]=r}return function(e,n){var t,i,s=arguments;if(2==s.length)for(t in n)void 0!==(i=n[t])&&n.hasOwnProperty(t)&&r(e,t,i);else r(e,s[1],s[2])}}();function u(e,n){return("string"==typeof e?e:f(e)).indexOf(" "+n+" ")>=0}function c(e,n){var t=f(e),r=t+n;u(t,n)||(e.className=r.substring(1))}function l(e,n){var t,r=f(e);u(e,n)&&(t=r.replace(" "+n+" "," "),e.className=t.substring(1,t.length-1))}function f(e){return(" "+(e.className||"")+" ").replace(/\s+/gi," ")}function d(e){e&&e.parentNode&&e.parentNode.removeChild(e)}return t}));
document.addEventListener("htmx:configRequest",(function(e){NProgress.start()})),document.addEventListener("htmx:afterOnLoad",(function(e){NProgress.done()}))
