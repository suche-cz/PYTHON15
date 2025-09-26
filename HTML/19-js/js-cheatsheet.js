// VARIABLES
let x = 1
const y = 2
var z = 3

// DATA TYPES
typeof 123        // "number"
typeof "hi"       // "string"
typeof true       // "boolean"
typeof {}         // "object"
typeof []         // "object"
typeof null       // "object"
typeof undefined  // "undefined"
typeof (() => { })   // "function"

// STRINGS
"hi".length
"hi".toUpperCase()
"hi".includes("h")
"hi".split("")
"hi".replace("h", "y")

// NUMBERS / MATH
Math.round(4.6)
Math.floor(4.9)
Math.ceil(4.1)
Math.max(1, 2, 3)
Math.random()     // 0–1

// FUNCTIONS
function f(x) { return x * 2 }
const g = x => x * 2

// CONTROL FLOW
if (x > 0) { } else { }
switch (val) { case 1: break }

// LOOPS
while (x < 5) { }

for (let i = 0; i < 5; i++) { }

do { } while (x < 5)

// ARRAYS
arr = [1, 2, 3]
arr.push(4)
arr.pop()
arr.shift()
arr.unshift(0)
arr.includes(2)
arr.indexOf(3)
arr.map(x => x * 2)
arr.filter(x => x > 1)
arr.reduce((a, b) => a + b, 0)
arr.forEach(x => console.log(x))
arr.find(x => x === 2)

// OBJECTS
obj = { a: 1, b: 2 }
obj.a
obj["b"]
Object.keys(obj)
Object.values(obj)
Object.entries(obj)

// JSON
JSON.stringify({ a: 1 })
JSON.parse('{"a":1}')

// CLASSES
class Person {
    constructor(name) { this.name = name }
    hi() { return "Hi " + this.name }
}
new Person("Tom").hi()

// PROMISES / ASYNC
fetch("/api")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err))

async function load() {
    try {
        const res = await fetch("/api")
        const data = await res.json()
    } catch (e) { console.error(e) }
}

// MODULES
export const xy = 1
import { x } from "./file.js"