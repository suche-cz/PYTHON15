// BOM = Browser Object Model (API)
// Umožňuje komunikovat/ovládat okno/prohlížeč.

// WINDOW
window.innerWidth
window.innerHeight
window.scrollX
window.scrollY
window.open("url")
window.close()
window.scrollTo(0, 0)
window.alert("Hi")
window.confirm("Sure?")
window.prompt("Enter")

// NAVIGATOR
navigator.userAgent
navigator.language
navigator.onLine
navigator.geolocation.getCurrentPosition(pos => {...})

// LOCATION (URL Adresa)
location.href
location.protocol(https)
location.host(seznam.cz, '77.75.79.222')
location.hostname(seznam.cz)
location.port(443, 80)
location.pathname('/watch', '/tag/ekonomika-29566')
location.search('?type=new&search=text')
location.hash('#') //kotva
location.reload()
location.assign("url") // nahradí aktuální stránku, s historii
location.replace("url") // nahradí aktuální stránku, bez historie

// HISTORY
// z důvodu soukromí nelze získat jednotivé stránky z historie
history.back()
history.forward()
history.go(-2)
history.pushState({ x: 1 }, "", "/new")
history.replaceState({}, "", "/edit")

// SCREEN
screen.width
screen.height
screen.availWidth
screen.availHeight
screen.orientation

// TIMERS
setTimeout(() => {...}, 1000)
clearTimeout(id)
setInterval(() => {...}, 1000)
clearInterval(id)
requestAnimationFrame(cb)
cancelAnimationFrame(id)
