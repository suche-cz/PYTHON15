let value = promt('Zadej jmeno:');

if (value === 'Jana') {
    console.log(1);
} else if (value === 'Petr') {
    console.log(2);
} else if (value === 'Karel') {
    console.log(3);
} else if (value === 'Alex') {
    console.log(4);
} else if (value === 'Jan') {
    console.log(5);
} else if (value === 'Oto') {
    console.log(6);
} else {
    console.log(null);
}


switch (value) {
    case 'Jana': {
        console.log(1);
        break;
    }
    case 'Petr': {
        console.log(2);
        break;
    }
    case 'Karel': {
        console.log(3);
        break;
    }
    case 'Alex': {
        console.log(4);
        break;
    }
    case 'Jan': {
        console.log(5);
        break;
    }
    case 'Oto': {
        console.log(6);
        break;
    }
    default: {
        console.log(null);
    }
}

