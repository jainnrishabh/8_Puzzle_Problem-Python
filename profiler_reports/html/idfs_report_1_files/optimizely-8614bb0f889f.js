"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["optimizely","optimizely-utils","uuid"],{67404:(e,t,n)=>{function r(e){return o(e)[0]}function o(e){let t=[];for(let n of a()){let[r,o]=n.trim().split("=");e===r&&void 0!==o&&t.push({key:r,value:o})}return t}function a(){try{return document.cookie.split(";")}catch{return[]}}function i(e,t,n=null,r=!1,o="lax"){let a=document.domain;if(null==a)throw Error("Unable to get document domain");a.endsWith(".github.com")&&(a="github.com");let i="https:"===location.protocol?"; secure":"",l=n?`; expires=${n}`:"";!1===r&&(a=`.${a}`);try{document.cookie=`${e}=${t}; path=/; domain=${a}${l}${i}; samesite=${o}`}catch{}}function l(e,t=!1){let n=document.domain;if(null==n)throw Error("Unable to get document domain");n.endsWith(".github.com")&&(n="github.com");let r=new Date().getTime(),o=new Date(r-1).toUTCString(),a="https:"===location.protocol?"; secure":"",i=`; expires=${o}`;!1===t&&(n=`.${n}`);try{document.cookie=`${e}=''; path=/; domain=${n}${i}${a}`}catch{}}n.d(t,{$1:()=>o,d8:()=>i,ej:()=>r,kT:()=>l})},31063:(e,t,n)=>{function r(e){return e.toLowerCase().replace(/-(.)/g,function(e,t){return t.toUpperCase()})}function o(e){let t={};for(let{name:n,value:o}of e.attributes)if(n.startsWith("data-optimizely-meta-")){let e=n.replace("data-optimizely-meta-","");o&&o.trim().length&&(t[r(e)]=o)}return t}n.d(t,{t:()=>o})},68379:(e,t,n)=>{let r;var o=n(24601),a=n(89359),i=n(48266),l=n(83314);let c={handleError(e){m(e)}};function u(){d();let e=document.head.querySelector("meta[name=optimizely-datafile]")?.content;return(0,i.Fs)({datafile:e,errorHandler:c})}function d(){let e=s("optimizely.logLevel");e?(0,i.Ub)(e):(0,i.EK)(null)}function s(e){try{return window.localStorage?.getItem(e)}catch(e){return null}}async function m(e){if(!l.Gb||e.message.startsWith("Optimizely::InvalidExperimentError:"))return;let t=document.head?.querySelector('meta[name="browser-optimizely-client-errors-url"]')?.content;if(!t)return;let n={message:e.message,stack:e.stack,stacktrace:(0,o.cI)(e),sanitizedUrl:(0,a.S)()||window.location.href,user:(0,o.aJ)()||void 0};try{await fetch(t,{method:"post",body:JSON.stringify(n)})}catch{}}var f=n(67404),p=n(82918),h=n(36071),y=n(59753),b=n(31063);!async function(){r=u(),await r.onReady()}(),(0,y.on)("click","[data-optimizely-event]",function(e){if(!r)return;let t=e.currentTarget,n=t.getAttribute("data-optimizely-event")||"",[o,a]=n.trim().split(/\s*,\s*/),i=(0,b.t)(t);o&&a?r.track(o,a,i):o&&r.track(o,(0,p.b)(),i)}),(0,h.N7)("[data-optimizely-experiment]",e=>{if(!r)return;let t=e.getAttribute("data-optimizely-experiment");if(!t||e.hidden)return;let n=(0,b.t)(e),o=r.activate(t,(0,p.b)(),n);if(!o)return;let a=e.querySelectorAll("[data-optimizely-variation]");for(let e of a){let t=e.getAttribute("data-optimizely-variation");e.hidden=t!==o}});let g=document.querySelector('meta[name="enabled-homepage-translation-languages"]')?.getAttribute("content")?.split(",")||[],v=(0,f.$1)("_locale_experiment").length>0&&"ko"===(0,f.$1)("_locale_experiment")[0].value&&g.includes("ko");async function _(){let e="ko_homepage_translation",t=(0,p.b)(),n=f.$1("_locale")[0]?.value?.slice(0,2);r.setForcedVariation(e,t,n),r.activate(e,t);let o=document.querySelectorAll("[data-optimizely-variation]");for(let e of o)e.hidden=n!==e.getAttribute("data-optimizely-variation");for(let e of document.querySelectorAll('form[action^="/join"]'))e.addEventListener("submit",()=>{r.track("submit.homepage_signup",t)});for(let e of document.querySelectorAll('a[href^="/join"]'))e.addEventListener("click",()=>{r.track("click.homepage_signup",t)})}async function w(){document.getElementById("signup-form")?.addEventListener("submit",()=>{let e=(0,p.b)();r.activate("ko_homepage_translation",e),r.track("submit.create_account",e)})}async function S(){if(!r)return;let e=(0,p.b)();r.activate("test_experiment",e),r.track("test_event",e)}v&&"/"===window.location.pathname&&_(),v&&"/join"===window.location.pathname&&w(),"/settings/profile"===window.location.pathname&&S()},328:(e,t,n)=>{function r(){return crypto.randomUUID()}n.r(t),n.d(t,{v4:()=>r})},89359:(e,t,n)=>{function r(e){let t=document.querySelectorAll(e);if(t.length>0)return t[t.length-1]}function o(){let e=r("meta[name=analytics-location]");return e?e.content:window.location.pathname}function a(){let e=r("meta[name=analytics-location-query-strip]"),t="";e||(t=window.location.search);let n=r("meta[name=analytics-location-params]");for(let e of(n&&(t+=(t?"&":"?")+n.content),document.querySelectorAll("meta[name=analytics-param-rename]"))){let n=e.content.split(":",2);t=t.replace(RegExp(`(^|[?&])${n[0]}($|=)`,"g"),`$1${n[1]}$2`)}return t}function i(){return`${window.location.protocol}//${window.location.host}${o()+a()}`}n.d(t,{S:()=>i})},24601:(e,t,n)=>{n.d(t,{aJ:()=>S,cI:()=>v,eK:()=>h});var r=n(82918),o=n(83314),a=n(28382),i=n(89359),l=n(23243),c=n(68202),u=n(53729),d=n(86283);let s=!1,m=0,f=Date.now();function p(e){return"AbortError"===e.name||"TypeError"===e.name&&"Failed to fetch"===e.message}function h(e,t={}){p(e)||y(g(b(e),t))}async function y(e){if(!A())return;let t=document.head?.querySelector('meta[name="browser-errors-url"]')?.content;if(t){if(w(e.error.stacktrace)){s=!0;return}m++;try{await fetch(t,{method:"post",body:JSON.stringify(e)})}catch{}}}function b(e){return{type:e.name,value:e.message,stacktrace:v(e)}}function g(e,t={}){return Object.assign({error:e,sanitizedUrl:(0,i.S)()||window.location.href,readyState:document.readyState,referrer:(0,c.wP)(),timeSinceLoad:Math.round(Date.now()-f),user:S()||void 0,turbo:(0,l.xc)(),bundler:u.A7,ui:Boolean(document.querySelector('meta[name="ui"]'))},t)}function v(e){return(0,a.Q)(e.stack||"").map(e=>({filename:e.file||"",function:String(e.methodName),lineno:(e.lineNumber||0).toString(),colno:(e.column||0).toString()}))}let _=/(chrome|moz|safari)-extension:\/\//;function w(e){return e.some(e=>_.test(e.filename)||_.test(e.function))}function S(){let e=document.head?.querySelector('meta[name="user-login"]')?.content;if(e)return e;let t=(0,r.b)();return`anonymous-${t}`}let k=!1;function A(){return!k&&!s&&m<10&&(0,o.Gb)()}if(d.iG?.addEventListener("pageshow",()=>k=!1),d.iG?.addEventListener("pagehide",()=>k=!0),"function"==typeof BroadcastChannel){let e=new BroadcastChannel("shared-worker-error");e.addEventListener("message",e=>{h(e.data.error)})}},46426:(e,t,n)=>{n.d(t,{$:()=>c,c:()=>i});var r=n(15205);let o=(0,r.Z)(a);function a(){return(document.head?.querySelector('meta[name="enabled-features"]')?.content||"").split(",")}let i=(0,r.Z)(l);function l(e){return -1!==o().indexOf(e)}let c={isFeatureEnabled:i}},23243:(e,t,n)=>{n.d(t,{AU:()=>u,Ap:()=>S,DT:()=>p,HN:()=>c,Lq:()=>i,T2:()=>_,Yg:()=>v,ag:()=>g,ck:()=>d,po:()=>b,q3:()=>s,uL:()=>w,wz:()=>f,xc:()=>l,xk:()=>h,zH:()=>a});var r=n(46426);let o="data-turbo-loaded";function a(){document.documentElement.setAttribute(o,"")}function i(){return document.documentElement.hasAttribute(o)}let l=()=>!(0,r.c)("PJAX_ENABLED"),c=e=>e?.tagName==="TURBO-FRAME";function u(e,t){let n=e.split("/",3).join("/"),r=t.split("/",3).join("/");return n===r}function d(e,t){let n=e.split("/",2).join("/"),r=t.split("/",2).join("/");return n===r}async function s(){let e=document.head.querySelectorAll("link[rel=stylesheet]"),t=new Set([...document.styleSheets].map(e=>e.href)),n=[];for(let r of e)""===r.href||t.has(r.href)||n.push(m(r));await Promise.all(n)}let m=(e,t=2e3)=>new Promise(n=>{let r=()=>{e.removeEventListener("error",r),e.removeEventListener("load",r),n()};e.addEventListener("load",r,{once:!0}),e.addEventListener("error",r,{once:!0}),setTimeout(r,t)}),f=(e,t)=>{let n=t||e.querySelectorAll("[data-turbo-replace]"),r=[...document.querySelectorAll("[data-turbo-replace]")];for(let e of n){let t=r.find(t=>t.id===e.id);t&&t.replaceWith(e)}},p=e=>{for(let t of e.querySelectorAll("link[rel=stylesheet]"))document.head.querySelector(`link[href="${t.getAttribute("href")}"],
           link[data-href="${t.getAttribute("data-href")}"]`)||document.head.append(t)},h=e=>{for(let t of e.querySelectorAll("script"))document.head.querySelector(`script[src="${t.getAttribute("src")}"]`)||y(t)},y=e=>{let{src:t}=e;if(!t)return;let n=document.createElement("script"),r=e.getAttribute("type");r&&(n.type=r),n.src=t,document.head&&document.head.appendChild(n)},b=e=>{let t=[];for(let n of e.querySelectorAll('meta[data-turbo-track="reload"]'))document.querySelector(`meta[http-equiv="${n.getAttribute("http-equiv")}"]`)?.content!==n.content&&t.push(_(n.getAttribute("http-equiv")));return t},g=e=>{let t=e.querySelector("[data-turbo-head]")||e.head;return{title:t.querySelector("title")?.textContent,transients:[...t.querySelectorAll("[data-turbo-transient]")].map(e=>e.cloneNode(!0)),bodyClasses:e.querySelector("meta[name=turbo-body-classes]")?.content,replacedElements:[...e.querySelectorAll("[data-turbo-replace]")].map(e=>e.cloneNode(!0))}},v=()=>[...document.documentElement.attributes],_=e=>e.replace(/^x-/,"").replaceAll("-","_"),w=e=>document.dispatchEvent(new CustomEvent("turbo:reload",{detail:{reason:e}})),S=(e,t)=>{for(let n of e.attributes)t.hasAttribute(n.nodeName)||"aria-busy"===n.nodeName||e.removeAttribute(n.nodeName);for(let n of t.attributes)e.getAttribute(n.nodeName)!==n.nodeValue&&e.setAttribute(n.nodeName,n.nodeValue)}}},e=>{var t=t=>e(e.s=t);e.O(0,["vendors-node_modules_github_selector-observer_dist_index_esm_js","vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-327bbf","vendors-node_modules_optimizely_optimizely-sdk_dist_optimizely_browser_es_min_js-node_modules-3f2a9e","ui_packages_soft-nav_soft-nav_ts"],()=>t(68379));var n=e.O()}]);
//# sourceMappingURL=optimizely-4a943bfeb0e2.js.map