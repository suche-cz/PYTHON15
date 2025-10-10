/*

int
- 4 bit
- 8 bit
- 16 bit
- 32 bit

True / False
1 bit


0.1 flaot 32 bitů

null


byte = 8 bitu


1 / 0

10010101


'hello'.starsWith('')

'h' + 'e' + 'l' + l' + 'o'

Array
0  1  2     3      4           5
[1, 2, null, true, 'askldjasl', []]


JS Array vlastnosti:
- složený datový typ, který obsahuje další informace
    - podporuje indexování array[index]
        - má různé metody pro modifikaci pole
            - dynamické - automaticky se rozšiřuje / změnšuje
                - heterogenní -> můžeme do něj dát různé prvky

*/

const data = [1, 2, 3]
// vložít tam 3 nové prvky
// zjisit počet prvků
// odebrat poslední 2 prvky
// získat prvek na indexu 1
// získat předposlední prvek
data.push('x') // přidá 'x'
data.pop() // odstraní poslední prvek
data.length // vrátí počet prvků
data[0] // vrátí prvek na první pozici (na nultém indexu)

data.push(item) // přidá prvek na konec
data.pop() // odstraní poslední prvek a vrátí ho
data.shift() // odstraní první prvek a vrátí ho
data.unshift(item) // přidá prvek na začátek
data.includes(value) // zjistí, zda array obsahuje hodnotu
data.indexOf(value) // vrátí index hodnoty nebo - 1
data.slice(start, end) // vrátí část array bez úpravy originálu
data.splice(start, deleteCount, ...items) // odstraní a / nebo přidá prvky přímo do originálu
data.concat(array2) // spojí dva(nebo více) arraye
data.sort(fn) // seřadí prvky(alfabeticky nebo vlastní funkcí), pro čísla (a, b) => a - b
data.reverse() // obrátí pořadí prvků v array

data.find(fn) // vrátí první prvek, který splní podmínku
data.findIndex(fn) // vrátí index prvního prvku, který splní podmínku
data.forEach(fn) // projde každý prvek(bez návratové hodnoty)
data.some(fn) // vrátí true, pokud aspoň jeden prvek splní podmínku
data.every(fn) // vrátí true, pokud všechny prvky splní podmínku
data.flat(depth) // "splácne" vnořené arraye do jednoho
data.map(fn) // vrátí nový array s výsledky funkce pro každý prvek
data.filter(fn) // vrátí nový array s prvky, které projdou podmínkou
data.reduce(fn, initial) // redukuje array na jednu hodnotu




function test(a, b) {
    return a - b;
}

(a, b) => { return a - b; }
(a, b) => a - b;
(a) => { }
a => { }
() => { }
item => { }
event => { }
