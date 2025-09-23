// DOM = Document Object Model (je to jedno z API)
// Umožňuje číst a měnit obsah, strukturu a styly stránky.

// SELECT
document.getElementById("id")
document.getElementsByClassName("class")
document.getElementsByTagName("div")
document.querySelector(".class")
document.querySelectorAll("div.class")

// MODIFY
el.textContent = "Hello"
el.innerHTML = "<b>Hi</b>"
el.value = "text"
el.src = "img.png"
el.href = "url"

// STYLE / CLASS
el.style.color = "red"
el.style.display = "none"
el.style.backgroundColor = 'red'
el.classList.add("active")
el.classList.remove("active")
el.classList.toggle("active")

// ATTRIBUTES
el.setAttribute("data-x", "123")
el.getAttribute("data-x")
el.removeAttribute("data-x")

// CREATE / INSERT
const el = document.createElement("div")
el.textContent = "new"
parent.appendChild(el)
parent.prepend(el)
parent.insertBefore(el, ref)
el.remove()

// EVENTS
el.addEventListener("click", e => {...})
el.removeEventListener("click", handler)
window.onload = () => {... }
document.addEventListener("DOMContentLoaded", fn) // todo:

// TRAVERSAL
el.parentElement
el.children
el.firstElementChild
el.lastElementChild
el.nextElementSibling
el.previousElementSibling

// FORMS
form.submit()
form.reset()
input.focus()
input.blur()
